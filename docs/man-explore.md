# `man-explore`

Interactive command manual page explorer and search tool using `fzf`, built for [`qol-scripts`](../README.md).

`man-explore` scans all available commands in your `$PATH` and lets you browse, search, preview, and read man pages interactively without knowing exact command names in advance.

---

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage & Keybindings](#usage--keybindings)
- [How It Works](#how-it-works)
- [Troubleshooting](#troubleshooting)

---

## Overview

Finding command-line options typically requires guessing command names or running `man` sequentially. `man-explore` offers a streamlined alternative:

- **Complete `$PATH` Coverage**: Uses Bash's `compgen -c` builtin to instantaneously collect all executables on your system.
- **Live Man Page Preview**: As you filter commands with `fzf`, the right pane renders the complete manual page with ANSI escape formatting stripped via `col -b`.
- **Direct Pager Launch**: Press **Enter** on any command to open its full `man` page in your system pager (`less`).
- **Quick Clipboard Copy**: Press <kbd>Alt+c</kbd> to copy the selected command name to your clipboard and immediately return to your prompt.

---

## Prerequisites

- **[fzf](https://github.com/junegunn/fzf)**: Command-line fuzzy finder.
- `man` and `col` (standard Unix tools).
- **Clipboard Utility**: `xclip` (Linux) or `pbcopy` (macOS).

---

## Installation

`man-explore` is an optional module in the [`qol-scripts`](../README.md) suite.

### 1. Install via the `qol` CLI

```bash
qol install man-explore
```

### 2. Manual Symlink (Alternative)

```bash
ln -s "$QOL_SCRIPTS_PATH/src/man-explore" "$QOL_SCRIPTS_PATH/bin/man-explore"
```

### Uninstallation

```bash
qol uninstall man-explore
```

---

## Usage & Keybindings

Launch `man-explore` from any terminal session:

```bash
man-explore
```

### Keybindings

| Key | Action |
|---|---|
| <kbd>Enter</kbd> | Open the full manual page in your pager (`man <cmd>`) |
| <kbd>Alt+c</kbd> | Copy the command name to your clipboard and exit |
| <kbd>Ctrl+d</kbd> | Scroll preview pane down |
| <kbd>Ctrl+u</kbd> | Scroll preview pane up |
| <kbd>Esc</kbd> / <kbd>Ctrl+c</kbd> | Exit without action |

---

## How It Works

1. Sources `tools/qol-preamble` with `--fzf-verify` to ensure `fzf` is installed.
2. Invokes `compgen -c | sort -u` to generate a deduplicated list of every executable in `$PATH`.
3. Passes the list into `fzf` configured with:
   - Preview command: `man {1} 2>/dev/null | col -b || echo 'No manual entry for {1}'`.
   - Scroll bindings: `ctrl-d` and `ctrl-u`.
   - Execution binding: `enter:execute(man {1})`.
   - Clipboard binding: `alt-c:execute-silent(echo {1} | pbcopy || echo {1} | xclip -sel clip)+abort`.

---

## Troubleshooting

### "No manual entry for ..." in preview
- Some shell builtins (e.g. `cd`, `echo`) or custom functions do not have standalone man pages. For shell builtins, use `help <command>` or `man bash`.
