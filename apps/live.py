from talon.voice import Key, press, Str, Context
from ..misc.mouse import command_click, press_key_and_click

import time


ctx = Context("live", bundle="com.ableton.live")

def focusCategories(upCount):
    press("cmd-f")
    time.sleep(0.1)
    press("escape")
    time.sleep(0.1)
    press("left") 
    for x in range(upCount):
      press("up") 
    
    press("right")
        

keymap = {
    "browser": [Key("cmd-alt-b")],
    "(click | clip) view": [Key("cmd-alt-l")],
    "(plug in) | third party": lambda m: focusCategories(3),
    "live devices": lambda m: focusCategories(4),
    "many effects": lambda m: focusCategories(5),
    "audio effects": lambda m: focusCategories(6),
    "instruments": lambda m: focusCategories(7), 
    "search": [Key("cmd-f")],
    
}

ctx.keymap(keymap)