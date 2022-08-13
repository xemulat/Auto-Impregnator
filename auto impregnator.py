from ctypes import string_at
from os import system
from urllib.request import urlopen, urlretrieve
from time import sleep
from sys import exit
from colorama import init, Fore
from lastversion import latest, has_update

init(autoreset=True)

system('cls')
print(Fore.RED + "Launching Semen Deamon...")
sleep(6)
print(Fore.RED + "Semen Deamon Started!")
print("                _                   _____                                            _       \n"      
      "     /\        | |                 |_   _|                                          | |            \n"
      "    /  \  _   _| |_ ___    ______    | |  _ __ ___  _ __  _ __ ___  __ _ _ __   __ _| |_ ___  _ __ \n"
      "   / /\ \| | | | __/ _ \  |______|   | | | '_ ` _ \| '_ \| '__/ _ \/ _` | '_ \ / _` | __/ _ \| '__|\n"
      "  / ____ \ |_| | || (_) |           _| |_| | | | | | |_) | | |  __/ (_| | | | | (_| | || (_) | |   \n"
      " /_/    \_\__,_|\__\___/           |_____|_| |_| |_| .__/|_|  \___|\__, |_| |_|\__,_|\__\___/|_|   \n"
      "                                                   | |              __/ |                          \n"
      "                                                   |_|             |___/                           \n")

print(Fore.RED + "CumCord Semi-Auto-Installer, written by Xemulated")
print(Fore.BLUE + "What mod you have:\n"
                   "1. Goosemod\n"
                   "2. BetterDiscord\n"
                   "3. No Mods\n"
                   "99. Exit")
whatmod = input("Responce: ")

if whatmod == '1':
    system('cls')
    print(Fore.CYAN + "Follow these steps:\n"
          "1. Go to Plugins tab in GooseMod\n"
          "2. Click on the cloud icon\n"
          "3. Paste this into the URL bar\n"
          "https://goose.lexisother.tk/nova.json\n"
          "4. Click 'ADD'\n"
          "5. Click Yes on the Popup\n"
          "6. Click the refresh button\n"
          "7. Click CTRL + R to refresh discord\n"
          "8. Search and install CumcordLoader in the Plugins Tab\n",
          "Done!")
    input("Click ENTER when you are done: ")
    exit(sleep(3))

if whatmod == '2':
    print("Downloading CumcordLoader...")
    urlretrieve("https://raw.githubusercontent.com/CumcordLoaders/BetterDiscord/master/CumcordLoader.plugin.js", "CumcordLoader.plugin.js")
    print("1. Drag-And-Drop the downloaded CumcordLoader.plugin.js file into your plugin folder.\n"
          "2. Press CTRL + R to restart")
    
    input("Click ENTER when you are done: ")
    exit(sleep(3))
    
if whatmod == '3':
    print("Downloading impregnator...")
    newestversion = latest(repo='Cumcord/Impregnate', output_format='version')
    urlretrieve("https://github.com/Cumcord/Impregnate/releases/download/v" + str(newestversion) + "/impregnate.exe", "CumInjector.exe")
    print("Launching Cum Injector...")
    print("Now install CumCord")
    system("CumInjector.exe")

if whatmod == '69':
    print("    __ ___  ")
    print("   / // _ \ ")
    print("  / /| (_) |")
    print(" | '_ \__, |")
    print(" | (_) |/ / ")
    print("  \___//_/  ")
    print("Nice")
    exit(sleep(6))

if whatmod == '99':
    exit(sleep(3))