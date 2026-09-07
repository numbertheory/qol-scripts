## Quality of Life Scripts

Scripts to improve quality of life while using the Kitty terminal emulator and CachyOS. Most of these scripts rely on the Kitty protocol's image viewing to be useful. Additionally, install `fzf` to enable fuzzy searching. Each script, aside from the core scripts, are all optional, so you can independently choose which ones are right for your system.

### Available Scripts

| Script | Description |
|---|---|
| [`code-search`](docs/code-search.md) | Search code with `ripgrep`, `fzf`, and `bat` line previews |
| [`color-test`](docs/color-test.md) | Display test of terminal color swatches and background colors |
| [`cookbook`](docs/cookbook.md) | Browse and preview JSON recipes grouped by category |
| [`dictionary`](docs/dictionary.md) | macOS offline dictionary and thesaurus lookup via Dictionary Services |
| [`emoji-picker`](docs/emoji-picker.md) | Search emojis with Kitty graphic previews, skin tones, and clipboard copy |
| [`fancy-cal`](docs/fancy-cal.md) | Interactive 12-month calendar navigator with keyboard controls |
| [`fancy-docker`](docs/fancy-docker.md) | Inspect local Docker images with live syntax-highlighted JSON previews |
| [`fancy-git`](docs/fancy-git.md) | Interactive Git branch graph selector and commit diff explorer |
| [`fancy-ollama`](docs/fancy-ollama.md) | Browse and inspect local Ollama LLM models with live model cards |
| [`file-info`](docs/file-info.md) | File metadata summary with archive, PDF, image, and git history inspection |
| [`folder-info`](docs/folder-info.md) | Directory summary showing item counts, disk usage, and filetype breakdowns |
| [`internet-ref`](docs/internet-ref.md) | Reference guides and cheatsheets for web and programming standards |
| [`man-explore`](docs/man-explore.md) | Interactive manual page explorer for all executables in `$PATH` |
| [`peek`](docs/peek.md) | Inspect compressed archives with optional hierarchical tree visualization |
| [`pyawesome`](docs/pyawesome.md) | Interactive `pyenv` Python version picker for `virtualenvwrapper` |
| [`starship-pick`](docs/starship-pick.md) | Interactively select and apply Starship prompt themes using `fzf` |
| [`wallpaper-pick`](docs/wallpaper-pick.md) | Select and apply desktop wallpapers with Kitty terminal image previews |
| [`weather`](docs/weather.md) | Terminal weather forecast viewer using the US National Weather Service API |

### Installation

Clone the repository to somewhere in your home directory, and add the `bin` and `core` folders to the PATH when you start your shell. For this example, we'll clone the repo to the `$HOME/.local/` folder.

```bash
git clone git@github.com:numbertheory/qol-scripts.git ~/.local/qol-scripts

# In your shell's RC file (.zshrc, .bashrc, etc.) set the path and the variable for the script updater to know where the repo is.
# Additionally, set a QOL_LOCATION, so the weather script knows what your coordinates are

export PATH=$PATH:$HOME/.local/qol-scripts/bin:$HOME/.local/qol-scripts/bin/core
export QOL_SCRIPTS_PATH=$HOME/.local/qol-scripts

# These values are for optional scripts that you install with qol install
# Only use the ones that are active in your system

# Weather
export QOL_LOCATION=38.8950,77.0363 # only four significant digits are allowed

# Cookbook
export QOL_RECIPES_FOLDER=<absolute path where your recipes are>

# Emoji picker skin tone
# Options are light, medium-light, medium, medium-dark, and dark
# can be overridden with skin tone passed as a flag, e.g. emoji-picker --medium-light
# Set QOL_SHOW_ALL_TONES to true to show all skin tones as options when you search.
export QOL_EMOJI_SKIN_TONE="medium"
export QOL_SHOW_ALL_TONES=true
```

To install an optional script, a symlink is created from the `src/` directory to `qol-scripts/bin`, which should be empty. Use the `qol install` command to install and uninstall scripts.

```bash
qol install wallpaper-pick
qol install weather
etc.
```

This way, you have more control over what is being added, and don't have to add everything in `src` to your PATH.
