#!/usr/bin/env python3
"""Generate all logo variants, favicons, social images for Locke Investments."""

from PIL import Image, ImageDraw, ImageFont
import os

SRC = "/Users/coreylocke/lockeinvestments-site/assets/logo-recraft-v2.png"
OUT = "/Users/coreylocke/lockeinvestments-site/assets"

os.makedirs(OUT, exist_ok=True)

# Open the base logo
img = Image.open(SRC).convert("RGBA")
print(f"Source: {img.size}")

# --- 1. Resized PNGs ---

# Social profile square (400x400 - LinkedIn, X/Twitter, Slack)
social_square = img.resize((400, 400), Image.LANCZOS)
social_square.save(f"{OUT}/logo-400.png")
print("logo-400.png (400x400)")

# GitHub / small profile (200x200)
social_small = img.resize((200, 200), Image.LANCZOS)
social_small.save(f"{OUT}/logo-200.png")
print("logo-200.png (200x200)")

# Website header (32x32)
header_small = img.resize((32, 32), Image.LANCZOS)
header_small.save(f"{OUT}/logo-32.png")
print("logo-32.png (32x32)")

# Apple touch icon (180x180)
apple_touch = img.resize((180, 180), Image.LANCZOS)
apple_touch.save(f"{OUT}/apple-touch-icon.png")
print("apple-touch-icon.png (180x180)")

# --- 2. Favicon multi-size ---
favicon_sizes = [16, 32, 48, 64, 96, 128, 192, 256]
for s in favicon_sizes:
    f = img.resize((s, s), Image.LANCZOS)
    f.save(f"{OUT}/favicon-{s}.png")
print(f"Favicon PNGs: {', '.join(str(s) for s in favicon_sizes)}px")

# --- 3. OG Image (1200x630) ---
og = Image.new("RGBA", (1200, 630), (7, 20, 38, 255))  # #071426

# Add logo centered, sized ~200px
logo_size = 200
logo_resized = img.resize((logo_size, logo_size), Image.LANCZOS)
logo_x = (1200 - logo_size) // 2
logo_y = 80
og.paste(logo_resized, (logo_x, logo_y), logo_resized)

# Add text overlay with PIL
try:
    font_bold = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 52)
    font_regular = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 24)
except:
    font_bold = ImageFont.load_default()
    font_regular = ImageFont.load_default()

# Draw text
draw = ImageDraw.Draw(og)

# "LOCKE INVESTMENTS" centered
text1 = "LOCKE INVESTMENTS"
# PIL doesn't have great centering without bbox, use rough center
text1_y = 320
# Gold color #C5A45D
gold = (197, 164, 93)
silver = (194, 199, 206)
white = (245, 246, 247)

# Get text size
try:
    bbox = draw.textbbox((0, 0), text1, font=font_bold)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    draw.text(((1200 - tw) // 2, text1_y), text1, font=font_bold, fill=gold)
except:
    draw.text((300, text1_y), text1, font=font_bold, fill=gold)

# Subtitle
text2 = "E-Commerce  ·  Wholesale Purchasing  ·  Supplier Partnerships"
try:
    bbox2 = draw.textbbox((0, 0), text2, font=font_regular)
    tw2 = bbox2[2] - bbox2[0]
    draw.text(((1200 - tw2) // 2, text1_y + 65), text2, font=font_regular, fill=silver)
except:
    draw.text((200, text1_y + 65), text2, font=font_regular, fill=silver)

# Tagline
text3 = "Better sourcing. Stronger commerce."
try:
    bbox3 = draw.textbbox((0, 0), text3, font=font_regular)
    tw3 = bbox3[2] - bbox3[0]
    draw.text(((1200 - tw3) // 2, text1_y + 105), text3, font=font_regular, fill=white)
except:
    draw.text((350, text1_y + 105), text3, font=font_regular, fill=white)

# "Michigan, USA" footer
text4 = "Michigan, USA"
try:
    bbox4 = draw.textbbox((0, 0), text4, font=font_regular)
    tw4 = bbox4[2] - bbox4[0]
    draw.text(((1200 - tw4) // 2, 560), text4, font=font_regular, fill=silver)
except:
    pass

og.save(f"{OUT}/og-image.png")
print("og-image.png (1200x630)")

# Also create JPG version for OG
og_rgb = og.convert("RGB")
og_rgb.save(f"{OUT}/og-image.jpg", quality=92)
print("og-image.jpg (1200x630)")

# --- 4. Social profile cards ---

# X/Twitter card (800x418)
tw_card = Image.new("RGBA", (800, 418), (7, 20, 38, 255))
logo_x = (800 - 120) // 2
logo_y = 40
logo_tw = img.resize((120, 120), Image.LANCZOS)
tw_card.paste(logo_tw, (logo_x, logo_y), logo_tw)
draw_tw = ImageDraw.Draw(tw_card)
try:
    bbox = draw_tw.textbbox((0, 0), "LOCKE INVESTMENTS", font=font_bold)
    nt = bbox[2] - bbox[0]
    draw_tw.text(((800 - nt) // 2, 180), "LOCKE INVESTMENTS", font=font_bold, fill=gold)
    bbox = draw_tw.textbbox((0, 0), "Better sourcing. Stronger commerce.", font=font_regular)
    nt = bbox[2] - bbox[0]
    draw_tw.text(((800 - nt) // 2, 245), "Better sourcing. Stronger commerce.", font=font_regular, fill=white)
    bbox = draw_tw.textbbox((0, 0), "Michigan · E-Commerce · Wholesale", font=font_regular)
    nt = bbox[2] - bbox[0]
    draw_tw.text(((800 - nt) // 2, 285), "Michigan · E-Commerce · Wholesale", font=font_regular, fill=silver)
except:
    pass
tw_card.save(f"{OUT}/x-card.png")
print("x-card.png (800x418)")

tw_card_rgb = tw_card.convert("RGB")
tw_card_rgb.save(f"{OUT}/x-card.jpg", quality=92)
print("x-card.jpg (800x418)")

# --- 5. Apple icon variants ---
# iOS splash (1024x1024)
ios_splash = img.resize((1024, 1024), Image.LANCZOS)
# Add navy background canvas
ios_bg = Image.new("RGBA", (1024, 1024), (7, 20, 38, 255))
# Center logo, slightly smaller
logo_ios = img.resize((800, 800), Image.LANCZOS)
ios_bg.paste(logo_ios, ((1024-800)//2, (1024-800)//2), logo_ios)
ios_bg.save(f"{OUT}/ios-icon-1024.png")
print("ios-icon-1024.png (1024x1024)")

# Linkedin banner (1584x396) - landscape
li_banner = Image.new("RGBA", (1584, 396), (7, 20, 38, 255))
logo_li = img.resize((100, 100), Image.LANCZOS)
li_banner.paste(logo_li, (80, (396-100)//2), logo_li)
draw_li = ImageDraw.Draw(li_banner)
try:
    font_title = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 38)
    font_sub = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 20)
    draw_li.text((210, 130), "LOCKE INVESTMENTS", font=font_title, fill=gold)
    draw_li.text((210, 180), "E-Commerce Retail & Wholesale Purchasing | Michigan, USA", font=font_sub, fill=silver)
except:
    pass
li_banner.save(f"{OUT}/linkedin-banner.png")
print("linkedin-banner.png (1584x396)")

# YouTube banner (2560x1440) - simplified
yt_banner = Image.new("RGBA", (2560, 1440), (7, 20, 38, 255))
logo_yt = img.resize((200, 200), Image.LANCZOS)
yt_banner.paste(logo_yt, ((2560-200)//2, 300), logo_yt)
draw_yt = ImageDraw.Draw(yt_banner)
try:
    font_yt = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 64)
    font_yt_s = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 32)
    draw_yt.text(((2560 - draw_yt.textbbox((0,0),"LOCKE INVESTMENTS LLC", font=font_yt)[2])//2, 560), "LOCKE INVESTMENTS LLC", font=font_yt, fill=gold)
    draw_yt.text(((2560 - draw_yt.textbbox((0,0),"E-Commerce · Wholesale Purchasing · Supplier Partnerships", font=font_yt_s)[2])//2, 640), "E-Commerce · Wholesale Purchasing · Supplier Partnerships", font=font_yt_s, fill=silver)
except:
    pass
yt_banner.save(f"{OUT}/youtube-banner.png")
print("youtube-banner.png (2560x1440)")

print("\nDone! All assets generated.")
