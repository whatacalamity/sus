loaded = False
colour = False
print("Importing required modules...")
for module in ["base64", "json", "os", "math"]:
    try:
        exec(f"import {module}")
        print(f"Imported module: {module}")
        loaded = True
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
            exec("import colorama")
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
    def newfolder(path):
        if not os.path.exists(path):
            os.makedirs(path)
    if colour == True:
        def hl(string, red: int, green: int, blue: int):
            _colour = f"\x1b[38;2;{red};{green};{blue}m"
            return f"{colorama.Fore.RESET}{_colour}{string}{colorama.Fore.RESET}"
    else:
        print("oopsie")
    parent = '\\'.join(__file__.split("\\")[:-1])
    if parent.split("\\")[-1] != "Among us save editor":
        print(f"{hl('This is the first time this program has been executed. Configuring...', 80, 160, 240)}")
        print(f"{hl('This script has been moved to <'+parent+'\\sus.py>', 255, 200, 0)}")
        newfolder(parent+"\\Among us save editor")
        parent = parent+"\\Among us save editor"
        os.rename(__file__, parent+"\\sus.py")
        __file__ = parent+"\\sus.py"
        with open(parent+"\\config.json", "w") as file:
            json.dump({
                "presets": {
                    
                }
            }, file)
        with open(parent+"\\backup.json", "w") as file:
            json.dump({
                "presets": {
                    
                }
            }, file)
        with open(parent+"\\settings.amogus", "w") as file1:
            with open(f"{os.path.expanduser('~')}\\AppData\\LocalLow\\Innersloth\\Among Us\\settings.amogus", "r") as file2:
                data = json.loads(file2.read())
            json.dump(data, file1)
    def fuzzyround(a, epsilon=1e-9):
        return round(a/epsilon)*epsilon
    def to_float(a: list):
        if a == [0, 0]:
            return 0
        return 2*((a[0]/256)+((1-(a[0]//128))/2)) * (2**(((a[1]*2)+(a[0]//128))-127))
    def to_sus(a: float):
        a = float(a)
        try:
            return [math.floor(256*(((a-((2**math.floor(2*math.log(math.sqrt(2*a), 2)))/2))/(2**math.floor(2*math.log(math.sqrt(2*a), 2)))+((((math.floor(2*math.log(math.sqrt(2*a), 2))/2)%1)))))), math.floor(math.log(math.sqrt(a)*2.82842712475, 2))+62]
        except:
            return [0, 0]
    def encode(data: list):
        return base64.b64encode(bytes(data)).decode("utf8")
    def decode(data):
        return list(bytearray(base64.b64decode(data)))
    def cast(string: str):
        try:
            k = float(string)
            if k == round(k):
                k = int(k)
                return k
            # else:
            #     time to figure out how among us stores floats [0-255][0-255]
        except:
            try:
                return {"y": 1, "yes": 1, "n": 0, "no": 0, "cancel": 0, "true": 1, "false": 0, "skeld": 0, "theskeld": 0, "mirahq": 1, "mira": 1, "polus": 2, "theairship": 3, "airship": 3, "the fungle": 4, "fungle": 4, "short": 0, "medium": 1, "long": 2, "always": 0, "meetings": 1, "never": 2}[string.lower().replace(" ","")]
            except:
                return 0
                print("Invalid string value.")
    def floatpad(num: float, unit: str=" "):
        num = float(num)
        length = 6
        a = f"{num}".split(".")
        string = f"{a[0]}.{a[1][0]}{unit} "
        if len(string) == 7:
            return hl(string[0:5]+"   ", 255, 255, 255)
        elif len(string) == 8:
            return hl(string[0:6]+"  ", 255, 255, 255)
        elif len(string) > 8:
            return hl("∞       ", 0, 80, 255)
        while len(string) < length:
            string += " "
        if num == 0:
            return hl(f"{string}                    "[0:8], 255, 0, 0)
        else:
            return hl(f"{string}                    "[0:8], 255, 255, 255)
    def pad(string, length: int):
        string = f"{string}"
        while len(string) < length:
            string += " "
        return hl(string, 255, 255, 255)
    def intpad(num: int, length: int, unit:str=""):
        string = f"{num}{unit}"
        while len(string) < length:
            string += " "
        if num == 0:
            return hl(string, 255, 0, 0)
        else:
            return hl(string, 255, 255, 255)
    def oddspad(num):
        length = 3
        string = f"{num}"
        while len(string) < length:
            string += " "
        if num == 0:
            return hl("0%  ", 255, 0, 0)
        elif num == 100:
            return hl("100%", 0, 255, 0)
        else:
            return hl(f"{string}%", 255, 255, 0)
    def rolepad(num, unit: str=" "):
        length = 4
        string = f"{num}{unit}"
        while len(string) < length:
            string += " "
        if num == 0:
            return hl("∞   ", 0, 80, 255)
        else:
            return hl(f"{string}", 255, 255, 255)
    def load():
        with open(f"{os.path.expanduser('~')}\\AppData\\LocalLow\\Innersloth\\Among Us\\settings.amogus", "r") as file:
            return decode(json.loads(file.read())["multiplayer"]["normalHostOptions"])
#    def comp(a: list, b: list):
#        if a == b:
#            print("Both saves are the same")
#            return
#        else:
#            return [i for i, v in enumerate(a) if a[i] != b[i]]
    corepresets = {
        "coresettings": {
            "name": f"{hl('Core Settings', 255, 255, 255)}",
            "type": f"{hl('[Innersloth]', 255, 255, 0)}",
            "data": "CoQAAAEAAA8AAQAAAAAAgD8AAIA/AADAPwAANEIBAQIBAAAAAQEPAAAAeAAAAAAAAQEAAAAJBQAAAAMAAAAKHgIAAAACAAAPBQQAAAADAAA8CgADAAAAAgAAHg8IAAAAAgAACgEJAAAAAgAADx4KAAAAAwAADx4BDAAAAAEAAAMSAAAAAQAADw=="
        },
        "rolesgalore": {
            "name": f"{hl('Roles Galore', 255, 255, 255)}",
            "type": f"{hl('[Innersloth]', 255, 255, 0)}",
            "data":  "CoQAAAEAAQ8AAQAAAAAAgD8AAIA/AADAPwAANEIBAQIBAAAAAQEPAAAAeAAAAAAAAQEAAAAJBQABZAMAAAAKHgIAAWQCAAAPBQQAAWQDAAA8CgADAAFkAgAAHg8IAAFkAgAACgEJAAFkAgAADx4KAAFkAwAADx4BDAABZAEAAAMSAAFkAQAADw=="
        },
        "nokillcooldown": {
            "name": f"{hl('No Kill Cooldown', 255, 0, 0)}",
            "type": f"{hl('[Built-in]', 255, 255, 255)}",
            "data": "CoQAAAEAAA8AAQAAAAAAwD8AAIA/AADAPwAAAAABAQIBAAAAAQAPAAAAeAAAAAAAAQEAAAAJBQAAAAMAAAAKHgIAAAACAAAPBQQAAAADAAA8CgADAA9kAgAAAAAIAAAAAgAACgEJAAAAAgAADx4KAAAAAwAADx4BDAAAAAEAAAMSAAFkAQAAAA=="
        },
#        "debug": {
#            "name": "debug",
#            "type": f"{hl('[Built-in]', 255, 255, 255)}",
#            "data": "CoQAAAEAAA8AAQAAAAAAgD8AAIA/AAAgQQAAlkP/AAABAAAAAQIeAAAAHgAAAAAAAQAAAAAJBQAAAAMAAAAKHgIAAAACAAAPBQQAAWQDAACWPAADAAAAAgAAHg8IAAAAAgAACgEJAAAAAgAADx4KAAAAAwAADx4BDAAAAAEAAAMSAAFkAQAAAA=="
#        }
    }
    presets = {}
    clamp = lambda x, y, z: max(min(x, z), y)
    def refreshconfig():
        global presets
        presets = dict(corepresets)
        with open("\\".join(__file__.split("\\")[:-1])+"\\config.json", "r") as file:
            data = json.loads(file.read())["presets"]
            for k in data.keys():
                v = data[k]
                presets[k] = {"name": f"{v['name']}", "type": f"{hl('[Custom]', 0, 255, 0)}", "data": v["data"]}
    def addpreset(key: str, value: str):
        print(f"{hl('The following step requires colorama to view its effects.', 255, 200, 0)}")
        colour = input(f"{hl('Input custom preset colour. (r, g, b) > ', 0, 255, 0)}").replace(" ","").split(",")
        if len(colour) != 3:
            return print(f"{hl('Invalid RGB value.', 255, 0, 0)}")
        r, g, b = [clamp(int(n), 0, 255) for n in colour][0:3]
        with open("\\".join(__file__.split("\\")[:-1])+"\\config.json", "r") as file:
            data = json.loads(file.read())
        data["presets"][key.lower().replace(" ","")] = {
            "name": f"{hl(key, r, g, b)}",
            "data": value
        }
        with open("\\".join(__file__.split("\\")[:-1])+"\\config.json", "w") as file:
            try:
                json.dump(data, file)
            except:
                print(f"{hl('Something went wrong with exporting your preset. Loading backup...', 255, 0, 0)}")
                with open("\\".join(__file__.split("\\")[:-1])+"\\backup.json", "r") as file1:
                    with open("\\".join(__file__.split("\\")[:-1])+"\\config.json", "w") as file2:
                        file2.write(file1.read())
            else:
                print(f"{hl('Exported preset.', 0, 255, 0)}")
                with open("\\".join(__file__.split("\\")[:-1])+"\\backup.json", "w") as file:
                    json.dump(data, file)
    key = {
        "players": [7],
        "map": [12],
        "playerspeed": [15, 17],
        "crewmatevision": [19,21],
        "impostorvision": [23,25],
        "killcooldown": [27,29],
        "commontasks": [29],
        "shorttasks": [30],
        "longtasks": [31],
        "emergencymeetings": [32],
        "impostors": [36],
        "killdistance": [37],
        "discussiontime": [38],
        "votingtime": [42],
        "emergencycooldown": [47],
        "confirmejects": [48],
        "visualtasks": [49],
        "anonymousvotes": [50],
        "taskbarupdates": [51],
        "shapeshifters": [56],
        "shapeshifterodds": [57],
        "leaveshapeshiftingevidence": [61],
        "shapeshiftcooldown": [62],
        "shapeshiftduration": [63],
        "scientists": [66],
        "scientistodds": [67],
        "vitalsdisplaycooldown": [72],
        "batteryduration": [73],
        "guardianangels": [75],
        "guardianangelodds": [76],
        "protectcooldown": [80],
        "protectduration": [81],
        "protectvisibletoimpostors": [82],
        "engineers": [85],
        "engineerodds": [86],
        "ventcooldown": [90],
        "ventduration": [91],
        "noisemakers": [94],
        "noisemakerodds": [95],
        "impostorsgetalert": [98],
        "alertduration": [99],
        "phantoms": [103],
        "phantomodds": [104],
        "vanishcooldown": [108],
        "vanishduration": [109],
        "trackers": [112],
        "trackerodds": [113],
        "trackingcooldown": [117],
        "trackingduration": [118],
        "trackingdelay": [119],
        "detectives": [122],
        "detectiveodds": [123],
        "suspectspercase": [127],
        "vipers": [130],
        "viperodds": [131],
        "dissolvetime": [135]
    }

    def getshortkey(index: str):
        return data[key[index][0]:key[index][1]]

    maps=[f"{hl('The skeld', 255, 255, 255)}  ", f"{hl('Mira HQ', 255, 255, 255)}    ", f"{hl('Polus', 255, 255, 255)}      ", f"{hl('The airship', 255, 255, 255)}", f"{hl('The fungle', 255, 255, 255)} "]
    distances=[f"{hl('Short', 127, 255, 0)} ", f"{hl('Medium', 255, 255, 0)}", f"{hl('Long', 255, 127, 0)}  "]
    booleans=[f"{hl('False', 255, 0, 0)}", f"{hl('True', 0, 255, 0)} "]
    taskbarupdates=[f"{hl('Always', 0, 255, 0)}  ", f"{hl('Meetings', 255, 255, 0)}", f"{hl('Never', 255, 0, 0)}   "]

    def display(data: list):
        return f'''┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                      == normalHostOptions ==                                     │
├────────────────────────────┬───────────────────────────────┬─────────────────────────────────────┤
│ Players: {intpad(data[key['players'][0]], 3)}               │ Engineers: {pad(data[key['engineers'][0]], 3)}                │ Guardian angels: {pad(data[key['guardianangels'][0]], 3)}                │
│ Map: {maps[data[key['map'][0]]]}           │ Engineer odds: {oddspad(data[key['engineerodds'][0]])}           │ Guardian angel odds: {oddspad(data[key['guardianangelodds'][0]])}           │
│ Impostors: {pad(data[key['impostors'][0]], 3)}             │ Vent cooldown: {intpad(data[key['ventcooldown'][0]], 4, "s")}           │ Protect cooldown: {intpad(data[key['protectcooldown'][0]], 4, "s")}              │
│ Kill cooldown: {floatpad(to_float(getshortkey('killcooldown')), 's')}    │ Vent duration: {rolepad(data[key['ventduration'][0]], "s")}           │ Protect duration: {intpad(data[key['protectduration'][0]], 4, "s")}              │
│ Impostor vision: {floatpad(to_float(getshortkey('impostorvision')), 'x')}  │ Scientists: {pad(data[key['scientists'][0]], 3)}               │ Protect visible to impostors: {booleans[data[key['protectvisibletoimpostors'][0]]]} │
│ Kill distance: {distances[data[key['killdistance'][0]]]}      │ Scientist odds: {oddspad(data[key['scientistodds'][0]])}          │                                     │
│ Player speed: {floatpad(to_float(getshortkey('playerspeed')), 'x')}     │ Vitals display cooldown: {intpad(data[key['vitalsdisplaycooldown'][0]], 4, "s")} │ Shapeshifters: {pad(data[key['shapeshifters'][0]], 3)}                  │
│ Crewmate vision: {floatpad(to_float(getshortkey('crewmatevision')), 'x')}  │ Battery duration: {intpad(data[key['batteryduration'][0]], 4, "s")}        │ Shapeshifter Odds: {oddspad(data[key['shapeshifterodds'][0]])}             │
│                            │ Trackers: {pad(data[key['trackers'][0]], 3)}                 │ Shapeshift cooldown: {intpad(data[key['shapeshiftcooldown'][0]], 4, "s")}           │
│ Emergency meetings: {pad(data[key['emergencymeetings'][0]], 3)}    │ Tracker odds: {oddspad(data[key['trackerodds'][0]])}            │ Shapeshift duration: {rolepad(data[key['shapeshiftduration'][0]], "s")}           │
│ Emergency cooldown: {intpad(data[key['emergencycooldown'][0]], 4, "s")}   │ Tracking cooldown: {intpad(data[key['trackingcooldown'][0]], 4, "s")}       │ Leave shapeshifting evidence: {booleans[data[key['leaveshapeshiftingevidence'][0]]]} │
│ Discussion time: {intpad(data[key['discussiontime'][0]], 4, "s")}      │ Tracking delay: {intpad(data[key['trackingdelay'][0]], 4, "s")}          │                                     │
│ Voting time {intpad(data[key['votingtime'][0]], 4, "s")}           │ Tracking duration: {intpad(data[key['trackingduration'][0]], 4, "s")}       │ Phantoms: {pad(data[key['phantoms'][0]], 3)}                       │
│ Anonymous votes: {booleans[data[key['anonymousvotes'][0]]]}     │ Noisemakers: {pad(data[key['noisemakers'][0]], 3)}              │ Phantom odds: {oddspad(data[key['phantomodds'][0]])}                  │
│ Confirm ejects: {booleans[data[key['confirmejects'][0]]]}      │ Noisemaker odds: {oddspad(data[key['noisemakerodds'][0]])}         │ Vanish cooldown: {intpad(data[key['vanishcooldown'][0]], 4, "s")}               │
│ Task bar updates: {taskbarupdates[data[key['taskbarupdates'][0]]]} │ Alert duration: {intpad(data[key['alertduration'][0]], 4, "s")}          │ Vanish duration: {intpad(data[key['vanishduration'][0]], 4, "s")}               │
│ Common tasks: {pad(data[key['commontasks'][0]], 3)}          │ Impostors get alert: {booleans[data[key['impostorsgetalert'][0]]]}    │                                     │
│ Long tasks: {pad(data[key['longtasks'][0]], 3)}            │ Detectives: {pad(data[key['detectives'][0]], 3)}               │ Vipers: {pad(data[key['vipers'][0]], 3)}                         │
│ Short tasks: {pad(data[key['shorttasks'][0]], 3)}           │ Detective odds: {oddspad(data[key['detectiveodds'][0]])}          │ Viper odds: {oddspad(data[key['viperodds'][0]])}                    │
│ Visual tasks: {booleans[data[key['visualtasks'][0]]]}        │ Suspects per case: {pad(data[key['suspectspercase'][0]], 3)}        │ Dissolve time: {intpad(data[key['dissolvetime'][0]], 4, "s")}                 │
└────────────────────────────┴───────────────────────────────┴─────────────────────────────────────┘'''

    print(f"{hl('Make sure Among us is closed before modifying your host options.', 255, 200, 0)}")
    input(f"{hl('| [ENTER] to proceed |', 255, 255, 255)} ")
    data = load()
    print('Input' + hl(" 'help' ", 0, 255, 0) + 'for a list of commands.')
    print(f"{display(data)}\nCurrent save code: {encode(data)}")
    while True:
        action = input("> ").lower().split(" ")
        if action[0] == "help":
            print('''== Among us host options editor - Commands ==
help - Shows this list.
display - Show the current settings.
get <setting> - View the value of one of the settings.
set <setting> <value(s)> - Change the value of one of the settings.
bset <setting> <byte(s)> - Change the value of one of the settings, using the byte values.
save - Saves the currently stored data to the settings file.
load - Load from a preset.
presets - View list of presets.
preview <preset> - View the settings of a preset.
export - Create a new preset.''')
        elif action[0] == "display":
            print(f"{display(data)}\nCurrent save code: {encode(data)}")
        elif action[0] == "get":
            action[1] = (''.join(action[1:])).lower()
            a = data[slice(key[action[1]][0],(key[action[1]][-1] if key[action[1]][-1] != key[action[1]][0] else key[action[1]][-1]+1),1)]
            if len(a) == 1:
                print(f"{action[1]}={a[0]}")
            else:
                print(f"{action[1]}={a}")
        elif action[0] == "bset":
            action[2] = " ".join(action[2:])
            if len(key[action[1]]) == 1:
                if cast(action[2]) > 255:
                    print("Input value must not be greater than 255.")
                elif cast(action[2]) < 0:
                    print("Input value must not be less than 0.")
                else:
                    data[key[action[1]][0]] = cast(action[2])
                    print(f"Byte {key[action[1]][0]} set to [{cast(action[2])}]")
            elif len(key[action[1]]) == 2:
                action[2:] = [int(k) for k in action[2].split(" ")]
                destination = key[action[1]]
                valid = True
                if cast(action[2]) > 255:
                    print("Input value 1 must not be greater than 255.")
                    valid = False
                elif cast(action[2]) < 0:
                    print("Input value 1 must not be less than 0.")
                    valid = False
                if cast(action[3]) > 255:
                    print("Input value 2 must not be greater than 255.")
                    valid = False
                elif cast(action[3]) < 0:
                    print("Input value 2 must not be less than 0.")
                    valid = False
                if valid == True:
                    data[slice(destination[0],destination[1],1)] = [action[2], action[3]]
                    print(f"Bytes [{destination[0]}:{destination[1]}] set to [{action[2]}, {action[3]}]")
            print(f"{display(data)}\nCurrent save code: {encode(data)}")
        elif action[0] == "set":
            if action[1] in ["playerspeed", "crewmatevision", "impostorvision", "killcooldown"]:
                action[2:] = to_sus(action[2])
                destination = key[action[1]]
                valid = True
                if cast(action[2]) > 255:
                    print("Input value 1 must not be greater than 255.")
                    valid = False
                elif cast(action[2]) < 0:
                    print("Input value 1 must not be less than 0.")
                    valid = False
                if cast(action[3]) > 255:
                    print("Input value 2 must not be greater than 255.")
                    valid = False
                elif cast(action[3]) < 0:
                    print("Input value 2 must not be less than 0.")
                    valid = False
                if valid == True:
                    data[slice(destination[0],destination[1],1)] = [action[2], action[3]]
                    print(f"Bytes [{destination[0]}:{destination[1]}] set to [{action[2]}, {action[3]}]")
            else:
                if cast(action[2]) > 255:
                    print("Input value must not be greater than 255.")
                elif cast(action[2]) < 0:
                    print("Input value must not be less than 0.")
                else:
                    data[key[action[1]][0]] = cast(action[2])
                    print(f"Byte {key[action[1]][0]} set to [{cast(action[2])}]")
            print(f"{display(data)}\nCurrent save code: {encode(data)}")
        elif action[0] == "save":
            print(f"{hl('Make sure Among us is closed before modifying your host options.', 255, 200, 0)}")
            input(f"{hl('| [ENTER] to save |', 255, 255, 255)} ")
            if any([not (0.5 <= to_float(getshortkey("playerspeed")) <= 3), not (1 <= data[key["impostors"][0]] <= 3)]):
                print(f"{hl('These settings are outside the allowed online play limits. This will cause unstable behaviour.', 255, 0, 255)}")
                if cast(input(f"{hl('Proceed anyway? (Y/n) > ', 255, 0, 255)}").lower().replace(" ","")) == 0:
                    continue
            print(f"{hl('Saving...', 255, 200, 0)}")
            with open(f"{os.path.expanduser('~')}\\AppData\\LocalLow\\Innersloth\\Among Us\\settings.amogus", "r") as file:
                output = json.loads(file.read())
                output["multiplayer"]["normalHostOptions"] = encode(data)
            with open(f"{os.path.expanduser('~')}\\AppData\\LocalLow\\Innersloth\\Among Us\\settings.amogus", "w") as file:
                try:
                    json.dump(output, file)
                    print(f"{hl('Saved.', 0, 255, 0)}")
                except:
                    print(f"{hl('Something went wrong while saving. Loading backup...', 255, 0, 0)}")
                    with open(f"{os.path.expanduser('~')}\\AppData\\LocalLow\\Innersloth\\Among Us\\settings.amogus", "w") as file1:
                        with open(parent+"\\settings.amogus", "r") as file2:
                            data = json.loads(file2.read())
                        json.dump(data, file1)
                else:
                    with open(parent+"\\settings.amogus", "w") as file1:
                        with open(f"{os.path.expanduser('~')}\\AppData\\LocalLow\\Innersloth\\Among Us\\settings.amogus", "r") as file2:
                            file1.write(file2.read())
        elif action[0] == "load":
            refreshconfig()
            preset = "".join(action[1:])
            if preset in list(presets.keys()):
                data = decode(presets[preset]["data"])
                print(f"Loaded the [{presets[preset]['name']}] preset.")
                print(f"{display(data)}\nCurrent save code: {encode(data)}")
            else:
                print(f"Invalid preset. Available presets: \n{'\n'.join([f'{presets[k]['name']} {presets[k]['type']}' for k in presets])}")
        elif action[0] == "export":
            print(f"{display(data)}\nPreset save code: {encode(data)}")
            name = input(f"{hl('Choose a name for your custom preset > ', 0, 255, 0)}")
            refreshconfig()
            if name.lower().replace(" ","") in presets.keys():
                action = input(f"{hl('This preset name already exists. Overwrite? (Y/n) > ', 255, 120, 0)}")
                if booleans[cast(action)] == booleans[cast("True")]:
                    if name.lower().replace(" ","") in corepresets.keys():
                        print(corepresets.keys())
                        print(f"{hl('Core presets cannot be overwritten. You must choose another name.', 255, 0, 0)}")
                    else:
                        addpreset(name, encode(data))
                else:
                    addpreset(name, encode(data))
            else:
                addpreset(name, encode(data))
        elif action[0] == "preview":
            refreshconfig()
            preset = "".join(action[1:])
            if preset in list(presets.keys()):
                data = decode(presets[preset]["data"])
                print(f"{display(data)}\nPreset save code: {encode(data)}")
        elif action[0] == "presets":
            refreshconfig()
            print(f"Available presets: \n{'\n'.join([f'{presets[k]['name']} {presets[k]['type']}' for k in presets])}")
        else:
            print("Invalid command. Input 'help' for a list of commands.")
