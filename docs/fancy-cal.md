# `fancy-cal`

An interactive 12-month terminal calendar navigator, built for [`qol-scripts`](../README.md).

`fancy-cal` presents an interactive 12-month calendar view with keyboard controls for jumping across months, searching specific years, and resetting to the current date.

---

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage & Navigation Controls](#usage--navigation-controls)
- [How It Works](#how-it-works)
- [Troubleshooting](#troubleshooting)

---

## Overview

While standard terminal `cal` displays single months or fixed years, planning ahead often requires browsing multi-month rolling windows.

`fancy-cal` provides:
- **Rolling 12-Month Block**: Displays a full year's worth of calendar blocks starting from the selected month.
- **Interactive Hotkeys**: Single-keypress controls for smooth forward and backward traversal.
- **Year Jump**: Instantly jump to any 4-digit calendar year.
- **Cross-Platform Compatibility**: Automatically adapts between GNU `date` and BSD/macOS `date`, as well as `cal --twelve` and `cal -A 11`.

---

## Prerequisites

- `cal` (from `util-linux` on Linux, or default BSD `cal` on macOS).
- `date` and `col` (standard Unix core utilities).

---

## Installation

`fancy-cal` is an optional module in the [`qol-scripts`](../README.md) suite.

### 1. Install via the `qol` CLI

```bash
qol install fancy-cal
```

### 2. Manual Symlink (Alternative)

```bash
ln -s "$QOL_SCRIPTS_PATH/src/fancy-cal" "$QOL_SCRIPTS_PATH/bin/fancy-cal"
```

### Uninstallation

```bash
qol uninstall fancy-cal
```

---

## Usage & Navigation Controls

Run `fancy-cal` in your terminal:

```bash
fancy-cal
```

### Keyboard Controls

| Key | Action | Description |
|---|---|---|
| <kbd>n</kbd> | **Next** | Advance forward by 1 month |
| <kbd>p</kbd> | **Previous** | Step backward by 1 month |
| <kbd>t</kbd> | **Today** | Reset to current month and year |
| <kbd>s</kbd> | **Search** | Prompt for a 4-digit year (`YYYY`) and jump directly to it |
| <kbd>q</kbd> | **Quit** | Exit the calendar |

---

## How It Works

1. Sources `tools/qol-preamble` with `--cal-verify` to ensure `cal` is installed.
2. Maintains an integer `offset` variable representing the month displacement relative to today.
3. Computes the starting date using GNU `date -d "$offset month"` or BSD `date -v${offset}m`.
4. Renders a decorative header bar with formatted ANSI colors.
5. Invokes `cal --twelve` (or `cal -A 11 -m`) through `col -b` to display clean 12-month calendar layouts.
6. Reads user keystrokes in raw mode (`read -n 1 -s -r`), updating the offset and re-rendering on each keypress.

---

## Troubleshooting

### "Error: cal could not be found. Please install it."
- Install `util-linux`:
  ```bash
  sudo pacman -S util-linux    # Arch Linux / CachyOS
  sudo apt install bsdmainutils # Debian / Ubuntu
  ```
