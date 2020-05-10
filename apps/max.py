from talon.voice import Key, press, Str, Context
from ..misc.mouse import command_click, press_key_and_click

ctx = Context("max", bundle="com.cycling74.Max")

keymap = {
    "new object": "n",
    "jitter object": ["n", "jit"],
    "print object": ["n", "print"],
    "new message": "m",
    "(locket | locket it) | (unlock it)": [command_click],
    "inspect": [lambda m: press_key_and_click(m, "alt", 1, 1)],
}

ctx.keymap(keymap)