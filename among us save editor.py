try:
    loaded = False
    colour = False
    print("Importing required modules...")
    for module in ["os", "webbrowser", "subprocess"]:
        try:
            exec(f"import {module}")
            print(f"Imported module: {module}")
            loaded = True
        except Exception as e:
            print(f"Failed to import module: {module} ({e})")
            loaded = False
    try:
        import requests
        print("Imported module: requests")
        loaded = True
    except ImportError:
        print(f"Failed to import required module: requests\nAttempt installation? (Y/n)")
        response = input("> ").lower()
        if response in ["1", "y", "yes", "t", "true"]:
            print("Attempting installation...")
            try:
                os.system('python -m pip install requests')
                import requests
            except Exception as e:
                print(f"Failed to import module: requests ({e})")
    except Exception as e:
        print(f"Failed to import module: {module} ({e})")
        loaded = False
    try:
        exec("import colorama")
        print(f"Imported optional module: colorama")
    except Exception as e:
        print(f"Failed to import optional module: colorama\nAttempt installation? (Y/n)")
        response = input("> ").lower()
        if response in ["1", "y", "yes", "t", "true"]:
            print("Proceeding with installation...")
            try:
                os.system('python -m pip install colorama')
                import colorama
            except:
                print("Install failed.\nProceeding without installation...")
        else:
            print("Proceeding without installation...")

    def hl(string, red, green, blue):
        return string
            
    try:
        colorama.init()
        colour = True
    except:
        print("Failed to initialize colorama. Terminal will not be highlighted.")
    if loaded == False:
        print("One or more required imports failed to load.")
        input("| [ENTER] to close program | ")
    else:
        if colour == True:
            def hl(string, red: int, green: int, blue: int):
                _colour = f"\x1b[38;2;{red};{green};{blue}m"
                return f"{colorama.Fore.RESET}{_colour}{string}{colorama.Fore.RESET}"
        print(f"{hl('Checking for updates...', 80, 160, 240)}")
        root = f"{os.path.expanduser('~')}\\AppData\\LocalLow\\sus"
        

        ###########################################################################
        
        source_main = "https://raw.githubusercontent.com/whatacalamity/sus/refs/heads/main/sus.py"
        source_updater = "https://raw.githubusercontent.com/whatacalamity/sus/refs/heads/main/among us save editor.py"
        
        ###########################################################################


        try:
            response = requests.get(source_updater)
        except:
            print(f"{hl('Could not connect to server. Check your internet connection. (among us save editor.py)', 255, 120, 0)}")
            print(f"{hl('Skipping launcher update...', 255, 120, 0)}")
        else:
            if response.status_code == 200:
                with open(__file__, "rb") as file:
                    a = file.read()
                    text = response.content
                    if a != text:
                        print(hl('Update found! (among us save editor.py)', 255, 200, 0))
                        print(hl("Select action:\n'source' - Show source (github)\n'install' - Install update\n'skip' - Continue without updating", 255, 255, 255))
                        while True:
                            action = input("> ").lower()
                            if action == "source":
                                webbrowser.open_new_tab(source_updater)
                            elif action == "install":
                                print(f"{hl('Updating...', 255, 200, 0)}")
                                with open(__file__, "wb") as file:
                                    file.write(text)
                                print(hl('All up to date! (among us save editor.py)', 0, 255, 0))
                            os.system(f"{__file__} 1")
                    else:
                        print(hl('All up to date! (among us save editor.py)', 0, 255, 0))
            else:
                print(f"{hl('Could not connect to server. Check your internet connection.', 255, 120, 0)}")
                print(f"{hl('Skipping launcher update...', 255, 120, 0)}")
        try:
            response = requests.get(source_main)
        except:
            print(f"{hl('Could not connect to server. Check your internet connection. (sus.py)', 255, 120, 0)}")
            print(f"{hl('Skipping editor update...', 255, 120, 0)}")
            os.system(f"{root}\\sus.py 1")
        else:
            if response.status_code == 200:
                if not os.path.exists(f"{root}\\sus.py"):
                    open(f"{root}\\sus.py", "w")
                with open(f"{root}\\sus.py", "rb") as file:
                    a = file.read()
                    text = response.content
                    if a != text:
                        print(hl('Update found! (sus.py)', 255, 200, 0))
                        print(hl("Select action:\n'source' - Show source (github)\n'install' - Install update and launch\n'skip' - Launch without updating", 255, 255, 255))
                        while True:
                            action = input("> ").lower()
                            if action == "source":
                                webbrowser.open_new_tab(source_main)
                            elif action == "install":
                                print(f"{hl('Updating...', 255, 200, 0)}")
                                with open(f"{root}\\sus.py", "wb") as file:
                                    file.write(text)
                                print(hl('All up to date! (sus.py)', 0, 255, 0))
                            os.system(f"{root}\\sus.py 1")
                    else:
                        print(hl('All up to date! (sus.py)', 0, 255, 0))
                        os.system(f"{root}\\sus.py 1")
            else:
                print(f"{hl('Could not connect to server. Check your internet connection.', 255, 120, 0)}")
                input("| [ENTER] to launch without updating | ")
                os.system(f"{root}\\sus.py 1")
                input("| [ENTER] to close program | ")
except Exception as e:
    print(f"Error opening the launcher. You should probably report this\n{e}")
    try:
        input("| [ENTER] to launch without updating | ")
        os.system(f"{root}\\sus.py 1")
    except Exception as e:
        print(f"Error opening the editor. You should probably report this\n{e}")
    input("| [ENTER] to close program | ")
