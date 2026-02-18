# MyAnkiConfig

Custom modifications for Anki focused on fast editing and preserving formatting during study workflows.

## Features

* Paste strictly what you copied (no formatting loss, no background stripping).
* Flags remapped to `Alt + (number)` for easier access.
* Quick text coloring shortcuts to reduce editor friction.

## Text Color Shortcuts

* `Ctrl + 1` → <span style="color:#ffaa00;"><b>Orange (#ffaa00)</b></span>
* `Ctrl + 2` → <span style="color:#65cb96;"><b>Green (#65cb96)</b></span>
* `Ctrl + 3` → <span style="color:#ff0000;"><b>Red (#ff0000)</b></span>
* `Ctrl + 4` → <span style="color:#ffffff; background-color:#444;"><b>White (#ffffff)</b></span>

The first three colors are automatically applied with **bold** to improve visual scanning while reviewing.

## Purpose

This setup removes unnecessary editor friction when creating or editing cards, allowing high–speed annotation without repeatedly opening formatting menus.

Designed for heavy daily use where small time losses compound into real inefficiency.

## How to use
### 1) Download these Add-ons:
* editor: paste raw unfiltered full html, 1765712663
* Customize Keyboard Shortcuts, 24411424

### 2) Text Colors
1) Copy and paste the files into an add-on. In Anki go to `Tools → Add-ons → Select "editor: paste raw unfiltered full html" add-on → View Files → Open "__init__.py" → paste the code below`. 
Or when you are in the folder replace `__init__.py` with the one on this repository.

### 3) Different Shortcuts for Flags:
You cannot use the aforementioned "Text Colors" if you do not change the flags shorcuts.
1) Go to `Tools → Add-ons → Select "Customize Keyboard Shortcuts" add-on → Config → Copy and paste the config file` or `change each flag to Alt+(the number you want)` .

### Example:
"flag1": "Alt+1", <br>
"flag2": "Alt+2", <br>
"flag3": "Alt+3", <br>
"flag4": "Alt+4"

### 4) Optional - remap shortcut of the clean paste:
If you want to change the shorcut of the paste without filter from `Ctrl+Alt+v` to `Ctrl+Shift+z` or wichiever you want.
Go to `Tools → Add-ons → Select "Customize Keyboard Shortcuts" add-on → Config → and change "full html shortcut": "Ctrl+Alt+z" to your liking`

### 5) Close and open anki.


