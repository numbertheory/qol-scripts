# `file-info`

Comprehensive, human-readable file inspection and metadata extraction, built for [`qol-scripts`](../README.md).

`file-info` analyzes any file and prints a formatted summary in your terminal, including filesystem attributes, permissions, git history, and deep introspection for archives, PDFs, images, and text files.

---

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Inspected File Types](#inspected-file-types)
  - [General Files](#general-files)
  - [Archives (ZIP / TAR)](#archives-zip--tar)
  - [PDF Documents](#pdf-documents)
  - [Images](#images)
  - [Text & Markdown](#text--markdown)
- [How It Works](#how-it-works)
- [Troubleshooting](#troubleshooting)

---

## Overview

Standard Unix utilities (`stat`, `file`, `ls -l`) display file metadata in raw, fragmented formats. `file-info` aggregates and synthesizes this data into an attractive, human-ready terminal report:

- **Filesystem & Permissions**: Absolute location, MIME type / Kind, apparent file size, octal and symbolic permissions matrix.
- **Creation & Modification Timestamps**: Accurately formats file creation and modification dates across Linux and macOS.
- **Git Awareness**: Automatically detects whether the file is tracked in a Git repository and displays commit history and blame summaries.
- **Type-Specific Introspection**: Deep dives into compressed archives, document metadata, image geometry, and word/line metrics.

---

## Prerequisites

- Standard Unix core utilities (`realpath`, `stat`, `date`, `du` or `ls`).
- **MIME Detection**: `xdg-mime` (Linux) or `mdls` (macOS).
- **Optional Tools for Specialized Introspection**:
  - `pdfinfo` (from `poppler-utils`) for PDF analysis.
  - `identify` (from `ImageMagick`) for image dimensions.
  - `git` for git repository commit information.

---

## Installation

`file-info` is an optional module in the [`qol-scripts`](../README.md) suite.

### 1. Install via the `qol` CLI

```bash
qol install file-info
```

### 2. Manual Symlink (Alternative)

```bash
ln -s "$QOL_SCRIPTS_PATH/src/file-info" "$QOL_SCRIPTS_PATH/bin/file-info"
```

### Uninstallation

```bash
qol uninstall file-info
```

---

## Usage

```bash
file-info <filename>
```

### Examples

```bash
file-info document.pdf
file-info archive.tar.gz
file-info photo.jpg
file-info src/app.py
```

---

## Inspected File Types

### General Files
Every file displays:
- **Location**: Absolute path (`realpath`).
- **Kind**: Detailed MIME type or OS file kind.
- **Size**: Human-readable size (e.g. `4.2M`, `128K`).
- **Created**: First creation date (falls back to initial git commit date if inside a git repository).
- **Modified**: Date and time of last modification.
- **Permissions**: Octal mode, symbolic representation, and user/group ownership.

### Archives (ZIP / TAR)
- Generates an interactive, ASCII tree representation of archive contents without extracting files to disk.

### PDF Documents
- Title, Author / Creator.
- Total page count.
- Document creation and modification dates.
- Page dimensions, orientation (Portrait vs. Landscape), and PDF version.

### Images
- Pixel resolution (`Width x Height`).
- Aspect orientation (`Landscape`, `Portrait`, or `Square`).

### Text & Markdown
- Line count, word count, character count, and whitespace metrics.

---

## How It Works

1. Sources `tools/qol-preamble` with `--colors --string-tools` to import formatting helpers (`print_kv`, `permissions_calc`, `unzip_to_json`, `json_to_tree`).
2. Validates that the target file exists.
3. Checks for `.git` in parent directories to determine repository status.
4. Branches on OS type (`Darwin` vs. `Linux`) to use optimal native utilities (`mdls` on macOS, `xdg-mime` / `stat` on Linux).
5. Detects MIME types and triggers specialized parsing blocks for archives, PDFs, images, and text.
6. If the file is inside a git repository, executes `$QOL_SCRIPTS_PATH/bin/tools/git-info-blob file` to append commit details.

---

## Troubleshooting

### "Error: file not found or set."
- Provide a valid path to an existing file: `file-info /path/to/file`.

### PDF metadata fields are blank
- Ensure `pdfinfo` is installed:
  ```bash
  sudo pacman -S poppler       # Arch Linux / CachyOS
  sudo apt install poppler-utils # Debian / Ubuntu
  ```
