from talon.voice import Key, press, Str, Context

# Commands for annotating pdfs.

ctx = Context("preview", bundle="com.apple.Preview")

keymap = {
    "(picked | pick | p) down": [Key("down")] * 3,
    "(picked | pick | p) up": [Key("up")] * 3,
    "bookmark page": Key("cmd-d"),
    "show bookmarks": Key("alt-cmd-5"),
    "hide (sidebar | bookmarks)": Key("alt-cmd-1"),
    "table of contents": Key("alt-cmd-3"),
    "highlight": Key("cmd-ctrl-h"),
    "open recent": [Key("ctrl-1"), 
                        Key("right"),
                        Key("down"),
                        Key("down"),               
                        Key("right")],
}

ctx.keymap(keymap)
