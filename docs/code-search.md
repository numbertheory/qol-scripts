# `code-search`

Fast interactive code search across files using `ripgrep` and `fzf`, built for [`qol-scripts`](../README.md).

`code-search` combines the blistering search speed of [`ripgrep`](https://github.com/BurntSushi/ripgrep) (`rg`) with the fuzzy-filtering power of [`fzf`](https://github.com/junegunn/fzf) and syntax-highlighted line previews via [`bat`](https://github.com/sharkdp/bat).

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

Searching through codebases in the terminal often requires running multiple grep commands or switching between editors. `code-search` provides a fast, lightweight terminal search interface:

- **Instant Results**: Scans directory trees using `ripgrep` without header clutter.
- **Interactive Fuzzy Navigation**: Filter through matches with `fzf` in real time.
- **Contextual Syntax Highlighting**: Previews matching files in `bat`, highlighting the exact matching line number.

---

## Prerequisites

Ensure the following tools are installed on your system:

1. **[ripgrep](https://github.com/BurntSushi/ripgrep) (`rg`)**: Fast recursive line-oriented search tool.
2. **[fzf](https://github.com/junegunn/fzf)**: Command-line fuzzy finder.
3. **[bat](https://github.com/sharkdp/bat)**: `cat` clone with syntax highlighting and line highlighting.

---

## Installation

`code-search` is an optional module in the [`qol-scripts`](../README.md) suite.

### 1. Install via the `qol` CLI

Use the built-in `qol` manager to create a symlink in your `bin/` directory:

```bash
qol install code-search
```

### 2. Manual Symlink (Alternative)

If you are not using the `qol` helper:

```bash
ln -s "$QOL_SCRIPTS_PATH/src/code-search" "$QOL_SCRIPTS_PATH/bin/code-search"
```

Ensure `$QOL_SCRIPTS_PATH/bin` is in your shell's `$PATH`.

### Uninstallation

To remove the script:

```bash
qol uninstall code-search
```

---

## Usage

```bash
code-search [folder]
```

### Search Current Working Directory

Run without arguments to search inside the current directory:

```bash
code-search
```

### Search Specific Directory

Pass a target folder path as the first argument:

```bash
code-search ~/projects/my-app
```

---

## How It Works

1. **Verification**: Sources `tools/qol-preamble` to verify that `rg` and `fzf` are present in `$PATH`.
2. **Directory Resolution**: Defaults to `$PWD` if no folder parameter is supplied.
3. **Stream Pipeline**:
   - Executes `rg --line-number --no-heading '' "$FOLDER"` to recursively stream all lines in the target path.
   - Pipes results to `fzf --delimiter ':'`, parsing the output into `<filepath>:<linenumber>:<linecontent>`.
   - Uses `bat --style=numbers --color=always {1} --highlight-line {2}` in the preview pane to render the file with syntax highlighting centered on the matching line.

---

## Troubleshooting

### "Error: rg could not be found"
- Install `ripgrep` via your package manager:
  ```bash
  sudo pacman -S ripgrep    # Arch Linux / CachyOS
  sudo apt install ripgrep   # Debian / Ubuntu
  brew install ripgrep       # macOS
  ```

### "Error: fzf could not be found"
- Install `fzf` via your package manager:
  ```bash
  sudo pacman -S fzf
  ```

### Preview displays errors or plain text
- Ensure `bat` is installed and available in your `$PATH`. On some Debian/Ubuntu systems, the binary may be named `batcat`.
