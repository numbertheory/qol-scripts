# `emoji-picker`

Interactive emoji picker with Kitty graphics preview and clipboard integration, built for [`qol-scripts`](../README.md).

`emoji-picker` provides a fuzzy searchable emoji selector with high-resolution Kitty terminal graphics rendering (`icat`), skin tone modifier customization, and automatic clipboard copying.

---

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [Usage](#usage)
  - [Interactive Selection](#interactive-selection)
  - [Skin Tone Customization](#skin-tone-customization)
  - [Pre-Caching Emoji Graphics](#pre-caching-emoji-graphics)
- [Options & Skin Tones](#options--skin-tones)
- [How It Works](#how-it-works)
- [Troubleshooting](#troubleshooting)

---

## Overview

Finding the right emoji or dealing with skin tone modifiers in a terminal can be challenging. `emoji-picker` solves this with:

- **Graphical Previews in Terminal**: Displays rendered PNG emoji images in the preview window using the Kitty graphics protocol (`kitty +kitten icat`).
- **Comprehensive Library**: Thousands of emojis categorized from Unicode data (`src/emoji-list.txt`).
- **Skin Tone Injection**: Supports Unicode FitzPatrick skin tones across hand gestures, people, and multi-person composite emojis.
- **Instant Clipboard Copy**: Automatically copies the chosen emoji to your system clipboard (`xclip`, `xsel`, or `pbcopy`) and prints it to stdout.

---

## Prerequisites

- **[Kitty](https://sw.kovidgoyal.net/kitty/)** terminal emulator (required for visual image preview via the Kitty graphics protocol).
- **[fzf](https://github.com/junegunn/fzf)**: Command-line fuzzy finder.
- **Clipboard Utility**: `xclip` or `xsel` on Linux, or `pbcopy` on macOS.
- **Font**: Color emoji font such as `Noto Color Emoji` or `Apple Color Emoji`.

---

## Installation

`emoji-picker` is an optional module in the [`qol-scripts`](../README.md) suite.

### 1. Install via the `qol` CLI

```bash
qol install emoji-picker
```

### 2. Manual Symlink (Alternative)

```bash
ln -s "$QOL_SCRIPTS_PATH/src/emoji-picker" "$QOL_SCRIPTS_PATH/bin/emoji-picker"
```

### Uninstallation

```bash
qol uninstall emoji-picker
```

---

## Environment Variables

Configure default behavior in your `~/.bashrc` or `~/.zshrc`:

```bash
# Set your default skin tone: light, medium-light, medium, medium-dark, or dark
export QOL_EMOJI_SKIN_TONE="medium"

# When true, includes all tone variations in search results rather than just the default tone
export QOL_SHOW_ALL_TONES=true
```

---

## Usage

```bash
emoji-picker [options]
```

### Interactive Selection

Run `emoji-picker` to open the selector:

```bash
emoji-picker
```

- Type to search by description (e.g. `party`, `rocket`, `thumbs up`, `coffee`).
- As you navigate items, high-res previews render in the preview pane.
- Press **Enter** to copy the selected emoji to your clipboard and output it to the terminal.
- Press **Esc** to cancel.

### Skin Tone Customization

Override your configured default skin tone on the fly using command-line flags:

```bash
emoji-picker --light
emoji-picker --medium-light
emoji-picker --medium
emoji-picker --medium-dark
emoji-picker --dark
```

### Pre-Caching Emoji Graphics

To generate offline cached images for faster previews in the Kitty terminal:

```bash
# Uses default "Noto-Color-Emoji" font
emoji-picker --cache

# Or specify a custom font family
emoji-picker --cache "Apple-Color-Emoji"
```

Cached images are stored in `$QOL_SCRIPTS_PATH/cache/emoji/`.

---

## Options & Skin Tones

| Flag | Description |
|---|---|
| `--light` | Apply Fitzpatrick Type 1-2 (Light skin tone) |
| `--medium-light` | Apply Fitzpatrick Type 3 (Medium-light skin tone) |
| `--medium` | Apply Fitzpatrick Type 4 (Medium skin tone) |
| `--medium-dark` | Apply Fitzpatrick Type 5 (Medium-dark skin tone) |
| `--dark` | Apply Fitzpatrick Type 6 (Dark skin tone) |
| `--cache [font]` | Generate PNG cache files for all emojis in `$QOL_SCRIPTS_PATH/cache/emoji/` |

---

## How It Works

1. **Trap Cleanup**: Registers a trap on `EXIT` to invoke `kitty +kitten icat --clear` and wipe graphic buffers when leaving `fzf`.
2. **Data Parsing & Tone Injection**: Reads `src/emoji-list.txt` and processes Unicode character sequences, dynamically injecting FitzPatrick modifier bytes and Zero-Width-Joiners (ZWJ) where applicable.
3. **Fuzzy Selection**: Piped to `fzf --nth=2` (searches description while keeping raw emoji in field 1).
4. **Kitty Graphics Preview**: In the preview hook, calculates Unicode codepoints and invokes `kitty icat` with `--place` geometry referencing `$QOL_SCRIPTS_PATH/cache/emoji/`.
5. **Clipboard Execution**: Inspects available clipboard managers (`pbcopy`, `xclip`, `xsel`) and writes the selected emoji directly to the system clipboard.

---

## Troubleshooting

### Preview images are blank or show broken icons
- Ensure you are running inside a Kitty terminal window.
- Generate pre-cached images by running `emoji-picker --cache`.

### Emoji does not copy to clipboard on Linux
- Ensure `xclip` or `xsel` is installed:
  ```bash
  sudo pacman -S xclip   # Arch Linux / CachyOS
  sudo apt install xclip  # Debian / Ubuntu
  ```
