from talon.voice import Key, press, Str, Context

ctx = Context("things", bundle="com.culturedcode.ThingsMac")

keymap = {
    "complete": Key("cmd-."),
    "( (p | pick | picked) up) | pageup": Key("ctrl-alt-cmd-up"),
    "( (p | pick | picked) down) | pagedown": Key("ctrl-alt-cmd-down"),
    "search": Key("cmd-f"),
}

ctx.keymap(keymap)