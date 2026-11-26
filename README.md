# Voye Arts & Designs — landing page

Client landing page for **Voye Arts & Designs** (Swakopmund, Namibia):
personalised, custom-designed stationery, books and binding, cards and gifts.
*Made to be yours.*

## Run it

**Live site:** https://tangison.github.io/voye-arts/ (GitHub Pages,
deployed from `main`).

The site is plain HTML, CSS and a few lines of JavaScript. No build step.

```bash
python3 scripts/serve.py     # http://localhost:3000
```

Any static file server works too. Deploy by publishing `index.html`,
`images/` and `engine/` together (the page references both with relative
paths).

## Layout

- `index.html` — the landing page (single file: styles and scripts inline)
- `images/` — logos (SVG + PNG), favicons, product photos, illustrations
- `engine/` — the scroll-craft animation engine, copied in unedited
- `scrollcraft/` — the animation brief and the build fingerprint registry
- `assets-inbox/Voye_Startup_Pack/` — the full client startup pack this page
  was built from: stationery, forms, brand guide, social templates, originals
- `scripts/serve.py` — local preview server (hides `.git` and source folders)

## Animation

The page uses the [scroll-craft](https://github.com/nateherkai/scroll-craft)
engine (`engine/scrollcraft.js` + `.css`, byte-identical upstream copies,
never edited per project). All page-specific motion is bespoke and lives in
`index.html`, reading the engine's `--sc-p` progress token.

- **Brief and decisions:** `scrollcraft/builds/voye-landing/BRIEF.md`
  (feeling curve, grammar rationale, device score, the peak).
- **Signature move:** a teal ribbon draws itself around the final ordering
  step and ties a bow on "beautifully wrapped".
- **Other motion:** a six-plane parallax postcard fan with a gentle pointer
  lean in the hero, windowed wipes for the facts band, a staggered catalog,
  gallery prints that develop into view, a ledger line that draws down the
  five ordering steps, and a kinetic signature line in the story.
- **Accessibility:** `prefers-reduced-motion` shows every element in its
  final state with no movement; without JavaScript the page is fully
  readable and the form area offers a direct WhatsApp link. Small teal text
  uses `--mid-text` (`#256A73`), a darkened shade of the brand mid teal, to
  hold WCAG AA contrast on cream and paper.
- **Verification:** headless Chromium walks at 1440×900 and 390×844 plus a
  reduced-motion pass and a no-JS pass; screenshot strips and a contrast
  probe of composited frames live in `scrollcraft/builds/voye-landing/lab/`
  (gitignored). Zero console errors, no horizontal overflow, contrast AA on
  every visible text node, focus order checked.
- **Registry:** `scrollcraft/FINGERPRINTS.md` records this build's
  fingerprint for future uniqueness checks.

## Brand

From the client brand guide (`assets-inbox/.../03_Brand_Guide_and_Logos/`):

| Token | Hex | Use |
|---|---|---|
| Deep teal | `#0E3B4A` | text, rules, dark backgrounds |
| Mid teal | `#2E7D86` | lines, links, secondary |
| Soft aqua | `#A8D5D1` | dividers, soft fills |
| Warm gold | `#F0C654` | single accent only |
| Cream | `#F6F2EA` | paper and backgrounds |

Type: Lora (headings) and Poppins Light (body), both on Google Fonts.
Sentence case. Gold is an accent, never body text. Do not recolour, stretch,
rotate or add effects to the logos. `--mid-text` (`#256A73`) is a darkened
shade of mid teal used only where small text needs AA contrast on light
grounds; lines, large text and graphics keep the exact brand mid teal.

## Copy checks

The page copy was reviewed with the SlopMonster skill
(`npx skills use "https://github.com/itsssssjack/slopmonster" --skill "slopmonster"`).
The checker scores the visible copy of the built page:

```bash
python3 tools/deslop.py index.html   # from the skill's supporting-files directory
```

Current result: 5/5, no scored patterns matched. All factual claims (prices,
turnaround, discounts, contact details) come from the client pack. The
second-model cleanse pass did not run: no rival-family CLI is installed in
the build environment.

## Still pending from the client

Shown as pending on the stationery, and deliberately not invented on the page:

- CC registration number and tax number (BIPA registration in progress)
- Banking details
- Real product photos (planners, calendars, gift cards) to replace the pack
  photography in the gallery when the client sends them
- Fixed physical address when the client is back in the country; the footer
  currently shows only the postal box from the pack
- Domain: the page assumes `voyearts.com` (canonical + Open Graph URLs)
