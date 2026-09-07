# `wallpaper-pick`

Interactive desktop wallpaper selector with Kitty terminal image previews, built for [`qol-scripts`](../README.md).

`wallpaper-pick` scans image files in a directory and provides an interactive `fzf` picker with real-time terminal graphic previews (via Kitty `icat`), applying the chosen image as your desktop background on macOS or Linux.

---

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Troubleshooting](#troubleshooting)

---

## Overview

Setting a desktop background from a large library of wallpaper images usually requires using a GUI file manager.

`wallpaper-pick` brings this workflow to the terminal:
- **Terminal Graphics Preview**: Renders high-fidelity thumbnails of wallpaper candidates inside your terminal using Kitty's graphics protocol.
- **Cross-Platform**: Natively sets desktop wallpaper on macOS (via Finder AppleScript) and Linux window managers (via your configured wallpaper tool).
- **Fast Fuzzy Filtering**: Quickly jump to images by filename or directory.

---

## Prerequisites

- **[Kitty](https://sw.kovidgoyal.net/kitty/)** terminal emulator (required for the image preview protocol).
- **[fzf](https://github.com/junegunn/fzf)**: Command-line fuzzy finder.
- **Linux Wallpaper Setter**: On Linux, ensure your system has a wallpaper utility configured (e.g. `swww`, `feh`, `hyprpaper`, or through `CORE_COMMAND`).

---

## Installation

`wallpaper-pick` is an optional module in the [`qol-scripts`](../README.md) suite.

### 1. Install via the `qol` CLI

```bash
qol install wallpaper-pick
```

### 2. Manual Symlink (Alternative)

```bash
ln -s "$QOL_SCRIPTS_PATH/src/wallpaper-pick" "$QOL_SCRIPTS_PATH/bin/wallpaper-pick"
```

### Uninstallation

```bash
qol uninstall wallpaper-pick
```

---

## Usage

Navigate to your wallpapers directory (or run it from anywhere if your wallpapers folder is indexed):

```bash
cd ~/Pictures/Wallpapers
wallpaper-pick
```

- Navigate the image list with arrow keys.
- Inspect the high-resolution image preview rendered in the right pane.
- Press **Enter** to apply the wallpaper and exit.
- Press **Esc** to cancel.

---

## How It Works

1. Sources `tools/qol-preamble` with `--fzf-verify`.
2. Uses `$QOL_SCRIPTS_PATH/bin/tools/find-files` to scan for supported image files (`.jpg`, `.jpeg`, `.png`, `.webp`).
3. Pipes image paths into `$QOL_SCRIPTS_PATH/bin/tools/fzf-prev`, which launches `fzf` configured with `kitty icat` previews.
4. On selection:
   - **macOS**: Executes an AppleScript command telling Finder to update the desktop picture to the chosen POSIX file path.
   - **Linux**: Executes the command configured in `${CORE_COMMAND} <image_path>` to apply the background.

---

## Troubleshooting

### Preview images do not appear
- Ensure you are running inside a Kitty terminal window.
- Check that the image format is supported (`.png`, `.jpg`, `.jpeg`, `.webp`).
