# Updater

LAUNCHER_VERSION = "0.0"

EDITOR_VERSION = "0.0"

##################################################################################################

source_editor = "https://raw.githubusercontent.com/whatacalamity/sus/refs/heads/main/sus.py"
source_updater = "https://raw.githubusercontent.com/whatacalamity/sus/refs/heads/main/among us save editor.py"
source_version = "https://raw.githubusercontent.com/whatacalamity/sus/refs/heads/main/impostor.json"
required_imports = ["requests", "webbrowser", "json"]
optional_imports = ["colorama"]

##################################################################################################

inf = float("inf")

def gt(v1, v2):
    if v1.count(".") + v2.count(".") == 0:
        return int(v1) > int(v2)
    v1, v2 = f"{v1}.0" if v1.count(".")==0 else v1, f"{v2}.0" if v2.count(".")==0 else v2
    if int(v1.split(".")[0]) > int(v2.split(".")[0]):
        return True
    elif int(v1.split(".")[0]) == int(v2.split(".")[0]):
        return gt(".".join(v1.split(".")[1:]), ".".join(v2.split(".")[1:]))
    else:
        return False

vc = {
    "editor": {"version": inf, "changelog": "-"},
    "updater": {"version": inf, "changelog": "-"}
}

templates = {
    "preferences": {
        "autosave": True,
        "backups": True,
        "colorama": True
    },
    "presets": {
        "normal": {},
        "hidenseek": {}
    }
}

modules = {}

try:
    modules["os"] = __import__("os")
except ImportError:
    print("Critical module \"os\" not found. How did you even pull this off?")
    input("Press ENTER to close program.\n> ")
    exit(713)
except:
    print("An error occurred while trying to import critical module \"os\". How did you even pull this off?")
    input("Press ENTER to close program.\n> ")
    exit(713)

def pause(msg: str="Press any key to continue . . ."):
    print(msg)
    return modules["os"].system(f"pause >{modules['os'].devnull} 2>&1")

pip = True

print("Verifying pip installation...")
if modules["os"].system(f"python -m pip --version >{modules['os'].devnull} 2>&1") == 1:
    pause("pip is missing.\nPress any key to install pip.")
    print("Installing pip...")
    try:
        modules["os"].system("python -m ensurepip --upgrade")
    except:
        print("An error occurred while trying to verify pip's installation.")
        pause("Press any key to skip verification. (You cannot install missing dependencies.)")
        pip = False
    else:
        print("Verifying pip installation...")
        modules["os"].system(f"python -m pip install --upgrade pip >{modules['os'].devnull} 2>&1")
        print("pip installation verified")
else:
    modules["os"].system(f"python -m pip install --upgrade pip >{modules['os'].devnull} 2>&1")
    print("pip installation verified")
        
skip = []
    
for module in optional_imports:
    while not module in modules.keys() and not module in skip:
        print(f"Attempting to import optional module \"{module}\"...")
        try:
            modules[module] = __import__(module)
        except ImportError:
            if pip == False:
                print(f"Optional module \"{module}\" not found. Dependencies cannot be installed at this time.")
                pause("Press any key to skip installation.")
                skip += [module]
            elif input(f"Optional module \"{module}\" not found. Attempt installation? Y/N\n> ").lower() in ["y", "yes"]:
                if modules["os"].system(f"python -m pip install {module}") == 1:
                    print(f"An error occurred while trying to install optional module \"{module}\". Retrying import...")
                else:
                    modules[module] = __import__(module)
                continue
            else:
                print("Skipping installation...")
                skip += [module]
        else:
            if module == "colorama":
                print(f"{modules['colorama'].Fore.RESET}\x1b[38;2;40;200;40mImported optional module \"colorama\".{modules['colorama'].Fore.RESET}")
            else:
                print(f"Imported optional module \"{module}\".")

skip = False

for module in required_imports:
    while not module in modules.keys() and skip == False:
        print(f"Attempting to import required module \"{module}\"...")
        try:
            modules[module] = __import__(module)
        except ImportError:
            if pip == False:
                print(f"Required module \"{module}\" not found. Dependencies cannot be installed at this time.")
                pause("Press any key to launch without updating.")
            elif input(f"Required module \"{module}\" not found. Attempt installation? Y/N\n> ").lower() in ["y", "yes"]:
                if modules["os"].system(f"python -m pip install {module}") == 1:
                    print(f"An error occurred while trying to install required module \"{module}\". Retrying import...")
                else:
                    modules[module] = __import__(module)
                continue
            else:
                print("Launching without updating...")
                skip = True
        else:
            if "colorama" in modules.keys():
                modules["colorama"].init()
                def print(text, red: int=204, green: int=204, blue: int=204):
                    return __builtins__.print(f"{modules['colorama'].Fore.RESET}\x1b[38;2;{red};{green};{blue}m{text}{modules['colorama'].Fore.RESET}")
                
                def input(text, red: int=204, green: int=204, blue: int=204):
                    return __builtins__.input(f"{modules['colorama'].Fore.RESET}\x1b[38;2;{red};{green};{blue}m{text}{modules['colorama'].Fore.RESET}")
                
                def pause(msg: str="Press any key to continue . . .", red: int=204, green: int=204, blue: int=204):
                    print(msg, red, green, blue)
                    return modules["os"].system(f"pause >{modules['os'].devnull} 2>&1")
            else:
                def print(text, red: int=204, green: int=204, blue: int=204):
                    return __builtins__.print(text)
                
                def input(text, red: int=204, green: int=204, blue: int=204):
                    return __builtins__.input(text)
            print(f"Imported required module \"{module}\".", 40, 200, 40)

parent = "\\".join(__file__.replace("/","\\").split("\\")[:-1])
if not modules["os"].path.exists(f"{parent}\\ඞ"):
    print("This is the first time the launcher has been used.", 200, 180, 0)
    pause("Press any key to apply first-time changes and restart the launcher.")
    if not modules["os"].path.exists(f"{parent}\\among us save editor"):
        modules["os"].mkdir(f"{parent}\\among us save editor")
    modules["os"].rename(__file__, f"{parent}\\among us save editor\\among us save editor.py")
    with open(f"{parent}\\among us save editor\\ඞ", "w") as file:
        file.write("this file is here so the setup procedure doesn't run on every startup")
        file.close()
    if modules["os"].system("cls") == 1:
        modules["os"].system("clear")
    modules["os"].system(f"python \"{parent}\\among us save editor\\among us save editor.py\"")

if not modules["os"].path.exists(f"{parent}\\config"):
    print("Creating missing directory: /config", 200, 80, 0)
    modules["os"].mkdir(f"{parent}\\config")

if not modules["os"].path.exists(f"{parent}\\config\\preferences.json"):
    print("Creating missing file: /config/preferences.json", 200, 80, 0)
    with open(f"{parent}\\config\\preferences.json", "w") as file:
        file.write("{}")

if not modules["os"].path.exists(f"{parent}\\config\\presets.json"):
    print("Creating missing file: /config/presets.json", 200, 80, 0)
    with open(f"{parent}\\config\\presets.json", "w") as file:
        file.write("{}")

if not modules["os"].path.exists(f"{parent}\\config\\backups"):
    print("Creating missing directory: /config/backups", 200, 80, 0)
    modules["os"].mkdir(f"{parent}\\config\\backups")

with open(f"{parent}\\config\\preferences.json", "r+") as file:
    data = modules["json"].loads(file.read())
    if templates["preferences"] | data != data:
        if data != {}:
            print("The preferences template no longer matches your savedata.", 200, 180, 0)
            pause("Press any key to merge /config/preferences.json with the new template.")
        file.seek(0)
        file.write(modules["json"].dumps(templates["preferences"] | data, indent=4))
    file.close()

with open(f"{parent}\\config\\presets.json", "r+") as file:
    data = modules["json"].loads(file.read())
    if templates["presets"] | data != data:
        if data != {}:
            print("The presets template no longer matches your savedata.", 200, 180, 0)
            pause("Press any key to merge /config/presets.json with the new template.")
        file.seek(0)
        file.write(modules["json"].dumps(templates["presets"] | data, indent=4))
    file.close()

sus = False

if modules["os"].path.exists(f"{parent}\\sus.py"):
    sus = True
    with open(f"{parent}\\sus.py", "r") as file:
        EDITOR_VERSION = ''.join([k for k in file.readlines()[0].split("=")[-1] if not k in " \n\""])
else:
    print("sus.py is missing. Editor installation cannot be skipped.", 200, 120, 0)

if skip == False:
    print("Checking for updates...", 200, 180, 40)
    try:
        response = modules["requests"].get("https://8.8.8.8")
    except:
        print("You are not connected to the internet. Skipping updater...", 200, 40, 40)
    else:
        try:
            response = modules["requests"].get(source_version)
            if response.status_code == 200:
                vc = response.json()
                if gt(LAUNCHER_VERSION, vc["updater"]["version"]):
                    print(f"Launcher is somehow newer than the latest release, how did you even pull this off? ({LAUNCHER_VERSION} > {vc['updater']['version']})", 200, 40, 200)
                elif gt(vc["updater"]["version"], LAUNCHER_VERSION):
                    print(f"\nLauncher update available! ({LAUNCHER_VERSION} -> {vc['updater']['version']})", 40, 200, 200)
                    print(f"\n{vc['updater']['changelog']}", 40, 200, 200)
                    print("\n'install' to install\n'source' to view source\n'skip' to skip update")
                    action = ""
                    while not action in ["install", "source", "skip"]:
                        action = input("> ").lower()
                        if action == "source":
                            print("Source opened in new tab.", 200, 180, 0)
                            modules["webbrowser"].open(source_updater)
                            action = ""
                        elif action == "skip":
                            print("Continuing without update...", 200, 180, 0)
                        elif action == "install":
                            if input("Proceed with installing? Y/N\n> ").lower() in ["y", "yes"]:
                                try:
                                    print("Downloading...", 200, 180, 40)
                                    response = modules["requests"].get(source_updater)
                                    if response.status_code == 200:
                                        _ = EDITOR_VERSION
                                        EDITOR_VERSION = "0.0"
                                        a = (response.text.replace("LAUNCHER_VERSION = \"0.0\"", f"LAUNCHER_VERSION = \"{vc['updater']['version']}\"")).encode("utf8")
                                        EDITOR_VERSION = _
                                        with open(__file__, "wb") as file:
                                            file.write(a)
                                        print("Restart required for update to take effect.", 200, 180, 40)
                                        pause("Press any key to restart the launcher.")
                                        modules["os"].system("cls")
                                        modules["os"].system(f"python \"{__file__}\"")
                                    else:
                                        print("Error in downloading launcher. Is Github down?")
                                        action = ""
                                except:
                                    print("Error in downloading launcher. Is Github down?")
                                    action = ""
                            else:
                                print("Installation aborted.", 200, 180, 0)
                                action = ""
                        else:
                            print("Invalid action.", 200, 40, 40)
                else:
                    print(f"Launcher is up to date! ({LAUNCHER_VERSION})", 40, 200, 40)
                if gt(EDITOR_VERSION, vc["editor"]["version"]):
                    print(f"Editor is somehow newer than the latest release, how did you even pull this off? ({EDITOR_VERSION} > {vc['editor']['version']})", 200, 40, 200)
                elif gt(vc["editor"]["version"], EDITOR_VERSION):
                    print(f"\nEditor update available! ({EDITOR_VERSION} -> {vc['editor']['version']})", 40, 200, 200)
                    print(f"\n{vc['editor']['changelog']}", 40, 200, 200)
                    print("\n'install' to install\n'source' to view source")
                    if sus == True:
                        print("'skip' to skip update")
                    else:
                        print("This update cannot be skipped, as sus.py is missing.", 200, 120, 0)
                    action = ""
                    while not (action in ["install", "source"] or (action == "skip" and sus == True)):
                        action = input("> ").lower()
                        if action == "source":
                            print("Source opened in new tab.", 200, 180, 0)
                            modules["webbrowser"].open(source_editor)
                            action = ""
                        elif action == "skip":
                            print("Continuing without update...", 200, 180, 0)
                        elif action == "install":
                            if input("Proceed with installing? Y/N\n> ").lower() in ["y", "yes"]:
                                try:
                                    print("Downloading...", 200, 180, 40)
                                    response = modules["requests"].get(source_editor)
                                    if response.status_code == 200:
                                        a = (response.text.replace("VERSION = \"0.0\"", f"VERSION = \"{vc['editor']['version']}\"")).encode("utf8")
                                        with open(f"{parent}\\sus.py", "wb") as file:
                                            sus = True
                                            file.write(a)
                                    else:
                                        print("Error in downloading editor. Is Github down?")
                                        action = ""
                                except:
                                    print("Error in downloading editor. Is Github down?")
                                    action = ""
                            else:
                                print("Installation aborted.", 200, 180, 0)
                                action = ""
                        else:
                            print("Invalid action.", 200, 40, 40)
                else:
                    print(f"Editor is up to date! ({EDITOR_VERSION})", 40, 200, 40)
            else:
                print("Error in getting version control. Is Github down?", 200, 120, 0)
        except Exception as e:
            print(e)
            print("Error in getting version control. Is Github down?", 200, 120, 0)

if sus == True:
    pause("Press any key to open the editor.")
    if modules["os"].system("cls") == 1:
        modules["os"].system("clear")
    modules["os"].system(f"python \"{parent}\\sus.py\"")


























        


print("How did we get here?", 80, 160, 200)
pause("Press any key to close program.")
exit(0)
