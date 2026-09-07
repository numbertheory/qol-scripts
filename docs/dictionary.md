# `dictionary`

Offline dictionary and thesaurus lookup using macOS Dictionary Services and `fzf`, built for [`qol-scripts`](../README.md).

> [!NOTE]
> `dictionary` requires **macOS (Darwin)** as it interacts directly with Apple's native CoreServices Dictionary APIs.

---

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Dictionary Search](#dictionary-search)
  - [Thesaurus Mode](#thesaurus-mode)
  - [Custom Dictionary Selection](#custom-dictionary-selection)
- [Options Reference](#options-reference)
- [How It Works](#how-it-works)
- [Troubleshooting](#troubleshooting)

---

## Overview

macOS ships with comprehensive offline dictionaries and thesauri. `dictionary` leverages these offline databases via Python's PyObjC bridge and brings them directly into your terminal workflow:

- **Offline Speed**: Instantaneous word definitions without internet requests.
- **Fuzzy Context Window**: Searches `/usr/share/dict/words` to show spelling suggestions and nearby alphabetical entries.
- **Rich Preview**: View full formatted definitions and etymology in an interactive `fzf` split window.
- **Thesaurus Mode**: Access synonyms and antonyms using the built-in Oxford American Writer's Thesaurus.

---

## Prerequisites

1. **macOS** (OS X 10.11+)
2. **Python 3** with `pyobjc-framework-CoreServices`:
   ```bash
   pip3 install pyobjc-framework-CoreServices
   ```
3. **[fzf](https://github.com/junegunn/fzf)**: Command-line fuzzy finder.

---

## Installation

`dictionary` is an optional module in the [`qol-scripts`](../README.md) suite.

### 1. Install via the `qol` CLI

```bash
qol install dictionary
```

### 2. Manual Symlink (Alternative)

```bash
ln -s "$QOL_SCRIPTS_PATH/src/dictionary" "$QOL_SCRIPTS_PATH/bin/dictionary"
```

### Uninstallation

```bash
qol uninstall dictionary
```

---

## Usage

```bash
dictionary [options] <word> [dictionary-name]
```

### Dictionary Search

Look up definitions in the default Oxford Dictionary of English / New Oxford American Dictionary:

```bash
dictionary serendipity
dictionary ephemeral
```

### Thesaurus Mode

Use the `-t` or `--thesaurus` flag to switch to thesaurus mode:

```bash
dictionary -t eloquent
dictionary --thesaurus pragmatic
```

### Custom Dictionary Selection

Specify an alternate dictionary by name as the second argument (e.g. `Apple`, `Oxford`):

```bash
dictionary compute Apple
```

---

## Options Reference

| Option | Description |
|---|---|
| `-t, --thesaurus` | Look up synonyms in the macOS thesaurus instead of definitions |
| `<word>` | Target word to search for (required) |
| `[dictionary-name]` | Optional query to select a specific installed dictionary (default: `Oxford`) |

---

## How It Works

1. **Platform Check**: Verifies that `$OSTYPE` starts with `darwin`.
2. **Dependency Check**: Confirms `CoreServices` is importable via Python 3.
3. **Dictionary Resolution**: Invokes `util/dictionary.py` to match the target dictionary service.
4. **Candidate Gathering**: Uses `grep -C 100` against `/usr/share/dict/words` to generate a candidate pool of valid nearby words.
5. **Validation**: Filters candidates with `CoreServices.DCSCopyTextDefinition` so only defined words appear.
6. **Fuzzy UI**: Opens `fzf` focused on the target word line, updating the definition preview dynamically as you navigate. Pressing **Enter** outputs the full definition directly to the terminal.

---

## Troubleshooting

### "Error: This script requires macOS Dictionary Services."
- This script depends on macOS private framework APIs and cannot run natively on Linux.

### "Error: Missing 'pyobjc-framework-CoreServices'."
- Install the required PyObjC framework bindings:
  ```bash
  pip3 install pyobjc-framework-CoreServices
  ```
