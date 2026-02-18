"""
License: GNU AGPLv3 or later <https://www.gnu.org/licenses/agpl.html>
Copyright: 2020- ijgnd
"""

import os
import re  # <-- added for style cleanup

from anki.hooks import wrap, addHook
from anki.utils import stripHTMLMedia

from aqt import mw
from aqt.editor import Editor
from aqt.qt import (
    QClipboard,
    QKeySequence,
)
from aqt.utils import tooltip

from .anki_version_detection import anki_point_version


addon_path = os.path.dirname(__file__)
unique_string = 'äöüäöüzuio'


def gc(arg, fail=False):
    conf = mw.addonManager.getConfig(__name__)
    if conf:
        return conf.get(arg, fail)
    return fail


def __unfilteredPaste(self, html, field):
    f = self.note.fields
    before, after = f[field].split(unique_string)
    f[field] = before + html + after
    if not self.addMode:
        self.note.flush()
    self.loadNote(focusTo=field)


def _unfilteredPaste(self, html, field):
    self.saveNow(lambda s=self, h=html, f=field: __unfilteredPaste(s, h, f))


def clean_html_preserve_colors(html):
    """
    Remove background styles introduced by dark mode or web sources
    while preserving text color and other formatting.
    """

    # Remove background-color
    html = re.sub(r'background-color\s*:\s*[^;"]+;?', '', html, flags=re.IGNORECASE)

    # Remove shorthand background property
    html = re.sub(r'background\s*:\s*[^;"]+;?', '', html, flags=re.IGNORECASE)

    # Remove Qt-injected dark mode attributes
    html = re.sub(r'-qt-background-role\s*:\s*[^;"]+;?', '', html, flags=re.IGNORECASE)
    html = re.sub(r'-qt-block-indent\s*:\s*[^;"]+;?', '', html, flags=re.IGNORECASE)

    # Clean empty style="" left behind
    html = re.sub(r'style="\s*"', '', html, flags=re.IGNORECASE)

    return html


def unfilteredPaste(self):
    focused_field_no = self.currentField
    if not isinstance(focused_field_no, int):
        tooltip("Aborting. No field focused. Try using shortcuts.")
        return

    if anki_point_version <= 49:
        mode = QClipboard.Clipboard
    else:
        mode = QClipboard.Mode.Clipboard

    mime = self.mw.app.clipboard().mimeData(mode=mode)
    html, _ = self.web._processMime(mime)

    if not html:
        return

    # --- KEY FIX ---
    html = clean_html_preserve_colors(html)

    jscode = f"""setFormat("insertText", "{unique_string}");"""
    self.web.evalWithCallback(
        jscode,
        lambda _, s=self, h=html, f=focused_field_no: _unfilteredPaste(s, h, f)
    )


def keystr(k):
    key = QKeySequence(k)
    return key.toString(QKeySequence.SequenceFormat.NativeText)


def maybe_extend_context_Menu(ewv, menu):
    e = ewv.editor
    if gc("context_menu_entry", False):
        a = menu.addAction("Paste full html ({})".format(keystr(gc("full html shortcut", ""))))
        a.triggered.connect(lambda _, ed=e: unfilteredPaste(ed))


addHook('EditorWebView.contextMenuEvent', maybe_extend_context_Menu)


def maybe_add_button(buttons, editor):
    if gc("show button"):
        b = editor.addButton(
            os.path.join(addon_path, "Octicons-diff-ignored.svg"),
            "paste_unfiltered_button",
            lambda e=editor: unfilteredPaste(e),
            tip="Paste unfiltered/full html ({})".format(keystr(gc("full html shortcut", ""))),
            keys=gc("full html shortcut", "")
        )
        buttons.extend([b])
    return buttons


addHook("setupEditorButtons", maybe_add_button)


def maybe_add_shortcut(cuts, editor):
    if not gc("show button"):
        fh = gc("full html shortcut")
        if fh:
            cuts.append((fh, lambda e=editor: unfilteredPaste(e)))


addHook("setupEditorShortcuts", maybe_add_shortcut)
