"""
Commands that write bits of code that is valid for multiple languages
"""

from talon.voice import Context, Key

ctx = Context("general_lang")

ctx.keymap(
    {
        # Operators
        "(op equals)": " = ",
        "(op (minus | subtract))": " - ",
        "(op (plus | add))": " + ",
        "(op (times | multiply))": " * ",
        "(op divide)": " / ",
        "op mod": " % ",
        "((op minus | subtract) equals)": " -= ",
        "((op plus | add) equals | (plus | add) assign)": " += ",
        "([op] (times | multiply) (assign | equals) | star assign)": " *= ",
        "[op] divide (assign | equals)": " /= ",
        "[op] mod (assign | equals)": " %= ",
        "(op colon (equals | assign))": " := ",
        "(op | is) greater [than]": " > ",
        "(op | is) less [than]": " < ",
        "((op | is) equal [to])": " == ",
        "((op | is) not equal [to])": " != ",
        "((op | is) greater [than] or equal [to])": " >= ",
        "((op | is) less [than] or equal [to])": " <= ",
        "([(op | is)] exactly (equal [to] | equals))": " === ",
        "([(op | is)] not exactly (equal [to] | equals))": " !== ",
        "(op (power | exponent) | to the power [of])": " ** ",
        "op and": " && ",
        "op or": " || ",
        "[op] (logical | bitwise) and": " & ",
        "([op] (logical | bitwise) or | (op | D) pipe)": " | ",
        "[(op | logical | bitwise)] (ex | exclusive) or": " ^ ",
        "(op | logical | bitwise) (left shift | shift left)": " << ",
        "(op | logical | bitwise) (right shift | shift right)": " >> ",
        "(op | logical | bitwise) and equals": " &= ",
        "(op | logical | bitwise) or equals": " |= ",
        "(op | logical | bitwise) (ex | exclusive) or equals": " ^= ",
        "[(op | logical | bitwise)] (left shift | shift left) equals": " <<= ",
        "[(op | logical | bitwise)] (right shift | shift right) equals": " >>= ",
        "[op] (arrow | lambo)": " -> ",
        "[op] fat (arrow | lambo)": " => ",
        # Completed matchables
        "(empty parens | call | prexy)": "()",
        "empty (dict | object)": "{}",
        "(empty array | brackers)": "[]",
        # Blocks
        #"brace block": [" {}", Key("left enter enter up tab")],
        #"[brace] shocker block": [Key("cmd-right enter"), "{}", Key("enter up right enter tab")],
        # "(square | brax) block": ["[", Key("enter")],
        #"(paren | prex) block": ["(", Key("enter")],
        
        # Combos
        "coalshock": [":", Key("enter")],
        "comshock": [",", Key("enter")],
        #   "sinker": [Key("cmd-right ;")],
        "swipe": ", ",
        "coalgap": ": ",
        "[forward] slasher": "// ",
        # Statements
        "state (def | deaf | deft)": "def ",
        "state if": ["if ()", Key("left")],
        "state else if": [" else if ()", Key("left")],
        "state while": ["while ()", Key("left")],
        "state for": ["for ()", Key("left")],
        "state switch": ["switch ()", Key("left")],
        #"state case": ["case \nbreak;", Key("up")],
        # Swift
        
        "state let": "let ",
        "state if let": "if let ",

        # Other Keywords
        "const": "const ",
        #"static": "static ",
        "tip pent": "Int ",
        "tip pool": "Bool ",
        "tip (char | care)": "char ",
        "tip byte": "byte ",
        "tip float": "float ",
        "tip double": "Double ",
        "tip string": "String",
        "miller": "nil",
        "cd float": "CGFloat ",
        "cd point": ["CGPoint(x: , y:)", Key("alt-left"), Key("left"), Key("left")],
        "ui image": "UIImage(",
        "as string any": " as? [String: Any]",

        # Comments
        "comment see": "// ",
        "comment py": "# ",
        
        # custom
        "get checkmark": "- [ ] ",

        # JS
        "a single function": "async function",
        "js print": ["console.log()", Key("left")],

        # Go
        "go print": "fmt.Print",


        #random/temp
        "superscript" : [Key("ctrl-cmd-+")]

    }
)
