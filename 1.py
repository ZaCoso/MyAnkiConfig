# ---------- CUSTOM COLOR SHORTCUTS ----------

from aqt.editor import Editor

def set_color(editor, color, make_bold=False):
    if make_bold:
        editor.web.eval('document.execCommand("bold", false, null);')
    editor.web.eval(f'document.execCommand("foreColor", false, "{color}");')

def color_1(editor):
    set_color(editor, "#ffaa00", True)  # naranja + bold

def color_2(editor):
    set_color(editor, "#65cb96", True)  # verde + bold

def color_3(editor):
    set_color(editor, "#ff0000", True)  # rojo + bold

def color_4(editor):
    set_color(editor, "#ffffff", False)  # blanco sin bold

def setup_color_shortcuts(cuts, editor):
    cuts.append(("Ctrl+1", lambda e=editor: color_1(e)))
    cuts.append(("Ctrl+2", lambda e=editor: color_2(e)))
    cuts.append(("Ctrl+3", lambda e=editor: color_3(e)))
    cuts.append(("Ctrl+4", lambda e=editor: color_4(e)))
    return cuts

addHook("setupEditorShortcuts", setup_color_shortcuts)
