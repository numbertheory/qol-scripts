## Quality of Life Scripts

Scripts to improve quality of life while using the Kitty terminal emulator and CachyOS. Most of these scripts rely on the Kitty protocol's image viewing to be useful. Additionally, install `fzf` to enable fuzzy searching. Each script, aside from the core scripts, are all optional, so you can independently choose which ones are right for your system.

### Installation

Clone the repository to somewhere in your home directory, and add the `bin` and `core` folders to the PATH when you start your shell. For this example, we'll clone the repo to the `$HOME/.local/` folder.

```bash
git clone git@github.com:numbertheory/qol-scripts.git ~/.local/qol-scripts

# In your shell's RC file (.zshrc, .bashrc, etc.) set the path and the variable for the script updater to know where the repo is.
# Additionally, set a QOL_LOCATION, so the weather script knows what your coordinates are

export PATH=$PATH:$HOME/.local/qol-scripts/bin:$HOME/.local/qol-scripts/bin/core
export QOL_SCRIPTS_PATH=$HOME/.local/qol-scripts

# These values are for optional scripts that you isntall with qol install
# Only use the ones that are active in your system

# Weather
export QOL_LOCATION=38.8950,77.0363 # only four significant digits are allowed

# Cookbook
export QOL_RECIPES_FOLDER=<absolute path where your recipes are>

# Emoji picker skin tone
# Options are light, medium-light, medium, medium-dark, and dark
# can be overridden with skin tone passed as a flag, emoji-picker --medium-light
export QOL_EMOJI_SKIN_TONE="medium"

```

To install an optional script, a symlink is created from the `src/` directory to `qol-scripts/bin`, which should be empty. Use the `qol install` command to install and uninstall scripts.

```bash
qol install wallpaper-pick
qol install weather
etc.
```

This way, you have more control over what is being added, and don't have to add everything in `src` to your PATH.
