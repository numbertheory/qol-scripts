# `color-test`

A terminal color palette display test tool, built for [`qol-scripts`](../README.md).

`color-test` previews terminal foreground and background color rendering against the color definitions provided by `qol-scripts/bin/tools/set-colors`.

---

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [Usage](#usage)
  - [Default Palette Test](#default-palette-test)
  - [Custom Background Color](#custom-background-color)
- [Options Reference](#options-reference)
- [Supported Colors](#supported-colors)
- [How It Works](#how-it-works)

---

## Overview

Terminal color rendering depends heavily on terminal emulator configurations, 256-color support, and truecolor support. `color-test` allows you to:
- Test all configured color swatches defined by `qol-scripts`.
- Check how foreground text styles appear across different background colors.
- Verify terminal ANSI escape code handling.

---

## Prerequisites

- Compatible terminal emulator (such as Kitty, Alacritty, Ghostty, Foot, etc.) supporting 256 or true color escape sequences.
- `qol-scripts` core tools installed and `QOL_SCRIPTS_PATH` defined in your environment.

---

## Installation

`color-test` is an optional module in the [`qol-scripts`](../README.md) suite.

### 1. Install via the `qol` CLI

```bash
qol install color-test
```

### 2. Manual Symlink (Alternative)

```bash
ln -s "$QOL_SCRIPTS_PATH/src/color-test" "$QOL_SCRIPTS_PATH/bin/color-test"
```

### Uninstallation

```bash
qol uninstall color-test
```

---

## Environment Variables

| Variable | Description | Required |
|---|---|---|
| `QOL_SCRIPTS_PATH` | Path to your `qol-scripts` repository (e.g. `~/.local/qol-scripts`). Used to locate `bin/tools/set-colors`. | **Yes** |

Ensure this is exported in your `~/.bashrc` or `~/.zshrc`:

```bash
export QOL_SCRIPTS_PATH="$HOME/.local/qol-scripts"
```

---

## Usage

```bash
color-test [--bg COLOR|default]
```

### Default Palette Test

Run without options to test the color swatches on your terminal's default background:

```bash
color-test
```

### Custom Background Color

Specify an alternate background color:

```bash
color-test --bg blue
color-test --bg=dark_orange
```

---

## Options Reference

| Option | Description |
|---|---|
| `--bg <COLOR>` | Sets the test background color (default: `default`) |
| `--bg=<COLOR>` | Alternative syntax for setting background color |
| `-h, --help` | Display usage instructions and color examples |

---

## Supported Colors

The following named colors can be passed to `--bg`:

- `default`
- `red`, `green`, `yellow`, `blue`, `cyan`, `magenta`
- `gray`, `light_gray`, `silver`, `white`, `black`
- `teal`, `maroon`, `purple`, `violet`, `lavender`
- `lime`, `brown`, `gold`
- `orange`, `dark_orange`, `pink`

---

## How It Works

1. Validates that `$QOL_SCRIPTS_PATH` is defined in your shell environment.
2. Parses CLI flags and normalizes color name inputs to lowercase.
3. Validates the selected background name against an allowed color whitelist.
4. Invokes `$QOL_SCRIPTS_PATH/bin/tools/set-colors --bg <color>` to render color swatches and text attribute samples directly in your terminal.
