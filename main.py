import sys
import os

from json import dumps, loads
from termcolor import cprint, colored
from simple_term_menu import TerminalMenu
from typing import Union, List, Dict, Optional

__repo__ = "https://github.com/Zidaan-Hayat/Noter"
__project__ = "Noter"
__author__ = "Zidaan Hayat"
__email__ = "doczidaan@gmail.com"
__copyright__ = "Copyright © 2020 Zidaan Hayat. All rights reserved"
__version__ = '1.0.0r' # Release version 1

store_file = 'store_notes.json'

def leave():
    sys.exit()

def _get_all_notes() -> Union[Dict[str,str], List[str], None]:
    with open(store_file, 'r') as f:
        data = loads(f.read())

        return data

def _remove_note(key: str) -> Optional[bool]:
    data = _get_all_notes()

    try:
        data[key]
    except:
        return None
    
    del data[key]

    with open(store_file, 'w') as f:
        f.write(dumps(data))

        return True
    
    return False

def _add_note(notes_data: Optional[Dict[str,str]]) -> Optional[bool]:
    if not notes_data:
        return False

    data = _get_all_notes()

    data[notes_data['title']] = notes_data['notes']

    with open(store_file, 'w') as f:
        f.write(dumps(data))
    
        return True
    
    return False

def remove_note():
    key = input("Which note should I remove?: ")

    do = _remove_note(key)

    if not do:
        print("Note was not found.")
    else:
        print("Note was removed.")

def add_note() -> Optional[bool]:
    title = input("What should these notes be labelled as?: ")

    notes = []
    given = ""

    print('You may start typing your notes. Type "COMPLETED" when complete.')

    while given != "COMPLETED":
            given = input()
            if given != "COMPLETED":
                notes.append(given)
        
    n = "\n"

    adding = _add_note({"title": title, "notes": n.join(notes)})

    if adding:
        print(f"Note {title} added.")
    else:
        print("Error")

def main():
    current_notes = _get_all_notes()
    
    def view_note(key: str): print("{0}: {1}".format(key,current_notes[key]))

    options = {}

    for k in list(current_notes.keys()):
        options[k] = view_note

    options["New Note"] = add_note
    options["Delete Note"] = remove_note
    options["Exit"] = leave

    choices: list = list(options.keys())

    menu = TerminalMenu(choices,title=colored('Notes (↑/↓)',color='blue'))

    choice = menu.show()
    choice = choices[choice]

    os.system('clear')

    if choice not in list(current_notes.keys()):
        options[choice]()
    else:
        options[choice](key=choice)

if __name__ == "__main__":
    while True:
        main()