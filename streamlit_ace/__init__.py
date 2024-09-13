import streamlit as st

from pathlib import Path
from streamlit.components.v1.components import declare_component
from streamlit_ace.version import __release__, __version__

if __release__:
    _source = {"path": (Path(__file__).parent/"frontend"/"build").resolve()}
else:
    _source = {"url": "http://localhost:3001"}

_render_component = declare_component("streamlit_ace", **_source)

# Source: https://github.com/ajaxorg/ace-builds/tree/master/src/mode-*.js
LANGUAGES = [ 
    "c_cpp" , "clojure" , "csharp", "css", "django", "dockerfile", "gitignore" , "golang" , "haml" , 
    "html" , "ini" , "io", "java" , "javascript" , "json" , "jsx" , "kotlin" , "latex" , "matlab" ,  
    "mysql", "objectivec" , "pascal" , "perl", "php" , "powershell" , "prisma" , "prolog" , 
    "python" , "qml" , "r" , "ruby" , "rust" , "scala" , "sjs" , "snippets" ,  "sql" , "sqlserver" , "svg" , "swift" ,  
    "terraform", "tex", "text", "textile", "toml", "tsx", "turtle", "twig", "typescript", "vala", "vbscript", 
    "xml" ,  "yaml"
]

# Source: https://github.com/ajaxorg/ace-builds/tree/master/src/theme-*.js
THEMES = [
    "twilight", "vibrant_ink", "xcode"
]

# Source: https://github.com/ajaxorg/ace-builds/tree/master/src/keybinding-*.js
KEYBINDINGS = [
    "emacs", "sublime", "vim", "vscode"
]


def st_ace(
    value="",
    placeholder="",
    height=None,
    language="plain_text",
    theme="twilight",
    keybinding="vscode",
    min_lines=12,
    max_lines=None,
    font_size=14,
    tab_size=4,
    wrap=False,
    show_gutter=True,
    show_print_margin=False,
    readonly=False,
    annotations=None,
    markers=None,
    auto_update=False,
    key=None
):
    """Display an Ace editor.

    Parameters
    ----------
    value : any
        The text value of this widget when it first renders.
        Empty string by default.
    placeholder : any
        The text value of this widget when the editor is empty.
        Empty string by default.
    height : int or None
        Desired height of the UI element expressed in pixels.
        If set to None, height will auto adjust to editor's content.
        None by default.
    language : str or None
        Language for parsing and code highlighting. If None, the editor
        will not highlight content.
        Available languages are defined in streamlit_ace.LANGUAGES.
        Plain text by default.
    theme : str or None
        The theme to use. If None, a default theme is used.
        Available themes are defined in streamlit_ace.THEMES.
        Chrome by default.
    keybinding : str
        Keybinding mode set.
        Available keybindings are defined in streamlit_ace.KEYBINDINGS.
        Vscode by default.
    min_lines : int or None
        Minimum number of lines allowed in editor. 12 by default.
    max_lines : int or None
        Maximum number of lines allowed in editor. None by default.
    font_size : int or None
        The font size of the enditor. 14 by default.
    tab_size : int or None
        The size of a tabulation. 4 by default.
    show_gutter : bool
        Show or hide gutter. True by default.
    show_print_margin : bool
        Show or hide print margin. False by default
    wrap : bool
        Enable line wrapping. False by default.
    readonly : bool
        Make the editor read only. False by default.
    annotations : list or None
        Anootations to show in the editor. None by default.
    markers : list or None
        Markers to show in the editor. None by default.
    auto_update : bool
        Choose whether Streamlit auto updates on input change, or waits
        for user validation. False by default.
    key : str
        An optional string to use as the unique key for the widget.
        If this is omitted, a key will be generated for the widget
        based on its content. Multiple widgets of the same type may
        not share the same key.
    
    Returns
    -------
    str
        The current content of the ace editor widget.
    """
    return _render_component(
        defaultValue=str(value),
        placeholder=str(placeholder),
        height=height,
        minLines=min_lines,
        maxLines=max_lines,
        fontSize=font_size,
        tabSize=tab_size,
        mode=language,
        theme=theme,
        showGutter=show_gutter,
        showPrintMargin=show_print_margin,
        wrapEnabled=wrap,
        readOnly=readonly,
        keyboardHandler=keybinding,
        annotations=annotations or [],
        markers=markers or [],
        autoUpdate=auto_update,
        key=key,
        default=str(value),
    )
