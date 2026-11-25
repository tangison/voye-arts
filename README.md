# Voye Arts & Designs — landing page

Client landing page for **Voye Arts & Designs** (Swakopmund, Namibia):
custom, handmade stationery, books and binding, cards and gifts.
*Made to be yours.*

## Run it

The site is plain HTML, CSS and a few lines of JavaScript. No build step.

```bash
python3 scripts/serve.py     # http://localhost:3000
```

Any static file server works too. Deploy by publishing `index.html` and
`images/` together (the page references `images/` with relative paths).

## Layout

- `index.html` — the landing page (single file: styles and scripts inline)
- `images/` — logos (SVG + PNG), favicons, product photos, illustrations
- `assets-inbox/Voye_Startup_Pack/` — the full client startup pack this page
  was built from: stationery, forms, brand guide, social templates, originals
- `scripts/serve.py` — local preview server (hides `.git` and source folders)

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
rotate or add effects to the logos.

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
- Instagram handle confirmation (printed as `@voye_artsdesign`)
- Domain: the page assumes `voyearts.com` (canonical + Open Graph URLs)
