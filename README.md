# Names in Fashion

An interactive chart of U.S. baby-name popularity from 1880 to 2025. Students look up any name that ever reached the top 1,000, compare up to four names, and browse the top ten for any year. By Gwen Sharp, as a companion to Chapter 5 (Culture) of *A Sociology Experiment*.

**Live site:** https://gsharpokie.github.io/babynames/

## What it does

- **How popular was it?** A line chart of each name’s rank by year (1 at the top). Five ready-made comparisons illustrate ideas from the sociology of culture: names of their time (Linda, Jennifer, Jason), names that moved from boys to girls (Ashley, Leslie), comebacks (Emma, Hazel, Theodore, Oliver), pop culture (Madison, Arya, Khaleesi), and names that never left (Mary, Elizabeth, James, William). A table gives each name’s best rank and years on the list.
- **The top ten in any year,** with a slider from 1880 to 2025.
- **What sociologists see in names,** drawing on Stanley Lieberson’s *A Matter of Taste*, plus discussion questions.

## Files

| File | What it is |
|---|---|
| `index.html` | The page |
| `data/names.json` | Every name’s rank by year, plus the top ten for each year |
| `tools/build_names.py` | The script that built `data/names.json` |

## Data

Social Security Administration, “Popular Baby Names”: the 1,000 most popular names for girls and for boys each year, 1880–2025 (https://www.ssa.gov/oact/babynames/). The lists were compiled from Arul John’s copy at https://github.com/aruljohn/popular-baby-names because the SSA site couldn’t be reached directly when the page was built. Spot checks match SSA’s published rankings (for example, Linda #1 in 1947–1952, Jennifer #1 in 1970–1984, Olivia and Liam #1 in 2025).

The data show ranks, not numbers of babies, and only names in the top 1,000.

## Updating it each year

SSA releases the previous year’s names each May. To add a year:

1. Download or clone https://github.com/aruljohn/popular-baby-names once it has the new year.
2. In `tools/build_names.py`, change `Y1 = 2025` to the new year.
3. Run `python tools/build_names.py path/to/popular-baby-names data/names.json`.
4. Upload the new `data/names.json` to GitHub, and change “2025” in the text of `index.html`.

This is a job for someone comfortable running a script; Claude can do it for you.

## Previewing on your own computer

Opening `index.html` directly won’t load the data (browsers block that). Open a terminal in this folder, run `python -m http.server`, and go to http://localhost:8000.

## Turning on the site (one time)

Go to **Settings → Pages**. Under **Build and deployment**, set **Source** to **Deploy from a branch**, choose the **main** branch and the **/ (root)** folder, and select **Save**. Keep Issues turned on so the “Suggest a correction” link works.

## Author

Created by Gwen Sharp ([@gsharpokie](https://x.com/gsharpokie)).

## License

© 2026 Gwen Sharp. Licensed under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/): you may share and adapt it for noncommercial purposes with credit. See [LICENSE](LICENSE). The name rankings are U.S. government data; this license covers the page’s design, text, and code.
