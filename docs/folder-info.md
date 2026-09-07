# `folder-info`

A detailed directory summary and disk inspection tool, built for [`qol-scripts`](../README.md).

`folder-info` generates an intuitive, formatted terminal report of any folder, displaying item counts, total disk usage, largest files, subdirectory file-type breakdowns, permissions, and Git repository status.

---

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Current Directory](#current-directory)
  - [Target Directory](#target-directory)
  - [Selective Section Flags](#selective-section-flags)
- [Options Reference](#options-reference)
- [How It Works](#how-it-works)
- [Troubleshooting](#troubleshooting)

---

## Overview

Investigating a directory's contents usually requires running multiple commands (`ls -la`, `du -sh`, `find`, `tree`). `folder-info` synthesizes this information into a clean, visual terminal dashboard:

- **Item Counts**: Total counts for files, subdirectories, and symbolic links.
- **Disk Usage**: Total folder size and top largest individual files across the directory tree.
- **Filetype Breakdown**: Analyzes file extensions per subdirectory (automatically excluding `.git/*`).
- **Permissions**: Displays user, group, and permissions matrix.
- **Git Status**: Shows branch name, uncommitted changes, and remote sync status if the folder is tracked by Git.

---

## Prerequisites

- Standard Unix utilities (`find`, `du`, `stat`, `awk`, `sed`, `sort`).
- `qol-scripts` preamble tools (`tools/qol-preamble`).
- **[Git](https://git-scm.com/)** *(Optional)*: For git repository status.

---

## Installation

`folder-info` is an optional module in the [`qol-scripts`](../README.md) suite.

### 1. Install via the `qol` CLI

```bash
qol install folder-info
```

### 2. Manual Symlink (Alternative)

```bash
ln -s "$QOL_SCRIPTS_PATH/src/folder-info" "$QOL_SCRIPTS_PATH/bin/folder-info"
```

### Uninstallation

```bash
qol uninstall folder-info
```

---

## Usage

```bash
folder-info [options] [folder]
```

### Current Directory

Run without arguments to inspect the current working directory:

```bash
folder-info
```

### Target Directory

Pass a directory path as the argument:

```bash
folder-info ~/Downloads
folder-info /var/log
```

### Selective Section Flags

Customize the output by omitting sections you don't need:

```bash
# Skip largest files listing and git checks
folder-info --no-largest-files --no-git

# Fast summary (counts and total size only)
folder-info --no-details --no-file-breakdown --no-largest-files
```

---

## Options Reference

| Flag | Description |
|---|---|
| `--no-details` | Skip metadata details (timestamps, owner, path) |
| `--no-file-breakdown` | Skip extension and file type breakdown |
| `--no-largest-files` | Skip listing the largest files in the directory |
| `--no-size` | Skip computing total directory disk usage |
| `--no-counts` | Skip item counts (files, folders, symlinks) |
| `--no-git` | Skip checking git repository status |
| `--no-permissions` | Skip folder permission matrix |
| `--help` | Display usage instructions and options |

---

## How It Works

1. Sources `tools/qol-preamble` with `--colors --string-tools` to import color palettes and string formatting utilities.
2. Resolves target folder path (defaults to `$PWD` if omitted).
3. Evaluates command-line flags to enable or disable individual report sections.
4. Gathers file statistics using `find`, calculates disk usage with `du`, and extracts largest files via `sort -rh`.
5. Analyzes extensions across subdirectories while filtering out internal `.git` directories.
6. If `.git` is present and git output is enabled, executes `tools/git-info-blob` to display branch and commit metrics.

---

## Troubleshooting

### "Unknown flag: ..."
- Run `folder-info --help` to view supported flags. Positional folder arguments can be passed before or after option flags.
