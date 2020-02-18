from talon.voice import Context, Key

ctx = Context("symbol")

keymap = {
    # simple
    "(question [mark] | questo)": "?",
    "plus": "+",
    "tilde": "~",
    "(bang | exclamation point | clamor)": "!",
    "(dollar [sign] | dolly)": "$",
    "(downscore)": "_",
    "colon": ":",
    "(lparen | [left] paren | precorp )": "(", 
    "(rparen | are paren | right paren )": ")",
    "(brace | left brace | kirksorp)": "{",
    "(rbrace | are brace | right brace )": "}",
    "(angle | left angle | less than)": "<",
    "(rangle | are angle | right angle | greater than)": ">",
    "(star | asterisk)": "*",
    "hash [sign]": "#",
    "percent [sign]": "%",
    "caret": "^",
    "at sign": "@",
    "(and sign | ampersand | amper)": "&",
    "(pipe | spike)": "|",
    "(dubquote | double quote | dubber)": '"',
   
    # compound
    "mintwice": "--",
    "plustwice": "++",
    "minquall": "-=",
    "pluqual": "+=",
    "starqual": "*=",
    "triple quote": "'''",
    "triple tick": "```",
    "[forward] dubslash": "//",
    "coal twice": "::",
    "(dot dot | dotdot)": "..",
    "(ellipsis | dot dot dot | dotdotdot)": "...",
    # unnecessary: use repetition commands?
    # Custom Symbols
    "spash": " - ", 
    "all files": " */* ",
}

ctx.keymap(keymap)
