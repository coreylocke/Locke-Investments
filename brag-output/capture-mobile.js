// Capture lockeinvestments.net at mobile viewport across scroll positions
const puppeteer = require("puppeteer");
const fs = require("fs");
const path = require("path");

const OUT = path.join(__dirname, "mobile-captures");
fs.mkdirSync(OUT, { recursive: true });

(async () => {
  const browser = await puppeteer.launch({
    headless: "shell",
    executablePath: "/Users/coreylocke/.cache/puppeteer/chrome-headless-shell/mac_arm-152.0.7977.54/chrome-headless-shell-mac-arm64/chrome-headless-shell",
    args: ["--no-sandbox", "--disable-setuid-sandbox"]
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 390, height: 844, deviceScaleFactor: 2, isMobile: true, hasTouch: true });
  await page.goto("https://lockeinvestments.net", { waitUntil: "networkidle2", timeout: 90000 });

  // let fonts and animations settle
  await new Promise(r => setTimeout(r, 2500));

  const positions = [0, 0.2, 0.4, 0.6, 0.8, 1.0];
  const scrollHeight = await page.evaluate(() => document.documentElement.scrollHeight - window.innerHeight);
  console.log("mobile scrollHeight (px):", scrollHeight);

  for (let i = 0; i < positions.length; i++) {
    const p = positions[i];
    const y = Math.round(scrollHeight * p);
    await page.evaluate(sy => window.scrollTo(0, sy), y);
    await new Promise(r => setTimeout(r, 900));
    const fn = path.join(OUT, `mobile-scroll-${String(i).padStart(3, "0")}.png`);
    await page.screenshot({ path: fn });
    console.log("saved", fn, "at y =", y);
  }

  // also grab one hero shot at top for the frame reveal
  await page.evaluate(() => window.scrollTo(0, 0));
  await new Promise(r => setTimeout(r, 800));
  await page.screenshot({ path: path.join(OUT, "mobile-hero.png") });

  await browser.close();
  console.log("DONE");
})().catch(e => { console.error("FAIL:", e.message); process.exit(1); });