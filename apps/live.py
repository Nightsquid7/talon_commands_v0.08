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
    "save it": [Key("cmd-s")],
    "save as": [Key("cmd-shift-s")],
    "duplicate": [Key("cmd-d")],
    "browser": [Key("cmd-alt-b")],
    "preferences": [Key("cmd-,")],
    "rename": [Key("cmd-r")],
    "device view": [Key("cmd-alt-l")],
    "device window": [Key("cmd-alt-p")],
    "(hi | show) video": [Key("cmd-alt-v")],
    "lp | loup": [Key("cmd-l")],
    "(plug in) | third party": lambda m: focusCategories(3),
    "max devices": lambda m: focusCategories(4),
    "many effects": lambda m: focusCategories(5),
    "audio effects": lambda m: focusCategories(6),
    "live devices": lambda m: focusCategories(7), 

    "search": [Key("cmd-f")],
    "(show | hide) (sentence | seds)": [Key("cmd-alt-r")],
    "(show | hide) (devices | midi)": [Key("cmd-alt-l")],
    "sound toys": [Key("cmd-f"), "Soundtoys"],
    "native instruments": [Key("cmd-f"), "Native Instruments"],
    "fab filter": [Key("cmd-f"), "Fabfilter"],
    "oratorio | arterial": [Key("cmd-f"), "Arturia"],
    "valhalla": [Key("cmd-f"), "Valhalla"],
    "open contact": [Key("cmd-f"), 
                     "Kontakt"],
}

ctx.keymap(keymap)