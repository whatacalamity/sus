# Updater

VERSION = "0.0"

##################################################################################################

source_main = "https://raw.githubusercontent.com/whatacalamity/sus/refs/heads/main/sus.py"
source_updater = "https://raw.githubusercontent.com/whatacalamity/sus/refs/heads/main/among us save editor.py"
source_version = "https://raw.githubusercontent.com/whatacalamity/sus/refs/heads/main/impostor.json"
required_imports = ["builtins", "requests", "webbrowser", "backoff"]
optional_imports = ["colorama"]

##################################################################################################

inf = float("inf")

def gt(v1, v2):
    v1, v2 = f"{v1}", f"{v2}"
    v1, v2 = v1+".0" if v1.count(".")==0 else v1, v2+".0" if v2.count(".")==0 else v2
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
try:
    modules["os"].system(f"python -m ensurepip --upgrade >{modules['os'].devnull} 2>&1")
except:
    print(f"An error occurred while trying to verify pip's installation.")
    pause("Press any key to skip verification. (You cannot install missing dependencies.)")
    pip = False
print("pip installation verified.")

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
            elif input(f"Optional module \"{module}\" not found. Attempt installation? Y/N\n> ").lower() in ["y", "yes"]:
                try:
                    modules["os"].system(f"pip install {module}")
                except:
                    print(f"An error occurred while trying to install optional module \"{module}\".")
                    pause("Press any key to skip installation.")
                    print("Skipping installation...")
                    skip += [module]
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
                try:
                    modules["os"].system(f"pip install {module}")
                except:
                    print(f"An error occurred while trying to install required module \"{module}\".", 200, 40, 40)
                    pause("Press any key to launch without updating.")
                    skip = True
                    break
                continue
            elif input(f"Required module \"{module}\" not found. Attempt installation? Y/N\n> ").lower() in ["y", "yes"]:
                try:
                    modules["os"].system(f"pip install {module}")
                except:
                    print(f"An error occurred while trying to install required module \"{module}\".")
                    pause("Press any key to launch without updating.")
                    print("Launching without updating...")
                    skip = True
                continue
            else:
                print("Launching without updating...")
                skip = True
                
        else:
            if module == "builtins":
                if "colorama" in modules.keys():
                    modules["colorama"].init()
                    def print(text, red: int=204, green: int=204, blue: int=204):
                        return modules["builtins"].print(f"{modules['colorama'].Fore.RESET}\x1b[38;2;{red};{green};{blue}m{text}{modules['colorama'].Fore.RESET}")
                    
                    def input(text, red: int=204, green: int=204, blue: int=204):
                        return modules["builtins"].input(f"{modules['colorama'].Fore.RESET}\x1b[38;2;{red};{green};{blue}m{text}{modules['colorama'].Fore.RESET}")
                    
                    def pause(msg: str="Press any key to continue . . .", red: int=204, green: int=204, blue: int=204):
                        print(msg, red, green, blue)
                        return modules["os"].system(f"pause >{modules['os'].devnull} 2>&1")
                else:
                    def print(text, red: int=204, green: int=204, blue: int=204):
                        return modules["builtins"].print(text)
                    
                    def input(text, red: int=204, green: int=204, blue: int=204):
                        return modules["builtins"].input(text)
            print(f"Imported required module \"{module}\".", 40, 200, 40)



if skip == False:
    @modules["backoff"].on_exception(
        modules["backoff"].expo,
        modules["requests"].exceptions.RequestException,
        max_tries=3,
        giveup=lambda e: e.response is not None and e.response.status_code != 200
    )
    def get(url: str):
        return modules["requests"].get(url, timeout=20)
    try:
        response = modules["requests"].get("https://8.8.8.8")
    except:
        print("You are not connected to the internet. Skipping updater...", 200, 40, 40)
    else:
        print("Checking for updates...", 200, 180, 40)
        try:
            response = modules["requests"].get(source_version)
            if response.status_code == 200:
                vc = response.json()
                print(vc)
                if gt(vc["updater"]["version"], VERSION):
                    print(f"\nLauncher update available! ({VERSION} -> {vc['updater']['version']})", 40, 200, 200)
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
                            if input(f"Proceed with installing? Y/N\n> ").lower() in ["y", "yes"]:
                                try:
                                    print("Downloading...", 200, 180, 40)
                                    response = get(source_updater)
                                    if response.status_code == 200:
                                        a = (response.text.replace("VERSION = \"0.0\"", f"VERSION = \"{vc['updater']['version']}\"")).encode("utf8")
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
                print("Error in getting version control. Is Github down?", 255, 120, 0)
        except:
            print("Error in getting version control. Is Github down?", 255, 120, 0)





























        


print("How did we get here?", 80, 160, 200)
pause("Press any key to close program.")
exit(0)
