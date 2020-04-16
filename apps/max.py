from talon.voice import Key, press, Str, Context

ctx = Context("max", bundle="com.cycling74.Max")

keymap = {
    "object": "n",
}

ctx.keymap(keymap)