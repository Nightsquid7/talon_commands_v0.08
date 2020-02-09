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
    "go to shell home": ["cd ~/ ; ls ", Key("enter")],
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
        # open apps/files
    "open unity": "open -a Unity",
    "openswiftlint": ["code .swiftlint.yml", Key("enter")],
    "yes": ["y", Key("enter")],
    "no": ["n", Key("enter")], 

    #  AppleScripts
    "add chrome url to notes": ["osascript /Users/stevenberkowitz/Development/scripting/addChromeUrlToNotes.applescript", Key("enter")],
    "input sleep data": ["osascript /Users/stevenberkowitz/Development/scripting/inputSleepData.applescript", Key("enter")],
    # Unix
    "touch": "touch ",
    "grep talon": ["grep   */*"],
    "echo path": ["echo $PATH", Key("enter")],

            # combine
    "open combine book": "open /Users/stevenberkowitz/Documents/Developer/Learning\ Resources/Ray\ Wenderlich/Combine_Asynchronous_Programming_with_Swift_v1.0.2/*.pdf",
    "open combine project": ["open -a Xcode /Users/stevenberkowitz/Documents/Developer/Learning\ Resources/Ray\ Wenderlich/Combine_Asynchronous_Programming_with_Swift_v1.0.2/0"],
    "open combine folder": ["open -a Finder /Users/stevenberkowitz/Documents/Developer/Learning\ Resources/Ray\ Wenderlich/Combine_Asynchronous_Programming_with_Swift_v1.0.2", Key("enter")],
    
    # git
    "git pull": "g pull",
    "add you": ["g add -u", Key("enter"), "sta", Key("enter")],
    "git add": "g add ",
    "glow": ["glo ", Key("enter")],
    "git list files": ["g ls-files", Key("enter")],
    "git remove": "g rm ",
    "sta": ["sta ", Key("enter")],
    "commit message": "g commit -m \"",
    "git checkout": "g checkout ",
    "checkout new branch": "g checkout -b ",
    "git branch": ["g branch ", Key("enter")],
    "git branch all": ["g branch -a", Key("enter")], 
    #"git branch": "git branch ",
    "git diff": "g diff ",
    "git rebase": "g rebase -i ",
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
    # C Commands
    #"see print": ["printf();", Key("left"),Key("left")],
    "see print": ["printf(\"\\n\");", Key("left"),Key("left"),Key("left")],
    "see scan": ["sscanf(,)"],
    
    # fsu Comp Sci
    "ssh": ["ssh berkowit@linprog.cs.fsu.edu", Key("enter")],
    "open fsu tabs": "osascript /Users/stevenberkowitz/Development/Nightsquid\ Personal\ Projects/automation/openFSUTabsInChrome.applescript",
    
    # operating systems
    "exit shell": ["exit", Key("enter")],
    "type a list": ["ls -l", Key("enter")],
    "type semi list": ["ls -l;", Key("enter")],


    #"run": ["run", Key("enter")],
    "make": [Key("enter"), Key("enter"), Key("enter"), Key("enter"), "make ", Key("enter")],
    "check last": ["echo $?", Key("enter")],
    "run test": ["runTest", Key("enter")],      
    "open asm template": ["emacs assem-template.c", Key("enter")],
    "type password": ["Sug7&77z",Key("enter")],
    "make directory" : "mkdir ",

    # iOS
    "open workspace": ["open -a 'Xcode.app' *space ", Key("enter")],
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
    "pseudo shut down now": "sudo shutdown now",
    "shell C H mod": "chmod ",
    "shell (make executable | add executable permissions)": "chmod a+x ",
    "shell clear": [Key("ctrl-c"), "clear\n"],
    "shell copy [<dgndictation>]": ["cp ", text],
    "shell copy (recursive | curse) [<dgndictation>]": ["cp -r", text],
    "shell kill": Key("ctrl-c"),
    "shell list [<dgndictation>]": ["ls ", text],
    "shell list all [<dgndictation>]": ["ls -la ", text],
    "shell make (durr | dear | directory) [<dgndictation>]": ["mkdir ", text],
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
    # "shell server {terminal.servers}": name_servers,
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
    # python
    "create virtual environment": ["virtualenv -p python3 venv", Key("enter")],
    "activate virtual environment": [
        "source `find . | grep bin/activate$`",
        Key("enter"),
    ],
    # apt-get
    "apt get": "apt-get ",
    "apt get install": "apt-get install ",
    "apt get update": "apt-get update ",
    "apt get upgrade": "apt-get upgrade ",
    # Tools
    # "(grep | grip)": ["grep  .", Key("left left")],
    "(grep | grip)": "grep ",
    "gripper": ["grep -r  .", Key("left left")],
    "pee socks": "ps aux ",
    "vi": "vi ",
    # docker
    "docker P S": "docker ps ",
    "docker (remove | R M)": "docker rm ",
    "docker stop": "docker stop ",
    "docker run": "docker run ",
    "docker exec": "docker exec ",
    "docker logs": "docker logs ",
    "docker shell": ["docker exec -it  bash"] + [Key("left")] * 5,
    "docker shell P X 4": ["docker exec -it px4simulator bash"] + [Key("left")] * 5,
    "docker compose up": "docker-compose up ",
    "docker compose down": "docker-compose down ",
    "docker detach": [Key("ctrl-p"), Key("ctrl-q")],
    # kubectl
    KUBERNETES_PREFIX + "control": "kubectl ",
    KUBERNETES_PREFIX + "create": "kubectl create ",
    KUBERNETES_PREFIX + "expose": "kubectl expose ",
    KUBERNETES_PREFIX + "run": "kubectl run ",
    KUBERNETES_PREFIX + "set": "kubectl set ",
    KUBERNETES_PREFIX + "run-container": "kubectl run-container ",
    KUBERNETES_PREFIX + "get": "kubectl get ",
    KUBERNETES_PREFIX + "explain": "kubectl explain ",
    KUBERNETES_PREFIX + "edit": "kubectl edit ",
    KUBERNETES_PREFIX + "delete": "kubectl delete ",
    KUBERNETES_PREFIX + "rollout": "kubectl rollout ",
    KUBERNETES_PREFIX + "rolling-update": "kubectl rolling-update ",
    KUBERNETES_PREFIX + "scale": "kubectl scale ",
    KUBERNETES_PREFIX + "autoscale": "kubectl autoscale ",
    KUBERNETES_PREFIX + "certificate": "kubectl certificate ",
    KUBERNETES_PREFIX + "cluster-info": "kubectl cluster-info ",
    KUBERNETES_PREFIX + "top": "kubectl top ",
    KUBERNETES_PREFIX + "cordon": "kubectl cordon ",
    KUBERNETES_PREFIX + "uncordon": "kubectl uncordon ",
    KUBERNETES_PREFIX + "drain": "kubectl drain ",
    KUBERNETES_PREFIX + "taint": "kubectl taint ",
    KUBERNETES_PREFIX + "describe": "kubectl describe ",
    KUBERNETES_PREFIX + "logs": "kubectl logs ",
    KUBERNETES_PREFIX + "attach": "kubectl attach ",
    KUBERNETES_PREFIX + "exec": "kubectl exec ",
    KUBERNETES_PREFIX + "port-forward": "kubectl port-forward ",
    KUBERNETES_PREFIX + "proxy": "kubectl proxy ",
    KUBERNETES_PREFIX + "cp": "kubectl cp ",
    KUBERNETES_PREFIX + "auth": "kubectl auth ",
    KUBERNETES_PREFIX + "apply": "kubectl apply ",
    KUBERNETES_PREFIX + "patch": "kubectl patch ",
    KUBERNETES_PREFIX + "replace": "kubectl replace ",
    KUBERNETES_PREFIX + "convert": "kubectl convert ",
    KUBERNETES_PREFIX + "label": "kubectl label ",
    KUBERNETES_PREFIX + "annotate": "kubectl annotate ",
    KUBERNETES_PREFIX + "completion": "kubectl completion ",
    KUBERNETES_PREFIX + "api": "kubectl api ",
    KUBERNETES_PREFIX + "config": "kubectl config ",
    KUBERNETES_PREFIX + "help": "kubectl help ",
    KUBERNETES_PREFIX + "plugin": "kubectl plugin ",
    KUBERNETES_PREFIX + "version": "kubectl version ",
    KUBERNETES_PREFIX
    + "shell": ["kubectl exec -it  -- /bin/bash"]
    + [Key("left")] * 13,
    # conda
    "conda install": "conda install ",
    "conda list": "conda list ",
    # tmux
    "T mux new session": "tmux ",
    "T mux list": "tmux ls",
    "T mux attach [<dgndictation>]": ["tmux a -t ", text],
    "T mux scroll": [Key("ctrl-b"), Key("[")],
    # other
    "shell make": "make\n",
    "shell jobs": "jobs\n",
    # gsutil
    "G S you till acl": "gsutil acl ",
    "G S you till bucketpolicyonly": "gsutil bucketpolicyonly ",
    "G S you till cat": "gsutil cat ",
    "G S you till compose": "gsutil compose ",
    "G S you till config": "gsutil config ",
    "G S you till cors": "gsutil cors ",
    "G S you till cp": "gsutil cp ",
    "G S you till defacl": "gsutil defacl ",
    "G S you till defstorageclass": "gsutil defstorageclass ",
    "G S you till D U": "gsutil du ",
    "G S you till hash": "gsutil hash ",
    "G S you till help": "gsutil help ",
    "G S you till I am": "gsutil iam ",
    "G S you till K M S": "gsutil kms ",
    "G S you till label": "gsutil label ",
    "G S you till lifecycle": "gsutil lifecycle ",
    "G S you till logging": "gsutil logging ",
    "G S you till L S": "gsutil ls ",
    "G S you till M B": "gsutil mb ",
    "G S you till move": "gsutil mv ",
    "G S you till notification": "gsutil notification ",
    "G S you till perfdiag": "gsutil perfdiag ",
    "G S you till rb": "gsutil rb ",
    "G S you till requesterpays": "gsutil requesterpays ",
    "G S you till retention": "gsutil retention ",
    "G S you till rewrite": "gsutil rewrite ",
    "G S you till rm": "gsutil rm ",
    "G S you till rsync": "gsutil rsync ",
    "G S you till setmeta": "gsutil setmeta ",
    "G S you till signurl": "gsutil signurl ",
    "G S you till stat": "gsutil stat ",
    "G S you till test": "gsutil test ",
    "G S you till update": "gsutil update ",
    "G S you till version": "gsutil version ",
    "G S you till versioning": "gsutil versioning ",
    "G S you till web": "gsutil web ",
    # rostopic
    "ross topic bandwidth": "rostopic bw ",
    "ross topic delay  ": "rostopic delay ",
    "ross topic echo   ": "rostopic echo ",
    "ross topic find   ": "rostopic find ",
    "ross topic hertz  ": "rostopic hz ",
    "ross topic info   ": "rostopic info ",
    "ross topic list   ": "rostopic list ",
    "ross topic pub    ": "rostopic pub ",
    "ross topic type   ": "rostopic type ",
}

for pip in ("pip", "pip3"):
    keymap.update(
        {
            f"{pip}": f"{pip}",
            f"{pip} install": f"{pip} install ",
            f"{pip} install requirements": f"{pip} install -r ",
            f"{pip} install editable": f"{pip} install -e ",
            f"{pip} install this": f"{pip} install -e .",
            f"{pip} install local": f"{pip} install -e .",
            f"{pip} [install] upgrade": f"{pip} install --upgrade ",
            f"{pip} uninstall": f"{pip} uninstall ",
            f"{pip} list": f"{pip} list",
        }
    )

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
