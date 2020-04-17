from talon.voice import Key, press, Str, Context

ctx = Context("things", bundle="com.culturedcode.ThingsMac")

keymap = {
    # complete a todo
    "complete": Key("cmd-."),
    # jump to next project
    "( (p | pick | picked) up) | pageup": Key("ctrl-alt-cmd-up"),
    "( (p | pick | picked) down) | pagedown": Key("ctrl-alt-cmd-down"),
    "new project": Key("cmd-alt-n"),
    "search": Key("cmd-f"),
}

ctx.keymap(keymap)