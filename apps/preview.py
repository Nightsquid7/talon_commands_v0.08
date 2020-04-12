from talon.voice import Key, press, Str, Context

# Commands for annotating pdfs.

ctx = Context("preview", bundle="com.apple.Preview")

keymap = {
    "(picked | pick | p) down": [Key("down")] * 3,
    "(picked | pick | p) up": [Key("up")] * 3,
    "highlight": Key("cmd-ctrl-h"), "note": Key("cmd-ctrl-n")
}

ctx.keymap(keymap)
