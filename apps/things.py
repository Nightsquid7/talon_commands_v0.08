from talon.voice import Key, press, Str, Context

ctx = Context("things", bundle="com.culturedcode.ThingsMac")

keymap = {
    # complete a todo
    "complete": Key("cmd-."),
    # jump to next project
    "( (p | pick | picked) up) | pageup": Key("ctrl-alt-cmd-up"),
    "( (p | pick | picked) down) | pagedown": Key("ctrl-alt-cmd-down"),
    "new project": Key("cmd-alt-n"),
    "new to do": Key("cmd-n"),
    "new header": Key("shift-cmd-n"),
    "next header": [Key("shift-cmd-n"), "Next", Key("enter")],
    "make list": [Key("enter"), Key("shift-cmd-c")],
    "search": Key("cmd-f"),
    "clear date": [Key("cmd-r")],
    "(enter | edit) date": [Key("cmd-s")],
}

ctx.keymap(keymap)