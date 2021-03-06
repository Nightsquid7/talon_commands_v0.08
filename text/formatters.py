from talon.voice import Word, Context, press
from talon import clip

from ..utils import (
    insert,
    normalise_keys,
    parse_word,
    surround,
    text,
    sentence_text,
    word,
    parse_words,
    spoken_text,
)


def title_case_capitalize_word(index, word, _):
    words_to_keep_lowercase = "a,an,the,at,by,for,in,of,on,to,up,and,as,but,or,nor".split(
        ","
    )
    if index == 0 or word not in words_to_keep_lowercase:
        return word.capitalize()
    else:
        return word


formatters = normalise_keys(
    {
        "camel": (
            True,
            lambda i, word, _: word if i == 0 else word.capitalize(),
        ),
        "yellsmash": (True, lambda i, word, _: word.upper()),
        "yeller": (False, lambda i, word, _: word.upper()),
        "(criff | criffed)": (True, lambda i, word, _: word.capitalize()),
        "snake": (True, lambda i, word, _: word if i == 0 else "_" + word),
        "dot": (True, lambda i, word, _: "." + word if i == 0 else word.capitalize()),
        "smash": (True, lambda i, word, _: word),
        "spine": (True, lambda i, word, _: word if i == 0 else "-" + word),
        "turtle": (False, title_case_capitalize_word),
    }
)

surrounders = normalise_keys(
    {
        "dubstring": (False, surround('"')),
        "angler": (False, surround("<", ">")),
        "brax": (False, surround("[", "]")),
        "kirk": (False, surround("{", "}")),
        "precoif": (False, surround('("', '")')),
        "(prex)": (False, surround("(", ")")),
    }
)

formatters.update(surrounders)


def FormatText(m):
    fmt = []

    for w in m._words:
        if isinstance(w, Word) and w != "over":
            fmt.append(w.word)
    words = parse_words(m)
    if not words:
        try:
            with clip.capture() as s:
                press("cmd-c")
            words = s.get().split(" ")
        except clip.NoChange:
            words = [""]

    tmp = []

    smash = False
    for i, w in enumerate(words):
        word = parse_word(w, True)
        for name in reversed(fmt):
            smash, func = formatters[name]
            word = func(i, word, i == len(words) - 1)
        tmp.append(word)

    sep = "" if smash else " "
    insert(sep.join(tmp))
    # if no words, move cursor inside surrounders
    if not words[0]:
        for i in range(len(tmp[0]) // 2):
            press("left")


ctx = Context("formatters")

ctx.keymap(
    {
        "(phrase | say) <dgndictation> [over]": text,
        "sentence <dgndictation> [over]": sentence_text,
        "(comma | ,) <dgndictation> [over]": [", ", spoken_text],
        "period <dgndictation> [over]": [". ", sentence_text],
        "word <dgnwords>": word,
        "(%s)+ [<dgndictation>] [over]" % (" | ".join(formatters)): FormatText,
        # to match surrounder command + another command (i.e. not dgndictation)
        "(%s)+" % (" | ".join(surrounders)): FormatText,
    }
)
