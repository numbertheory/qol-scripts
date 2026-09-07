# `fancy-ollama`

Interactive Ollama model browser and inspector using `fzf`, built for [`qol-scripts`](../README.md).

`fancy-ollama` provides a fast terminal interface to view, inspect, and select locally installed [Ollama](https://ollama.com/) LLM models with live model details.

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

When working with multiple local Large Language Models (LLMs) via Ollama, remembering exact model tags, parameters, and system prompts can be inconvenient.

`fancy-ollama` provides:
- **Instant Model Listing**: Queries all models currently installed on your local Ollama daemon.
- **Live Model Details Preview**: Renders the complete `ollama show` output (architecture, parameters, context length, system prompt, and license) in real time.
- **Fuzzy Search**: Quickly filter through your local model library with `fzf`.

---

## Prerequisites

- **[Ollama](https://ollama.com/)**: Ollama CLI and daemon installed and running.
- **[fzf](https://github.com/junegunn/fzf)**: Command-line fuzzy finder.

---

## Installation

`fancy-ollama` is an optional module in the [`qol-scripts`](../README.md) suite.

### 1. Install via the `qol` CLI

```bash
qol install fancy-ollama
```

### 2. Manual Symlink (Alternative)

```bash
ln -s "$QOL_SCRIPTS_PATH/src/fancy-ollama" "$QOL_SCRIPTS_PATH/bin/fancy-ollama"
```

### Uninstallation

```bash
qol uninstall fancy-ollama
```

---

## Usage

Launch `fancy-ollama` from your terminal:

```bash
fancy-ollama
```

- Scroll or fuzzy search through your local Ollama models.
- The preview pane displays the model card returned by `ollama show <model>`.
- Press **Enter** to select a model.
- Press **Esc** to exit.

---

## How It Works

1. Sources `tools/qol-preamble` with `--fzf-verify` to ensure `fzf` is available.
2. Runs `ollama list` and extracts model names via `awk '{ print $1 }' | tail -n +2`.
3. Feeds model names into `fzf` with a 70% width preview window executing `ollama show {}`.

---

## Troubleshooting

### "Error: fzf could not be found."
- Install `fzf` using your package manager:
  ```bash
  sudo pacman -S fzf   # Arch Linux / CachyOS
  sudo apt install fzf  # Debian / Ubuntu
  ```

### "Failed to connect to ollama" or no models listed
- Make sure the Ollama background service is running:
  ```bash
  ollama serve
  ```
- Check that you have downloaded models with `ollama pull <model>`.
