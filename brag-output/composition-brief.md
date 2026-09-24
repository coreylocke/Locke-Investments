# Hyperframes Composition Brief: Locke Investments LLC

## Objective
Create a short launch-style brag video for Locke Investments LLC (wholesale procurement & multichannel retail).

## Output
- Composition directory: `/Users/coreylocke/lockeinvestments-site/brag-output/composition/`
- Rendered video: `/Users/coreylocke/lockeinvestments-site/brag-output/brag.mp4`
- Format: landscape — 1920x1080
- Duration: 19 seconds

## Source Material
- Project root: `/Users/coreylocke/lockeinvestments-site/`
- Primary files read: `index.html` (single-file site, 1164 lines)
- Product name: Locke Investments LLC
- Tagline / strongest claim: "Better sourcing. Stronger commerce."
- Key UI or visual moment to recreate: the hero supply-chain route SVG — 4 nodes (SUPPLIERS → LOCKE INVESTMENTS LLC → 3PL INFRASTRUCTURE → RETAIL CHANNELS → CONSUMERS) connected by animated vertical flow arrows; and the gold `.gold-block` wholesale-account section
- Copy that must appear verbatim:
  - "Better sourcing."
  - "Stronger commerce."
  - "Wholesale Procurement · Multichannel Retail · Supplier Partnerships"
  - "Open for wholesale accounts"
  - "Let's build a long-term purchasing relationship."

## Creative Direction
- Tone preset: `polished`
- Creative direction: quiet premium B2B supply-chain film
- Interpretation: few scenes, long holds, generous negative space; type confident and restrained; motion structural (node reveals, flow-line drawing) not playful; gold (#C5A45D) the only accent
- Angle: trace the supply chain the company sits inside — Suppliers → Locke → 3PL → Retail — then land the invitation to wholesale suppliers
- Hook: "Better sourcing." in white 800-weight Manrope on deep navy with a gold top status strip
- Outro / punchline: gold block "Open for wholesale accounts — Let's build a long-term purchasing relationship." + wordmark
- Avoid:
  - Generic SaaS language ("streamline", "unlock")
  - Abstract filler visuals / color washes
  - Playful or rounded motion (site uses sharp 2px rectangles)

## Visual Identity
- Background: `#071426`
- Panel: `#10243D`, `#0C1E33`
- Accent: `#C5A45D` (gold), hover `#D4B87A`
- Text: `#F5F6F7` (ink), `#E3E6EA` (muted), `#C2C7CE` (silver)
- Lines: rgba(245,246,247,.12)
- Display font: Manrope 700/800 (site uses Manrope only)
- Body font: Manrope 400/500/600
- Visual references from the project: status bar (4 gold-labeled cells), sharp 2px-radius rectangles, route diagram, category chip grid, gold-block CTA section

## Storyboard
See `/Users/coreylocke/lockeinvestments-site/brag-output/brag-plan.md` — it is the creative contract.

Scene summary:
1. Hook — 2.5s — "Better sourcing." type reveal with gold status strip
2. The Route — 6s — 4 nodes + 3 flow lines animate in sequence (site's route SVG)
3. Stronger Commerce — 3.5s — route recedes, headline slams, gold word, sub-line
4. Categories & Verification — 4.5s — "What we source" chips + "What suppliers get" checklist
5. Outro — 3s — gold block + wordmark, fade out

## Audio
- Audio role: cinematic support with a warm corporate presence
- Audio arc: quiet open → building route steps → bell payoff on the claim → structured ticks → warm fade under the logo
- Music: `happy-beats-business-moves-vol-12-by-ende-dot-app.mp3` (steady/clean — polished & cinematic)
- Music treatment: volume ~0.28, gentle fade-in, small swell at route completion (~Scene 3), fade under final logo
- Music cue guidance: bundled preset at `/Users/coreylocke/.hermes/skills/brag/assets/music/cues/happy-beats-business-moves-vol-12-by-ende-dot-app.music-cues.md` — use 2-3 strong cues for the route completion and outro
- Audio-reactive treatment: subtle; gold glow and node panels breathe gently with RMS/bass. No waveform/equalizer visuals.
- Audio-coupled moments:
  - Scene 2 — 4 node arrivals + 3 flow-line draws (soft drops / whoosh-lite; accent line draws)
  - Scene 3 — bell on "Stronger commerce." landing
  - Scene 4 — chip ticks (accent first + last only)
  - Scene 5 — final impactSoft + logo settle
- SFX selection guidance: polished restraint — 2-3 cues max total beyond the natural node accents; prefer low high-frequency-risk files (`sfx-analysis.md`)
- SFX analysis guidance: `/Users/coreylocke/.hermes/skills/brag/assets/sfx/sfx-analysis.md`
- Exact SFX choice: Hyperframes chooses filenames, timestamps, density, volume based on the implemented animation.
- Audio files: copy music into `composition/assets/music/`; copy chosen SFX into `composition/assets/sfx/`.

## Hyperframes Instructions
Build the composition for this brief per the Hyperframes domain skills (`hyperframes-core`, `hyperframes-animation`, `hyperframes-creative`, `hyperframes-keyframes`, `hyperframes-cli`). /brag is its own workflow — do not enter the hyperframes entry-point intent interview. Prefer native Hyperframes conventions.

Requirements:
- Show real UI/copy from the site (route diagram, gold block, verbatim lines)
- All text readable in the final render
- 15-25s total (19s target)
- Music + tasteful SFX layer on
- Treat music cues as optional timing hints; 1-3 strong cue locks max
- Run `npx hyperframes check` — must pass with zero errors before render