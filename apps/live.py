from talon.voice import Key, press, Str, Context
from ..misc.mouse import command_click, press_key_and_click

ctx = Context("live", bundle="com.ableton.live")

keymap = {
    "browser": [Key("cmd-alt-b")],
}

ctx.keymap(keymap)