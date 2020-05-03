from talon.voice import Key, press, Str, Context
from ..misc.mouse import command_click

ctx = Context("max", bundle="com.cycling74.Max")

keymap = {
    "object": "n",
    "(locket | locket it) | (unlock it)": [command_click],
}

ctx.keymap(keymap)