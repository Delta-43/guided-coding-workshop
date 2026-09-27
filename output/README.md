# Showcase: Weather Dashboard

The finished version of the app built at the workshop, extended into a full dashboard:

- current weather, feels-like, humidity, wind with a direction arrow, and sunrise/sunset
- the next 24 hours as a temperature chart with rain chance
- a 7-day outlook
- a **live contour map of the searched place** behind the stats, drawn from real elevation data
- °C / °F, quick-pick cities, and shareable links: `?city=Innsbruck` opens straight on that city

**Live:** https://delta-43.github.io/guided-coding-workshop/ (once published, see [`PUBLISH.md`](PUBLISH.md))

## How it works

It's one static file, `index.html`, with no server of its own. The browser talks directly to free, key-less services:

| What | Source |
|---|---|
| City search | Open-Meteo geocoding API |
| Weather | Open-Meteo forecast API |
| Terrain | AWS Terrain Tiles (Terrarium PNGs: height = R·256 + G + B/256 − 32768 m), traced into contours with d3-contour |
| UI | React 18 + Babel from a CDN, Anton + JetBrains Mono from Google Fonts |

In the workshop the same data came through a small FastAPI backend (`GET /weather`). This version moves that logic into the page, so it can be hosted anywhere for free.

## Run it locally

```bash
cd output
python3 -m http.server 8030
```

Open http://localhost:8030. Any static web server works.

## Hosting

`.github/workflows/pages.yml` publishes `index.html` to GitHub Pages whenever it changes on `main`. That's free for public repositories, with no account or server to maintain.

## Credits

- Weather data: [Open-Meteo](https://open-meteo.com/), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
- Elevation: [Terrain Tiles on AWS](https://registry.opendata.aws/terrain-tiles/), from SRTM, GMTED, ETOPO1 and other sources ([attribution](https://github.com/tilezen/joerd/blob/master/docs/attribution.md)).
- Contour tracing: [d3-contour](https://github.com/d3/d3-contour) (ISC).
