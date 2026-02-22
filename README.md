## Quality of Life Scripts

Scripts to improve quality of life while using the Kitty terminal emulator and CachyOS. Most of these scripts rely on the Kitty protocol's image viewing to be useful. Additionally, install `fzf` to enable fuzzy searching. Each script, aside from the core scripts, are all optional, so you can independently choose which ones are right for your system.

### Installation

Clone the repository to somewhere in your home directory, and add the `bin` and `core` folders to the PATH when you start your shell. For this example, we'll clone the repo to the `$HOME/.local/` folder.

```bash
git clone ssh/https url

# In your shell's RC file (.zshrc, .bashrc, etc.)

export PATH=$PATH:$HOME/.local/qol-scripts/bin:$HOME/.local/qol-scripts/bin/core
```

To install an optional script, link the script from the `src/` directory to `qol-scripts/bin`, which should be empty:

```
ln -s $HOME/.local/qol-scripts/src/wallpaper-pick ~/.local/qol-scripts/bin/wallpaper-pick
```

This way, you have more control over what is being added, and don't have to add everything in `src` to your PATH.

### Script Library

- qol-check

