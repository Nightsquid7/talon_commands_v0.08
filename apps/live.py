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

def pressMultiple(key,times):
    for x in range(times):
      press(key)

     

keymap = {
    "save it": [Key("cmd-s")],
    "save as": [Key("cmd-shift-s")],
    "duplicate": [Key("cmd-d")],
    "browser": [Key("cmd-alt-b")],
    "open preferences": [Key("cmd-,")],
    "rename": [Key("cmd-r")],
    "export trap": [Key("shift-cmd-r")],
    "midi window | view": [Key("cmd-alt-l")],
    "device window": [Key("cmd-alt-p")],
    "(hi | show) video": [Key("cmd-alt-v")],
    "lp | loup": [Key("cmd-l")],

    "makemidit": [Key("shift-cmd-t")],
    "make audiot": [Key("cmd-t")],
    "make many region": [Key("shift-cmd-m")],
    
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
    # Open instruments
    # Audreio
    "open (alter ego) | allj": [Key("cmd-f"), 
                       "audreio",
                       Key("down")],
    "open reactor": [Key("cmd-f"), 
                     "Reaktor",
                     Key("down"),
                     ],
    "open contact": [Key("cmd-f"), 
                     "Kontakt",
                     lambda m: pressMultiple("down", 1)],
}

ctx.keymap(keymap)