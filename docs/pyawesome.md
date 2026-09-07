# `pyawesome`

An interactive `pyenv` and `virtualenvwrapper` environment setup bridge, built for [`qol-scripts`](../README.md).

`pyawesome` streamlines creating Python virtual environments by allowing you to select an installed [`pyenv`](https://github.com/pyenv/pyenv) Python interpreter version via [`fzf`](https://github.com/junegunn/fzf) and automatically binding it to `virtualenvwrapper`'s `mkvirtualenv`.

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

Setting up a virtual environment with a specific Python version often requires looking up full `pyenv` binary paths (e.g. `mkvirtualenv --python=$HOME/.pyenv/versions/3.12.2/bin/python my-env`).

`pyawesome` simplifies this workflow:
- Dynamically queries all Python versions installed via `pyenv`.
- Opens a clean, reverse `fzf` prompt to choose the exact Python version.
- Prompts for the new virtual environment name.
- Automatically executes `mkvirtualenv` with the chosen Python interpreter binary.

---

## Prerequisites

- **[pyenv](https://github.com/pyenv/pyenv)**: Python version management tool with at least one Python version installed (`pyenv install <version>`).
- **[virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/)**: Python virtual environment extensions.
- **[fzf](https://github.com/junegunn/fzf)**: Command-line fuzzy finder.

---

## Installation

`pyawesome` is an optional module in the [`qol-scripts`](../README.md) suite.

### 1. Install via the `qol` CLI

```bash
qol install pyawesome
```

### 2. Manual Symlink (Alternative)

```bash
ln -s "$QOL_SCRIPTS_PATH/src/pyawesome" "$QOL_SCRIPTS_PATH/bin/pyawesome"
```

### Uninstallation

```bash
qol uninstall pyawesome
```

---

## Usage

Run `pyawesome` in your shell:

```bash
pyawesome
```

### Step-by-Step Flow

1. **Select Python Version**: An `fzf` menu appears listing your installed `pyenv` versions (e.g. `3.11.8`, `3.12.2`, `pypy3.10-7.3.15`). Choose one and press **Enter** (or select `Cancel` to abort).
2. **Name Virtual Environment**: When prompted:
   ```text
   Creating Python Virtual Environment with 3.12.2
   Name the new environment:
   ```
   Type the desired name (e.g. `data-science`, `api-service`) and press **Enter**.
3. **Activate Environment**: Once created, activate the environment using:
   ```bash
   workon <name>
   ```

---

## How It Works

1. Sources `virtualenvwrapper.sh` to make the `mkvirtualenv` function available.
2. Verifies that `pyenv` and `fzf` are present in `$PATH`.
3. Runs `pyenv versions --bare` to list all locally installed Python runtimes.
4. Uses `fzf` to present the versions alongside a `Cancel` entry.
5. Reads the user-specified environment name and calls:
   ```bash
   mkvirtualenv --python="$HOME/.pyenv/versions/${selected_version}/bin/python" $venv_name
   ```

---

## Troubleshooting

### "No Python versions found."
- Install a Python version with `pyenv`:
  ```bash
  pyenv install 3.12.2
  ```

### "pyenv is not installed." / "virtualenvwrapper.sh: No such file or directory"
- Ensure `pyenv` and `virtualenvwrapper` are configured in your shell startup file (`~/.bashrc` or `~/.zshrc`).
