import time

from talon.voice import Key, Context, Str, press
from talon_init import TALON_HOME, TALON_PLUGINS, TALON_USER
from talon import ctrl, ui

from ..utils import parse_words, text, is_in_bundles, insert
from .. import config
from ..misc.switcher import switch_app
from ..bundle_groups import TERMINAL_BUNDLES

# TODO: move application specific commands into their own files: apt-get, etc

ctx = Context("terminal", func=is_in_bundles(TERMINAL_BUNDLES))

mapping = {"semicolon": ";", r"new-line": "\n", r"new-paragraph": "\n\n"}


def parse_word(word):
    word = word.lstrip("\\").split("\\", 1)[0]
    word = mapping.get(word, word)
    return word


def dash(m):
    words = parse_words(m)
    press(" ")
    if len(words) == 1 and len(words[0]) == 1:
        press("-")
        Str(words[0])(None)
    else:
        if words == ["michelle"]:
            words = ["shell"]
        press("-")
        press("-")
        Str("-".join(words))(None)


KUBERNETES_PREFIX = "(cube | cube control)"

directory_shortcuts = {
    "up": "..",
    "up up": "../..",
    "up up up": "../../..",
    "up up up up": "../../../..",
    "up up up up up": "../../../../..",
    "home": "~",
    "temp": "/tmp",
    "talon home": TALON_HOME,
    "talon user": TALON_USER,
    "talon plug-ins": TALON_PLUGINS,
    "talon community": "~/.talon/user/talon_community",
}
directory_shortcuts.update(config.load_config_json("directory_shortcuts.json"))


def cd_directory_shortcut(m):
    directory = directory_shortcuts[m[1]]
    insert(f"cd {directory}; ls")
    for _ in range(4):
        press("left")
    press("enter")


def name_directory_shortcuts(m):
    insert(directory_shortcuts[" ".join(m["terminal.directory_shortcuts"])])


servers = config.load_config_json("servers.json")


def get_server(m):
    return servers[" ".join(m["global_terminal.servers"])]


def mosh_servers(m):
    insert(f"mosh {get_server(m)}")


def ssh_servers(m):
    insert(f"ssh {get_server(m)}")


def name_servers(m):
    insert(get_server(m))


def ssh_copy_id_servers(m):
    insert(f"ssh-copy-id {get_server(m)}")


def new_server(m):
    press("cmd-d")
    insert(f"ssh {get_server(m)}")
    press("enter")


keymap = {
    # Personal keys 
    # Navigation
    # # Folders
    "nightsquid folder": ["cd /Users/stevenberkowitz/Development/Nightsquid\ Personal\ Projects/; ls", Key("enter")],
    "fsu folder": ["fsu", Key("enter")],
    "midi visualizer folder": ["cd /Users/stevenberkowitz/Development/Nightsquid\ Personal\ Projects/music_projects/MIDI\ Visualizers",Key("enter")],
    "midi folder": ["cd /Users/stevenberkowitz/Documents/Music\/MIDI; ls", Key("enter")],
    "scripting folder": ["cd /Users/stevenberkowitz/Development/scripting/; ls",Key("enter")],
    
    "zeppelin music": ['cd /Users/stevenberkowitz/Documents/Music/Zeppelin/ARaddin; ll', Key("enter")],
    "audio hijack folder": ['cd /Users/stevenberkowitz/Music/Audio\ Hijack; ls', Key("enter")],
    # Utility
    "print working directory string": ["printf \"%q\\n\" \"$(pwd)\"",Key("enter")],
    "finder": ["open -a finder .", Key("enter")],
    "new terminal window": 
    [Key("ctrl-1"),Key("right"), Key("right"), Key("down"),Key("down"),Key("right"),Key("down"),Key("down"),Key("down")],
    "new terminal tab": [Key("ctrl-1"),Key("right"), Key("right"), Key("down"), Key("down"),Key("down"),Key("right"),Key("down"),Key("down")],
    "code": "code ",
    "node": "node ",
    "osc": ["osc", Key("enter")],

    "remove checkmarks": ["remcheck", Key("enter")],  
    "af convert": ["afconvert -f m4af -d aac -b 256000 "],
    "afterplay | af play": "afplay -d ",
    "shell (substitute | sub | sup)": ["$()", Key("left")],
    "(substitute | sub) last": "$(lst)",
    "HAD": "HEAD",

    "yes": ["y", Key("enter")],
    "no": ["n", Key("enter")], 
    # open apps/files
    "open shell commands": ["zshrc", Key("enter")],
    "(reload | run) shell commands": ["runz", Key("enter")],
    "openswiftlint": ["code .swiftlint.yml", Key("enter")],
    "(open apco man's | open app commands)": [ "code /Users/stevenberkowitz/.talon/user/talon_community/apps/"],
    "open general commands": ["code /Users/stevenberkowitz/.talon/user/talon_community/lang/general.py", Key("enter")],
    "open terminal commands": ["code /Users/stevenberkowitz/.talon/user/talon_community/apps/terminal.py", Key("enter")],
    "open xcode commands": ["code /Users/stevenberkowitz/.talon/user/talon_community/apps/xcode.py", Key("enter")],
    "open xcode project": ["open *proj", Key("enter")],
    "open things commands": ["code /Users/stevenberkowitz/.talon/user/talon_community/apps/things.py", Key("enter")],
    "open max commands": ["code /Users/stevenberkowitz/.talon/user/talon_community/apps/max.py", Key("enter")],
    "open live commands": ["code /Users/stevenberkowitz/.talon/user/talon_community/apps/live.py", Key("enter")],
    "open talon words": ["code /Users/stevenberkowitz/.talon/user/talon_community/misc/words.py", Key("enter")],
    #  AppleScripts
    "add chrome url to notes": ["osascript /Users/stevenberkowitz/Development/scripting/addChromeUrlToNotes.applescript", Key("enter")],
    "input sleep data": ["osascript /Users/stevenberkowitz/Development/scripting/inputSleepData.applescript", Key("enter")],
    "sleep data": ["sleepdata", Key("enter")],
    
    # Unix
    "shell find": "find . -name \"*",
    "shell alias": "alias ",
    "shell man": "man ",
    "shell top": ["top", Key("enter")],
    "shell touch": "touch ",
    "shell echo": "echo -n ",
    "shell echo last": ["echo $?", Key("enter")],
    "shell (asked if | sdiff)": "sdiff ",
    "shell tree": ["tree", Key("enter")],
    "shell (grep | grip)": "grep ",
    "shell gripper": ["grep -rn  .", Key("left left")],
    "shell open": "open ",
    "shell (pb | pv) copy ": "pbcopy ",
    "(shell | shall) (pb | pv) do it": "pbpaste ",
    "shell change mode": "chmod ",
    "shell said": ["sed \'s///\'", Key("alt-left"), Key("right"), Key("right")],
    "echo path": ["echo $PATH", Key("enter")],
    "(show | shell) off": ["awk '{}'", Key("left"), Key("left")],
    "shell app find": ["mdfind -name \"*\"", Key("left")],
    "shell tail": "tail -n ",
    "shell had": "head -n ",

            # combine
    "open combine book": "open /Users/stevenberkowitz/Documents/Developer/Learning\ Resources/Ray\ Wenderlich/Combine_Asynchronous_Programming_with_Swift_v1.0.2/*.pdf",
    "open combine project": ["open -a Xcode /Users/stevenberkowitz/Documents/Developer/Learning\ Resources/Ray\ Wenderlich/Combine_Asynchronous_Programming_with_Swift_v1.0.2/0"],
    "open combine folder": ["open -a Finder /Users/stevenberkowitz/Documents/Developer/Learning\ Resources/Ray\ Wenderlich/Combine_Asynchronous_Programming_with_Swift_v1.0.2", Key("enter")],
    
    # git
    "code get ignore": ["code .gitignore", Key("enter")],
    "get in8": ["git init", Key("enter")],
    "get pole | poll": "git pull ",
    "get fetch": "git fetch 5",
    "get push": "git push ",
    "git add": "git add ",
    "add you": ["git add -u", Key("enter"), "sta", Key("enter")],
    "add and commit": "git commit -am \"",
    "get show": "git show ",
    "glow": ["glo ", Key("enter")],
    "get roughl | get rest log": ["git reflog", Key("enter")],
    "git list files": ["git ls-files", Key("enter")],
    "git remove": "git rm ",
    "get reset": "git reset ",
    "sta": ["sta ", Key("enter")],
    "get commit": "git commit ",
    "commit message": "git commit -m \"",
    "git checkout": "git checkout ",
    "checkout new branch": "git checkout -b ",
    "git branch": "git branch ",
    "git branch all": ["git branch -a", Key("enter")], 
    "git diff": "git diff ",
    "get diff stage": ["git diff --staged", Key("enter")],
    "git rebase": "git rebase -i ",
    "get remote": "git remote ",
    "get - | gets- | gets- dash": "git stash ",
    "get march | merge": "git merge ",
    "get clone": "git clone ",
    
    
    

    # emacs
    "emacs safe": [Key("ctrl-x"), Key("ctrl-s")],
    "emacs quit": [Key("ctrl-x"), Key("ctrl-c")],
    "emacs undo": [Key("ctrl-x"), Key("u")],
    "emacs open": "emacs ",
    "emacs shock": [Key("ctrl-e"), Key("enter"), Key("tab")],
    "emacs kite": [Key("ctrl-a"), Key("ctrl-k"), Key("tab")],
    "emacs comment line": [Key("ctrl-a"), "//"],
    "emacs paste": Key("ctrl-y"),
    "emacs brace": ["{", Key("enter"), Key("enter"), "}", Key("up"), Key("tab")],
    "emacs closer": ");",
    "emacs brend": "];",
    "mark start": [Key("ctrl-space")],
    "mark end": Key("ctrl-w"),
    "save and run": [Key("ctrl-x"), Key("ctrl-s"), Key("cmd-`"), "run", Key("enter")],

    "emacs split window": [Key("ctrl-x"), "2"],
    # emacs - gdb
    "emacs execute": [Key("ctrl-c"), Key("ctrl-c")],
    "quick gdb": ["quit", Key("enter")],
    "ddb": ["gdb", Key("enter")],
    # for typing the continue in gdb
    "continue": ["continue", Key("enter"), Key("ctrl-c"), Key("ctrl-c")],
    "show breakpoints": ["i b ", Key("enter")],
    # emacs - xv6
    "quit xp6": [Key("ctrl-a"), "x"],

    # C Commands
    #"see print": ["printf();", Key("left"),Key("left")],
    "see print": ["printf(\"\\n\");", Key("left"),Key("left"),Key("left")],
    "see scan": ["sscanf(,)"],
    
    # fsu Comp Sci
    "fsu canvas": ["fsucanvas", Key("enter")],
    "ssh": ["ssh berkowit@linprog.cs.fsu.edu", Key("enter")],
    "open fsu tabs": "osascript /Users/stevenberkowitz/Development/Nightsquid\ Personal\ Projects/automation/openFSUTabsInChrome.applescript",
    
    # operating systems
    "obsess": ["cd /home/majors/berkowit/cop4610/proj4/xv6-public; ls", Key("enter")],
    "shell exit": ["exit", Key("enter")],
    "run (xp6 | xv6)": ["make qemu-nox ", Key("enter")],
    "(quick | quit) (xv6 | xp6)": [Key("ctrl-a"), Key("c"), "quit", Key("enter")],
    "make (clean | claim)": ["make clean", Key("enter")],
    "run gbd": ["", Key("enter")],


    # Programming Languages
    #"C make": ["g++ -std=c++11 -Wall -Wextra -o cparse.x cparse.cpp;", Key("enter"), Key("enter"),"./cparse.x ./proj3_official/extra1", Key("enter")], 
    "programming languages": ["progl", Key("enter")],
    "(built (yet | y)) | build yak": ["yacc -d cexpr.y", Key("enter")],
    "(build flex) | buildx": ["flex scan.l", Key("enter")],
    "build scanner": ["gcc lex.yy.c y.tab.c -o cexpr.exe -lfl -ggdb3", Key("enter")],
    "build all": [Key("enter"), Key("enter"), Key("enter"),
                  "yacc -d cexpr.y", Key("enter"),
                  "flex  scan.l", Key("enter"),
                  "gcc lex.yy.c y.tab.c -o cexpr.exe -lfl -ggdb3", Key("enter")],
    "build and run": [Key("enter"), Key("enter"), Key("enter"),
                  "yacc -d cexpr.y", Key("enter"),
                  "flex  scan.l", Key("enter"),
                  "gcc lex.yy.c y.tab.c -o cexpr.exe -lfl -ggdb3", Key("enter"),
                  "./cexpr.exe < test4 > mytest4", Key("enter"),
                  "sdiff mytest4 offtest4", Key("enter")],
    "run exec": ["./cexpr.exe < test"],
    "run vanilla": ["./cexpr.exe", Key("enter")],
    "run val grind": ["valgrind cexpr.exe < test1", Key("enter")],
    


    #"run": ["run", Key("enter")],
    "shell make": [Key("enter"), Key("enter"), Key("enter"), Key("enter"), "make ", Key("enter")],
    "check last": ["echo $?", Key("enter")],
    "run test": ["runTest", Key("enter")],      
    "open asm template": ["emacs assem-template.c", Key("enter")],
    "type password": ["Sug7&77z",Key("enter")],
    "make directory" : "mkdir ",

    # iOS
    "open workspace": ["open *space ", Key("enter")],
    # add pod to xCode
    "part in it": ["pod init", Key("enter")],
    "code part file": ["code Podfile", Key("enter")],
    "part install": ["pod install", Key("enter")],
    # .git
    "add get ignore": ["cp /Users/stevenberkowitz/Development/scripting/default\ files/.gitignore ."],
    #
    "print working directory": ["pwd ", Key("enter")],
    
    #
    "shell home": "~/",
    "lefty": Key("ctrl-a"),
    "ricky": Key("ctrl-e"),
    "clear back": Key("ctrl-u"),
    "clear line": [Key("ctrl-e"), Key("ctrl-u")],
    "(pain new | split vertical)": Key("cmd-d"),
    "new [S S H] [tab] {global_terminal.servers}": new_server,
    # talon
    "tail talon": "tail -f ~/.talon/talon.log",
    "talon reple": "~/.talon/bin/repl",
    "talon home": ["cd ~/.talon/user/talon_community/", Key("enter"), "ll ", Key("enter")],
    "open talon commands": ["code ~/.talon/user/talon_community/ ", Key("enter")],
    #"reverse": Key("ctrl-r"),
    "rerun": [Key("up"), Key("enter")],
    "cd": ["cd ; ls", Key("left"), Key("left"), Key("left"), Key("left")],
    "cd wild": [
        "cd **; ls",
        Key("left"),
        Key("left"),
        Key("left"),
        Key("left"),
        Key("left"),
    ],
    "cd wild [<dgndictation>]": [
        "cd **; ls",
        Key("left"),
        Key("left"),
        Key("left"),
        Key("left"),
        Key("left"),
        text,
    ],
    "cd {terminal.directory_shortcuts}": cd_directory_shortcut,
    "directory {terminal.directory_shortcuts}": name_directory_shortcuts,
    "(ls | run ellis | run alice)": "ls\n",
    "(la | run la)": "ls -la\n",
    "(shell | shall ) shortlist": ["ll", Key("enter")],
    # "durrup": "cd ..; ls\n",
    "go back": "cd -\n",
    "dash <dgndictation> [over]": dash,
    "pseudo": "sudo ",
    "(redo pseudo | pseudo [make me a] sandwich)": [
        Key("up"),
        Key("ctrl-a"),
        "sudo ",
        Key("enter"),
    ],
    "shell C H mod": "chmod ",
    "shell (make executable | add executable permissions)": "chmod a+x ",
    "shell clear": [Key("ctrl-c"), "clear\n"],
    "shell copy [<dgndictation>]": ["cp ", text],
    "shell copy (recursive | curse) [<dgndictation>]": ["cp -r", text],
    "shell kill": Key("ctrl-c"),
    "shell list [<dgndictation>]": ["ls ", text],
    "shell list all [<dgndictation>]": ["ls -la ", text],
    #"shell make (durr | dear | directory) [<dgndictation>]": ["mkdir ", text],
    "shell mipple [<dgndictation>]": ["mkdir -p ", text],
    "shell move [<dgndictation>]": ["mv ", text],
    "shell remove [<dgndictation>]": ["rm ", text],
    "shell remove (recursive | curse) [<dgndictation>]": ["rm -rf ", text],
    "shell enter": "ag -l | entr ",
    "shell enter 1": "ag -l . .. | entr ",
    "shell enter 2": "ag -l . ../.. | entr ",
    "shell enter 3": "ag -l . ../../.. | entr ",
    "shell enter 4": "ag -l . ../../../.. | entr ",
    "shell less [<dgndictation>]": ["less ", text],
    "shell cat [<dgndictation>]": ["cat ", text],
    "shell X args [<dgndictation>]": ["xargs ", text],
    "shell mosh": "mosh ",
    "[shell] mosh {global_terminal.servers}": mosh_servers,
    "[shell] (S S H | SSH) {global_terminal.servers}": ssh_servers,
    "[shell] S S H copy I D {global_terminal.servers}": ssh_copy_id_servers,
    "shell M player": "mplayer ",
    "shell nvidia S M I": "nvidia-smi ",
    "shell R sync": "./src/dotfiles/sync_rsync ",
    
    "shell tail follow": "tail -f ",
    "shall count lines": "wc -l ",
    "shell L S U S B": "lsusb",
    "shell net stat": "netstat -l ",
    "W get": "wget ",
    
    # apt-get
    "apt get": "apt-get ",
    "apt get install": "apt-get install ",
    "apt get update": "apt-get update ",
    "apt get upgrade": "apt-get upgrade ",
    # Tools
    
    "pee socks": "ps aux ",
    "vi": "vi ",
    
    # other
    #"shell make": "make\n",
    "shell jobs": "jobs\n",
    
}



for action in ("get", "delete", "describe"):
    for object in (
        "nodes",
        "jobs",
        "pods",
        "namespaces",
        "services",
        "events",
        "deployments",
        "replicasets",
        "",
    ):
        if object:
            object = object + " "
        command = f"{KUBERNETES_PREFIX} {action} {object}"
        typed = f"kubectl {action} {object}"
        keymap.update({command: typed})

keymap.update({"(pain | bang) " + str(i): Key("alt-" + str(i)) for i in range(10)})

ctx.keymap(keymap)
ctx.set_list("directory_shortcuts", directory_shortcuts.keys())
# ctx.set_list("servers", servers.keys())


def shell_rerun(m):
    # switch_app(name='iTerm2')
    app = ui.apps(bundle="com.googlecode.iterm2")[0]
    ctrl.key_press("c", ctrl=True, app=app)
    time.sleep(0.05)
    ctrl.key_press("up", app=app)
    ctrl.key_press("enter", app=app)


def shell_new_server(m):
    """
    global command for swtching to iterm, creating a new pain and logging into
    the specified server
    """
    switch_app("iTerm2")
    new_server(m)


global_ctx = Context("global_terminal")
global_ctx.keymap(
    {
        "shell rerun": shell_rerun,
        "shell server {global_terminal.servers}": name_servers,
        "shell new {global_terminal.servers}": shell_new_server,
    }
)
global_ctx.set_list("servers", servers.keys())
