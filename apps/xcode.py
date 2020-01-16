# Talon voice commands for Xcode
# John S. Cooper  jcooper@korgrd.com

from talon.voice import Key, Context
from ..misc.mouse import control_shift_click

ctx = Context("xcode", bundle="com.apple.dt.Xcode")

ctx.keymap(
    {
        "build it": Key("cmd-b"),
        "stop it": Key("cmd-."),
        "run it": Key("cmd-r"),
        "run playground": Key("shift-cmd-enter"),
        "go back": Key("cmd-ctrl-left"),
        "go (fore | forward)": Key("cmd-ctrl-right"),
        "find in (proj | project)": Key("cmd-shift-f"),
        "(sell find in (proj | project) | find selection in project)": Key("cmd-e cmd-shift-f enter"),
        "(sell find ace in (proj | project) | replace selection in project)": Key("cmd-e cmd-shift-alt-f"),
        "next in (proj | project)": Key("cmd-ctrl-g"),
        "prev in (proj | project)": Key("shift-cmd-ctrl-g"),
        "split window": Key("cmd-alt-enter"),
        "show editor": Key("cmd-enter"),
        "(show | hide) debug": Key("cmd-shift-y"),
        "(show | find) call hierarchy": Key("cmd-ctrl-shift-h"),
        "show (recent | recent files)": [Key("ctrl-1"), "recent files\n"],
        "show related": Key("ctrl-1"),
        "show history": Key("ctrl-2"),
        "show files": Key("ctrl-5"),
        "show (methods | items)": Key("ctrl-6"),
        "show navigator": Key("cmd-0"),
        "hide (navigator | project | warnings | breakpoints | reports | build)": Key("cmd-0"),
        "show project": Key("cmd-1"),
        "show warnings": Key("cmd-5"),
        "show breakpoints": Key("cmd-8"),
        "show (reports | build)": Key("cmd-9"),
        "show diffs": Key("cmd-alt-shift-enter"),
        "(next counterpart | show header | switcher)": Key("cmd-ctrl-down"),
        "prev counterpart": Key("cmd-ctrl-up"),
        "toggle comment": Key("cmd-/"),
        "toggle breakpoint": Key("cmd-\\"),
        "toggle all breakpoints": Key("cmd-y"),
        "go to line": Key("cmd-l"),
        "line end": [Key("down"), Key("up"),Key("cmd-right")],
        "editor": [Key("cmd-j"),Key("enter")],

        "move line up": Key("cmd-alt-["),
        "move line down": Key("cmd-alt-]"),

        "go (deafen | definition)": Key("cmd-ctrl-j"),
        "edit scheme": Key("cmd-shift-,"),
        "quick open": Key("cmd-shift-o"),
        "comm skoosh": "// ",
        # mycommands



        # editor
        "comment line": Key("cmd-/"),
        "print": ["print()", Key("left")],
        "print string": ["\()", Key("left")],
        "print copy": ["print(\"\\(", Key("cmd-v"),")"],
        "complete paren": ["(", Key("escape")],
        "state function": "func ",
        "state in it": "init()",
        "guard let": "guard let ",

        
        "step in": Key("f7"),
        "step over": Key("f6"),
        "step out": Key("f8"),
        "step (continue | go)": Key("ctrl-cmd-y"),
        "show blame for line": Key("cmd-alt-ctrl-b"),
        "(reveal file | show file in finder)": Key("cmd-alt-ctrl-shift-f"),
        "(snipline | delete line)": Key("cmd-alt-ctrl-shift-backspace"),
        "add cursor down": Key("ctrl-shift-down"),
        "add cursor up": Key("ctrl-shift-up"),
        "add cursor": control_shift_click,
        "dub add cursor": lambda m: control_shift_click(m, 0, 2),
        "((select | sell) (partial | sub) [word] left)": Key("shift-ctrl-left"),
        "((select | sell) (partial | sub) [word] right)": Key("shift-ctrl-right"),
        # the following require custom key bindings in xcode preferences
        "((partial | sub) [word] left | wonkrim)": Key("alt-ctrl-left"),
        "((partial | sub) [word] right | wonkrish)": Key("alt-ctrl-right"),

        # import statements
        "import audiokit":  "import AudioKit",
        "import combined": "import Combine",
        "import scene kit": "import SceneKit",
        "import spray kit": "import SpriteKit",
        "import gameplayc": "important GameplayKit",

        # General swift?
        ".annette": ".init(",
        "wrecked": "rect",

        # scene kit
        "SK shape node": "SKShapeNode",

        # AudioKit
        "midi note number": "MIDINoteNumber",
        # SwiftUI/Combine
        "variable": "var ",
        "geometry reader": "GeometryReader { g in \n\n",
        "state variable": "@State var ",
        "binding variable": "@Binding var ",
        "environment variable": "@EnvironmentObject var",
        "published variable": "@Published var",
        ".sync": ".sink(",
        ".sync full": [".sink(",Key("enter"),Key("tab"),"receiveCompletion: ",
                Key("enter"),Key("tab"),"receiveValue: ",Key("up"),Key("cmd-right"),Key("right")],
        ".store": ".store(in: &disposables)",
        "print sync in store": ".sink(receiveValue: { print($0) })\n.store(in: &subscriptions)",
        "pass through subject": "PassthroughSubject<",
        "refresh preview": Key("cmd-alt-p"),
        "swift (4 e | 4 each | 4e)": ".forEach",
        # Containers
        "for e | 4e": ["ForEach(, id: \.self) { _ in ",Key("enter")],
        "horizontal stack": ["HStack {}", Key("left")],
        "vertical stack": ["VStack {}", Key("left")],
        "spacer": ["Spacer()", Key("cmd-left"), Key("tab")],
        "make button": ["""Button(action:  {


                }, label:  {
                    Text("")

                 """]

    }
)
