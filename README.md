# Math Ed Portfolio · Miami University

A program site and three sample student portfolios for the Mathematics Education
ePortfolio, built on Miami's MILE portfolio (Google Sites, UNV 101 → Capstone).

## What's here

| Path | What it is |
|---|---|
| `docs/index.html` | Program page: why a portfolio, MILE alignment, artifact list, four-year timeline, sample gallery, FAQ |
| `docs/samples/` | Three fictional student portfolios rendered to look and navigate like Google Sites: **Priya** (complete, four-year build), **Marcus** (transfer, built backward then forward), **Jordan** (sophomore, in progress) |
| `docs/templates/` | Web versions of the three planning decks: Four-Year Build, Late Start, Course Pilot |
| `decks/` | The same three decks as `.pptx` |
| `src/` | Generators. `sites.py` is the Google-Sites-style renderer with per-student themes; `site_*.py` hold each student's content; `decks.py` + `render.py` produce the decks in both formats; `index.html` is the hand-authored program page |

`docs/` is ready for GitHub Pages (Settings → Pages → Deploy from branch → `main` / `docs`).

## Build

```
python3 -m pip install python-pptx
python3 build.py              # relative links, for docs/ and Pages
python3 build.py --artifacts  # links point at the published claude.ai artifacts
```

## Sources

Miami ePortfolios Working Group, Fall 2026 (Wardle, Olejnik, Boddy, Bapst): MILE requirements,
reflection prompt families (Process / Outcomes / Integration / Development), transfer research
(Perkins & Salomon), metacognition tools (Schraw 1998; Lovett 2016; Tanner 2012).

Students, teachers, and artifacts in the samples are fictional.
