# `internet-ref`

Interactive reference documents and cheatsheets for programming and internet standards, built for [`qol-scripts`](../README.md).

`internet-ref` provides instant terminal access to curated reference guides, protocol specifications, and developer cheatsheets stored in `resources/` (such as HTTP status codes, Ollama modelfiles, and more) with `fzf` search, direct CLI printing, and an optional GUI overlay.

---

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Interactive Mode (fzf)](#interactive-mode-fzf)
  - [Direct Article Output](#direct-article-output)
  - [JSON Article Index](#json-article-index)
  - [GUI Mode (Quickshell Overlay)](#gui-mode-quickshell-overlay)
- [Options Reference](#options-reference)
- [Adding Custom Reference Articles](#adding-custom-reference-articles)
- [How It Works](#how-it-works)
- [Troubleshooting](#troubleshooting)

---

## Overview

Remembering HTTP response status numbers, configuration formats, or command cheatsheets often leads to browser tab clutter.

`internet-ref` centralizes reference guides:
- **Offline & Instant**: Stored locally as clean Markdown documents in `resources/`.
- **Interactive Markdown Previews**: Browse articles in `fzf` with formatted previews via `bat` or `glow`.
- **Direct Terminal Query**: Call `internet-ref http` to output an article directly to your screen or pager.
- **Desktop Shell Integration**: Integrates with `omarchy-shell` / Quickshell for an on-demand floating reference HUD.

---

## Prerequisites

- **[fzf](https://github.com/junegunn/fzf)**: Command-line fuzzy finder.
- **[jq](https://github.com/jqlang/jq)**: JSON parsing for article metadata.
- **Optional Previewers**: [`bat`](https://github.com/sharkdp/bat) or `glow` for enhanced Markdown formatting.
- **Optional GUI**: `omarchy-shell` for the Quickshell desktop HUD overlay.

---

## Installation

`internet-ref` is an optional module in the [`qol-scripts`](../README.md) suite.

### 1. Install via the `qol` CLI

```bash
qol install internet-ref
```

### 2. Manual Symlink (Alternative)

```bash
ln -s "$QOL_SCRIPTS_PATH/src/internet-ref" "$QOL_SCRIPTS_PATH/bin/internet-ref"
```

### Uninstallation

```bash
qol uninstall internet-ref
```

---

## Usage

```bash
internet-ref [options] [article]
```

### Interactive Mode (fzf)

Run without arguments to launch the interactive selector:

```bash
internet-ref
```

- Navigate the list of topics on the left.
- Read the formatted reference guide in the preview pane on the right.
- Press **Enter** to exit and dump the full article into your terminal.
- Press **Esc** to close.

### Direct Article Output

Pass the article name, filename, or partial keyword to print it directly:

```bash
internet-ref http
internet-ref modelfile
```

### JSON Article Index

Output all registered articles in machine-readable JSON (useful for shell completions and UI launchers):

```bash
internet-ref --list-json
```

### GUI Mode (Quickshell Overlay)

If running within an `omarchy-shell` environment (e.g. Hyprland on Arch/CachyOS), toggle the Quickshell floating overlay HUD:

```bash
internet-ref --gui
```

---

## Options Reference

| Option | Description |
|---|---|
| `[article]` | Article title, filename, or partial keyword to output directly |
| `--list-json` | Output JSON array of all available reference articles |
| `--gui` | Open the interactive desktop Quickshell overlay |
| `-h, --help` | Display usage information |

---

## Adding Custom Reference Articles

You can add your own reference sheets by saving Markdown (`.md`) files into the `resources/` directory of the `qol-scripts` repository:

```bash
cat << 'EOF' > "$QOL_SCRIPTS_PATH/resources/git-cheatsheet.md"
# Git Cheatsheet

## Branching
- `git switch -c <branch>`: Create and switch to branch
- `git branch -d <branch>`: Delete local branch
EOF
```

The script automatically detects new files and extracts the top-level `# Title` for the menu.

---

## How It Works

1. Resolves symlinks to identify the true script installation directory and resources folder (`resources/`).
2. Scans for all non-hidden files in `resources/`.
3. If `--gui` is specified, delegates to `omarchy-shell shell toggle internet-ref`.
4. If `--list-json` is specified, parses the primary Markdown header `# ` of each file with `jq` and outputs JSON.
5. If an article name is provided as an argument, matches against filenames or titles and prints the content with `bat` or `cat`.
6. Otherwise, launches `fzf` with full preview window and color formatting.

---

## Troubleshooting

### "Error: Resources folder not found"
- Verify that `$QOL_SCRIPTS_PATH` is set properly or that the repository contains the `resources/` folder.
