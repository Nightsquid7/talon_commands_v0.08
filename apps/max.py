from talon.voice import Key, press, Str, Context
from ..misc.mouse import command_click, press_key_and_click

ctx = Context("max", bundle="com.cycling74.Max")

keymap = {
    
    "print": ["n", "print"],
    "trigger event list": ["n", "t b l"],
    "(locket | locket it) | (unlock it)": [command_click],
    "inspect": [lambda m: press_key_and_click(m, "alt", 1, 1)],
    "copy from keyboard | click4": [Key("alt-cmd-n")],
}

ctx.keymap(keymap)