# `peek`

Universal compressed archive inspector with ASCII directory tree visualization, built for [`qol-scripts`](../README.md).

`peek` lets you examine the contents of various compressed archive formats without extracting them to disk, featuring an optional hierarchical ASCII tree view (`-t`).

---

## Table of Contents

- [Overview](#overview)
- [Supported Formats](#supported-formats)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Standard Listing](#standard-listing)
  - [Tree View Mode](#tree-view-mode)
- [Options Reference](#options-reference)
- [How It Works](#how-it-works)
- [Troubleshooting](#troubleshooting)

---

## Overview

Opening or extracting an unknown archive just to check its directory structure wastes disk space and time.

`peek` provides:
- **Broad Format Support**: Works across `.tar`, `.tar.gz`, `.zip`, `.jar`, `.rar`, `.7z`, `.gz`, and `.bz2`.
- **Hierarchical Tree View**: With `-t`, transforms linear archive filepaths into an indented directory tree.
- **Fast Content Peek for Compressed Text**: Automatically decompresses and previews headers for standalone `.gz` and `.bz2` files.

---

## Supported Formats

| Format | Extensions | Tree View Supported |
|---|---|:---:|
| **Tarballs** | `.tar`, `.tar.gz`, `.tgz`, `.tar.bz2`, `.tbz2`, `.tar.xz`, `.txz`, `.tar.z` | Yes |
| **Zip Archives** | `.zip`, `.jar`, `.war` | Yes |
| **RAR Archives** | `.rar` | Yes |
| **7-Zip Archives** | `.7z` | Yes |
| **Gzip Compressed** | `.gz` (single file) | Content preview |
| **Bzip2 Compressed** | `.bz2` (single file) | Content preview |

---

## Prerequisites

- **Python 3**: For converting archive paths to tree JSON data.
- **Archive Utilities** (as needed for your formats):
  - `tar` (core utility)
  - `unzip` (for `.zip`, `.jar`, `.war`)
  - `unrar` (for `.rar`)
  - `7z` (from `p7zip`, for `.7z`)
  - `zcat` / `bzcat` (standard compression tools)

---

## Installation

`peek` is an optional module in the [`qol-scripts`](../README.md) suite.

### 1. Install via the `qol` CLI

```bash
qol install peek
```

### 2. Manual Symlink (Alternative)

```bash
ln -s "$QOL_SCRIPTS_PATH/src/peek" "$QOL_SCRIPTS_PATH/bin/peek"
```

### Uninstallation

```bash
qol uninstall peek
```

---

## Usage

```bash
peek [-t] <filename>
```

### Standard Listing

Run `peek` with an archive file path to see the default file table of contents:

```bash
peek release.tar.gz
peek bundle.zip
```

### Tree View Mode

Pass `-t` to render the archive contents as a clean visual file tree:

```bash
peek -t project.zip
peek -t source.tar.xz
peek -t package.7z
```

---

## Options Reference

| Option | Description |
|---|---|
| `-t` | Render archive contents as a hierarchical ASCII directory tree |
| `<filename>` | Path to the compressed archive file (required) |

---

## How It Works

1. Sources `tools/qol-preamble` to load helper functions (`tar_to_json`, `unzip_to_json`, `json_to_tree`).
2. Checks file existence and normalizes the extension to lowercase.
3. Dispatches to the appropriate extraction tool based on pattern matching:
   - For Tarballs: Uses `tar -tvf` or `tar_to_json | json_to_tree`.
   - For Zip/Jar/War: Uses `unzip -l` or `unzip_to_json | json_to_tree`.
   - For RAR: Uses `unrar l` or parses paths via Python into JSON tree.
   - For 7z: Uses `7z l` or parses paths into JSON tree.
   - For Gz/Bz2: Displays the first 20 lines using `zcat` / `bzcat`.

---

## Troubleshooting

### "Error: Unsupported file format."
- Check the file extension. Ensure the file has a standard archive extension matching one of the supported formats.

### "Error: File '...' not found."
- Verify the path to the target archive file.
