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
    "nightsquid projects": ["cd /Users/stevenberkowitz/Development/Nightsquid\ Personal\ Projects/; ls", Key("enter")],
    "fsu folder": ["fsu", Key("enter")],
    "midi visualizer folder": ["cd /Users/stevenberkowitz/Development/Nightsquid\ Personal\ Projects/music_projects/MIDI\ Visualizers",Key("enter")],
    "midi folder": ["cd /Users/stevenberkowitz/Documents/Music\ /MIDI; ls", Key("enter")],
    "scripting": ["cd /Users/stevenberkowitz/Development/scripting/; ls",Key("enter")],
    
    #
    # Utility
    "print working directory string": ["printf \"%q\\n\" \"$(pwd)\"",Key("enter")],
    "zip show config": ["zshrc", Key("enter")],
    "finder": ["open -a finder .", Key("enter")],
    "new terminal window": 
    [Key("ctrl-1"),Key("right"), Key("right"), Key("down"),Key("down"),Key("right"),Key("down"),Key("down"),Key("down")],
    "new terminal tab": [Key("ctrl-1"),Key("right"), Key("right"), Key("down"), Key("down"),Key("down"),Key("right"),Key("down"),Key("down")],
    "code": "code ",
    "node": "node ",
    "osc": ["osc", Key("enter")],

    "yes": ["y", Key("enter")],
    "no": ["n", Key("enter")], 
        # open apps/files
    "open unity": "open -a Unity",
    "openswiftlint": ["code .swiftlint.yml", Key("enter")],
    "open terminal commands": ["code /Users/stevenberkowitz/.talon/user/talon_community/apps/terminal.py", Key("enter")],
    "open xcode commands": ["code /Users/stevenberkowitz/.talon/user/talon_community/apps/xcode.py", Key("enter")],

    #  AppleScripts
    "add chrome url to notes": ["osascript /Users/stevenberkowitz/Development/scripting/addChromeUrlToNotes.applescript", Key("enter")],
    "input sleep data": ["osascript /Users/stevenberkowitz/Development/scripting/inputSleepData.applescript", Key("enter")],
    
    # Unix
    "touch": "touch ",
    "grep talon": ["grep   */*"],
    "echo path": ["echo $PATH", Key("enter")],
    "shell tree": ["tree", Key("enter")],

            # combine
    "open combine book": "open /Users/stevenberkowitz/Documents/Developer/Learning\ Resources/Ray\ Wenderlich/Combine_Asynchronous_Programming_with_Swift_v1.0.2/*.pdf",
    "open combine project": ["open -a Xcode /Users/stevenberkowitz/Documents/Developer/Learning\ Resources/Ray\ Wenderlich/Combine_Asynchronous_Programming_with_Swift_v1.0.2/0"],
    "open combine folder": ["open -a Finder /Users/stevenberkowitz/Documents/Developer/Learning\ Resources/Ray\ Wenderlich/Combine_Asynchronous_Programming_with_Swift_v1.0.2", Key("enter")],
    
    # git
    "code get ignore": ["code .gitignore", Key("enter")],
    "get pole": "g pull ",
    "get push": "g push ",
    "git add": "g add ",
    "add you": ["g add -u", Key("enter"), "sta", Key("enter")],
    "get show": "git show ",
    "glow": ["glo ", Key("enter")],
    "git list files": ["g ls-files", Key("enter")],
    "git remove": "g rm ",
    "get reset": "git reset",
    "sta": ["sta ", Key("enter")],
    "commit message": "g commit -m \"",
    "git checkout": "g checkout ",
    "checkout new branch": "g checkout -b ",
    "git branch": ["g branch ", Key("enter")],
    "git branch all": ["g branch -a", Key("enter")], 
    "git diff": "g diff ",
    "get diff stage": ["git diff --staged", Key("enter")],
    "git rebase": "g rebase -i ",
    "get - ": "git stash ",
    "get/pop": "git stash pop",
    

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
    "ssh": ["ssh berkowit@linprog.cs.fsu.edu", Key("enter")],
    "open fsu tabs": "osascript /Users/stevenberkowitz/Development/Nightsquid\ Personal\ Projects/automation/openFSUTabsInChrome.applescript",
    
    # operating systems
#    "obsess": ["opsys", Key("enter")],
    "obsess": ["cd /home/majors/berkowit/cop4610/proj3/xv6-public; ls", Key("enter")],
    "exit shell": ["exit", Key("enter")],
    "type a list": ["ls -l", Key("enter")],
    "type semi list": ["ls -l;", Key("enter")],

    # Programming Languages
    "C make": ["g++ -std=c++11 -Wall -Wextra -o cparse.x cparse.cpp;", Key("enter"), Key("enter"),"./cparse.x ./proj3_official/extra1", Key("enter")], 


    #"run": ["run", Key("enter")],
    "shell make": [Key("enter"), Key("enter"), Key("enter"), Key("enter"), "make ", Key("enter")],
    "check last": ["echo $?", Key("enter")],
    "run test": ["runTest", Key("enter")],      
    "open asm template": ["emacs assem-template.c", Key("enter")],
    "type password": ["Sug7&77z",Key("enter")],
    "make directory" : "mkdir ",

    # iOS
    "open workspace": ["open -a 'Xcode 11.1 11A1027' *space ", Key("enter")],
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
    "shell tail": "tail ",
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
    "(grep | grip)": "grep ",
    "gripper": ["grep -r  .", Key("left left")],
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
