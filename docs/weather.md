# `weather`

A weather forecast viewer in your terminal using the National Weather Service API and `fzf`, built for [`qol-scripts`](../README.md).

`weather` queries live, detailed forecast data from the US National Weather Service (`api.weather.gov`), displaying day and night forecast periods with weather emoji icons, heat colors, relative update timestamps, and a detailed forecast side-by-side preview pane.

---

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Troubleshooting](#troubleshooting)

---

## Overview

Checking local weather from the command line is often either too rudimentary (plain temperatures) or too noisy (large ASCII art maps).

`weather` delivers an ideal balance:
- **Official US NWS Data**: Retrieves forecasts directly from `api.weather.gov` for exact geographic coordinates.
- **Dynamic Emoji Icons**: Maps conditions (sunny, rain, snow, fog, clouds, thunderstorms) to clear Unicode emoji indicators.
- **Heat-Indexed Colors**: Automatically colorizes temperatures based on warm vs. cold thresholds.
- **Relative Update Timestamp**: Displays when the forecast was last refreshed (e.g. `24 mins ago`).
- **Comprehensive Preview**: Highlights period names, temperatures, concise conditions, and full narrative forecasts in the preview pane.

---

## Prerequisites

- **[curl](https://curl.se/)**: Used to fetch NWS endpoints.
- **[jq](https://github.com/jqlang/jq)**: JSON query and mathematical transformations.
- **[fzf](https://github.com/junegunn/fzf)**: Terminal UI and preview layout.

---

## Installation

`weather` is an optional module in the [`qol-scripts`](../README.md) suite.

### 1. Install via the `qol` CLI

```bash
qol install weather
```

### 2. Manual Symlink (Alternative)

```bash
ln -s "$QOL_SCRIPTS_PATH/src/weather" "$QOL_SCRIPTS_PATH/bin/weather"
```

### Uninstallation

```bash
qol uninstall weather
```

---

## Configuration

`weather` requires your latitude and longitude coordinates exported in the `QOL_LOCATION` environment variable in your `~/.bashrc` or `~/.zshrc`:

```bash
# Format: "latitude,longitude" (up to 4 decimal places)
# Example: Washington, DC
export QOL_LOCATION="38.8895,-77.0353"

# Example: New York City, NY
export QOL_LOCATION="40.7484,-73.9857"
```

> [!TIP]
> The US National Weather Service API (`api.weather.gov`) covers US locations and territories. To find your latitude and longitude, search your city on [OpenStreetMap](https://www.openstreetmap.org) or Google Maps.

---

## Usage

Run `weather` in your terminal:

```bash
weather
```

- Browse upcoming daytime and nighttime forecast periods with arrow keys.
- Inspect the full meteorological narrative and wind/precipitation descriptions in the right pane.
- Press **Enter** or **Esc** to exit.

---

## How It Works

1. Sources `tools/qol-preamble` with `--curl-verify` to ensure network tools are available.
2. Validates that `$QOL_LOCATION` is set.
3. Calls `https://api.weather.gov/points/$QOL_LOCAL` to discover the grid forecast URL and local zone station name.
4. Queries the forecast endpoint and calculates relative elapsed time since NWS `updateTime` using `jq` epoch math.
5. Formats each forecast period in `jq`:
   - Matches keywords to select weather emojis (`☀️`, `🌧️`, `❄️`, `☁️`, `🌫️`, `⚡`, `🌡️`).
   - Applies warm (`\033[33m`) or cool (`\033[36m`) ANSI colors according to temperature values.
6. Presents the formatted periods in `fzf` with a rounded border, station name header, last updated footer, and word-wrapped preview pane.

---

## Troubleshooting

### "QOL_LOCATION must be set in the environment to use weather."
- Add `export QOL_LOCATION="<latitude>,<longitude>"` to your shell profile and reload your shell.

### "curl: (22) The requested URL returned error: 404"
- Ensure your coordinates are within the United States or US territories (NWS coverage area).
- Verify that your coordinate string does not exceed four decimal places (e.g. `38.8950,77.0363`).
