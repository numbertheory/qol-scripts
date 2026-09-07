# `fancy-docker`

Interactive Docker image inspector and browser using `fzf`, built for [`qol-scripts`](../README.md).

`fancy-docker` displays all local Docker images in an interactive `fzf` list with syntax-highlighted `docker inspect` JSON previews, and outputs the raw JSON of the selected image.

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

Inspecting local Docker images often involves running `docker images`, copying a 12-character hexadecimal image hash, and piping `docker inspect` to `jq` or a pager.

`fancy-docker` simplifies this workflow:
- **Tabular Image List**: Displays Image ID, Repository, Tag, and Size aligned in clean columns.
- **Live Inspected Preview**: As you browse images, the preview pane immediately shows the full `docker inspect` JSON with syntax coloring.
- **Select to Output**: Pressing **Enter** prints the full JSON to stdout, suitable for piping to `jq`, clipboard tools, or files.

---

## Prerequisites

- **[Docker](https://www.docker.com/)**: Docker daemon and CLI installed and running.
- **[fzf](https://github.com/junegunn/fzf)**: Command-line fuzzy finder.
- **Optional Highlighting Tools**: [`bat`](https://github.com/sharkdp/bat) or [`jq`](https://github.com/jqlang/jq) for colored JSON preview.

---

## Installation

`fancy-docker` is an optional module in the [`qol-scripts`](../README.md) suite.

### 1. Install via the `qol` CLI

```bash
qol install fancy-docker
```

### 2. Manual Symlink (Alternative)

```bash
ln -s "$QOL_SCRIPTS_PATH/src/fancy-docker" "$QOL_SCRIPTS_PATH/bin/fancy-docker"
```

### Uninstallation

```bash
qol uninstall fancy-docker
```

---

## Usage

Run `fancy-docker` from any directory:

```bash
fancy-docker
```

- Navigate the list of local Docker images using **Up / Down** arrow keys or fuzzy search.
- The preview pane on the right renders `docker inspect {image-id}` with JSON syntax highlighting.
- Press **Enter** to exit `fzf` and print the selected image's inspect JSON to the terminal.
- Press **Esc** to cancel without output.

### Piping Output

Pipe the output directly into other tools:

```bash
# Extract environment variables of selected image
fancy-docker | jq '.[0].Config.Env'

# Copy image inspect JSON to clipboard
fancy-docker | xclip -selection clipboard
```

---

## How It Works

1. Sources `tools/qol-preamble` with `--docker-verify` to ensure the `docker` binary exists.
2. Checks for `bat` or `jq` in `$PATH` to construct the syntax-highlighted preview command (`docker inspect {1} | bat --color=always -l json` or `docker inspect {1} | jq -C .`).
3. Formats local Docker image metadata via `docker images --format "{{.ID}}\t{{.Repository}}:{{.Tag}}\t{{.Size}}"` and aligns them with `column -t`.
4. Passes the table to `fzf` with live preview.
5. If a selection was made, extracts the image ID from column 1 and outputs the full inspect JSON.

---

## Troubleshooting

### "Error: docker could not be found. Please install it."
- Install Docker and verify the Docker service is running:
  ```bash
  sudo systemctl start docker
  ```

### Permission denied when connecting to Docker daemon
- Ensure your user is part of the `docker` group:
  ```bash
  sudo usermod -aG docker "$USER"
  ```
  Then log out and log back in.
