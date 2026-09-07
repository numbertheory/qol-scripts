# `cookbook`

An interactive terminal recipe browser for JSON recipes, built for [`qol-scripts`](../README.md).

`cookbook` lets you explore and preview your personal recipe collection formatted in JSON, organized by category or protein, using [`fzf`](https://github.com/junegunn/fzf) and [`jq`](https://github.com/jqlang/jq).

---

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Recipe Directory Structure](#recipe-directory-structure)
- [Recipe File Format](#recipe-file-format)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Troubleshooting](#troubleshooting)

---

## Overview

`cookbook` provides a two-tiered interactive terminal navigation experience for personal cooking recipes:

1. **Category / Protein Selection**: Select a folder category (e.g. `Chicken`, `Beef`, `Vegetarian`, `Dessert`).
2. **Recipe Search & Live Preview**: Browse recipes inside that category with `fzf`. The preview pane formats ingredients, instructions, and notes using `jq` and text word-wrapping.
3. **Quick Terminal Output**: Upon selecting a recipe, outputs the recipe title and formatted ingredient list for instant reference while cooking.

---

## Prerequisites

- **[fzf](https://github.com/junegunn/fzf)**: Interactive fuzzy finder.
- **[jq](https://github.com/jqlang/jq)**: Command-line JSON processor.
- `tput` and `fold` (standard utilities included with coreutils/ncurses).

---

## Installation

`cookbook` is an optional module in the [`qol-scripts`](../README.md) suite.

### 1. Install via the `qol` CLI

```bash
qol install cookbook
```

### 2. Manual Symlink (Alternative)

```bash
ln -s "$QOL_SCRIPTS_PATH/src/cookbook" "$QOL_SCRIPTS_PATH/bin/cookbook"
```

### Uninstallation

```bash
qol uninstall cookbook
```

---

## Configuration

Set the `QOL_RECIPES_FOLDER` environment variable in your shell configuration (`~/.bashrc` or `~/.zshrc`):

```bash
export QOL_RECIPES_FOLDER="$HOME/Documents/recipes"
```

---

## Recipe Directory Structure

The recipes folder should organize `.json` recipes one directory deep by category:

```text
$QOL_RECIPES_FOLDER/
├── Beef/
│   ├── beef_stew.json
│   └── smash_burgers.json
├── Chicken/
│   ├── chicken_curry.json
│   └── roasted_chicken.json
├── Pasta/
│   └── carbonara.json
└── Vegetarian/
    └── lentil_soup.json
```

---

## Recipe File Format

Recipes are structured as JSON files adhering to the schema formatted by `util/format_recipe.jq`:

```json
{
  "recipe": {
    "title": "Classic Beef Stew",
    "category": "Beef",
    "servings": 4,
    "prep_time": "20 mins",
    "cook_time": "2 hours",
    "ingredients": [
      "2 lbs beef chuck, cut into 1-inch cubes",
      "4 carrots, sliced",
      "3 potatoes, cubed",
      "1 onion, diced",
      "4 cups beef broth"
    ],
    "instructions": [
      "Sear beef in a large Dutch oven until browned on all sides.",
      "Add onions and cook until softened.",
      "Add broth, carrots, and potatoes; bring to a boil.",
      "Simmer on low heat for 2 hours until tender."
    ]
  }
}
```

---

## Usage

Run `cookbook` in your terminal:

```bash
cookbook
```

1. **Select Category**: A centered `fzf` prompt appears with all subdirectories in `$QOL_RECIPES_FOLDER`. Choose one with arrow keys and press **Enter** (or press **Esc** to exit).
2. **Select Recipe**: The second `fzf` screen lists all recipes in the category. The right side displays a formatted recipe preview.
3. **Confirm Selection**: Press **Enter** to print the recipe title and full ingredient list directly into your terminal.

---

## How It Works

1. Sources `tools/qol-preamble` to verify dependencies (`jq`, `fzf`) and initialize ANSI colors.
2. Checks that `QOL_RECIPES_FOLDER` exists and is exported.
3. Scans top-level folders via `find "$RECIPES_FOLDER" -mindepth 1 -maxdepth 1 -type d`.
4. Uses `tools/find-files -f "$TARGET_DIR" -e json` to find all recipe JSON files in the selected folder.
5. In `fzf`, invokes `jq -r -f util/format_recipe.jq` piped to `fold` for real-time wrapped preview.
6. Upon item selection, parses `.recipe.title` and `.recipe.ingredients[]` with `jq` and prints them formatted with ANSI colors.

---

## Troubleshooting

### "Set QOL_RECIPES_FOLDER in your environment where JSON recipes are found."
- Make sure to export `QOL_RECIPES_FOLDER` with the absolute path to your recipes directory in `~/.bashrc` or `~/.zshrc`.
