# `fancy-git`

An interactive branch and commit history browser for Git repositories, built for [`qol-scripts`](../README.md).

`fancy-git` provides a two-stage terminal interface using [`fzf`](https://github.com/junegunn/fzf) to explore local and remote Git branches with live graph previews, drill down into individual branch commit histories, and inspect commit diffs.

---

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Options Reference](#options-reference)
- [How It Works](#how-it-works)
- [Troubleshooting](#troubleshooting)

---

## Overview

Navigating git history across complex branch topologies can be difficult with basic `git log`. `fancy-git` provides a fast, intuitive terminal workflow:

1. **Branch Selector**: Lists all local and remote branches. The preview pane displays a colorized ASCII commit graph for the highlighted branch.
2. **Commit Browser**: Selecting a branch transitions to its chronological commit history.
3. **Commit Diff Preview**: Highlights individual commits with full `git show` colorized diffs.
4. **Interactive Backtrack**: Pressing **Enter** or **Esc** in the commit view returns you back to the branch selector.

---

## Prerequisites

- **[Git](https://git-scm.com/)**: Version control system.
- **[fzf](https://github.com/junegunn/fzf)**: Command-line fuzzy finder.

---

## Installation

`fancy-git` is an optional module in the [`qol-scripts`](../README.md) suite.

### 1. Install via the `qol` CLI

```bash
qol install fancy-git
```

### 2. Manual Symlink (Alternative)

```bash
ln -s "$QOL_SCRIPTS_PATH/src/fancy-git" "$QOL_SCRIPTS_PATH/bin/fancy-git"
```

### Uninstallation

```bash
qol uninstall fancy-git
```

---

## Usage

```bash
fancy-git [-f <folder>]
```

### Inspect Current Repository

Run `fancy-git` inside any git directory:

```bash
fancy-git
```

### Inspect Repository at Specific Path

Pass the `-f` flag to target a repository located elsewhere:

```bash
fancy-git -f ~/projects/my-repo
```

### Navigation Workflow

1. In the **Branch Selector**, scroll or fuzzy-search across branches.
2. Press **Enter** on any branch to view its commit history.
3. In the **Commit View**, browse commits while inspecting the full `git show` patch in the preview pane.
4. Press **Esc** or **Enter** to step back to the branch selection menu.
5. Press **Esc** from the branch menu to exit the tool completely.

---

## Options Reference

| Flag | Argument | Description |
|---|---|---|
| `-f` | `<folder>` | Target git repository folder path (default: current working directory) |

---

## How It Works

1. Sources `tools/qol-preamble` with `--git-verify` to ensure `git` is available.
2. Verifies that `$FOLDER/.git` exists.
3. Collects all branches via `git branch --all`, normalizes branch strings, and removes `origin/HEAD`.
4. Renders branches with `fzf`, previewing a formatted `--graph` log for each branch candidate.
5. When a branch is selected, invokes `show_commits()`, generating a formatted `git log` list piped into a secondary `fzf` instance with `git show --color=always {1}` previews.

---

## Troubleshooting

### "Error: '...' is not a git repository."
- Run the command inside a git repository or provide the path to one using `-f <folder>`.
