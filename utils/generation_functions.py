import random
import string
import subprocess
import platform
from utils.ascii_menu import raccoon_ascii, menu_ascii

def center():
    for _ in range(4):
        print("\n")

def clear_screen():
    system = platform.system()
    command = 'cls' if system == 'Windows' else 'clear'
    subprocess.run(command, shell=True)
    center()

def print_menu():
    print(raccoon_ascii)
    print(menu_ascii)


def get_nb_characters() -> int:
    while True:
        clear_screen()
        nb_characters = 14
        print("Password length? (14 to 20 characters)")
        try:
            nb_characters=int(input())
        except ValueError:
            clear_screen()
            print("Wrong input, type a number")
            input("(Press Enter to continue)")
            continue
        if nb_characters == 22:
            return 22
        elif nb_characters < 14 or nb_characters>20:
            clear_screen()
            print("Wrong length, choose from 14 to 20 characters")
            input("(Press Enter to continue)")
            continue
        elif nb_characters >= 14 and nb_characters<=20:
            return nb_characters


def get_nb_specials(nb_characters: int) -> int:
    while True:
        clear_screen()
        nb_specials = 4
        print("How many special characters? (min 4)")
        try:
            nb_specials=int(input())
        except ValueError:
            clear_screen()
            print("Wrong input, type a number")
            input("(Press Enter to continue)")
            continue
        if nb_specials > nb_characters or nb_specials < 4:
            clear_screen()
            print("Wrong number, min 4 special characters.")
            input("(Press Enter to continue)")
            continue
        elif nb_specials >=4 and nb_specials <= nb_characters-nb_specials-5:
            return nb_specials

def get_nb_upper_letters(nb_characters: int, nb_specials: int) -> int:
    while True:
        clear_screen()
        nb_upper_letters = 3
        print("How many upper letters? (min 3)")
        try: 
            nb_upper_letters =int(input())
        except ValueError:
            clear_screen()
            print("Wrong input, type a number")
            input("(Press Enter to continue)")
        if nb_upper_letters > nb_characters or nb_upper_letters < 3:
            clear_screen()
            print("Wrong number of upper letters,  min 3 upper letters.")
            input("(Press Enter to continue)")
            continue
        elif nb_upper_letters < nb_characters - nb_specials - 3:
            return nb_upper_letters

def get_nb_numbers(nb_characters: int, nb_specials: int, nb_upper_letters: int) -> int:
    while True:
        clear_screen()
        print("How many numbers? (min 3)")
        try: 
            nb_numbers =int(input())
        except ValueError:
            clear_screen()
            print("Wrong input, type a number")
            input("(Press Enter to continue)")
        if nb_numbers > nb_characters or nb_numbers < 3:
            clear_screen()
            print("Wrong number numbers, min 3 numbers.")
            input("(Press Enter to continue)")
            continue
        elif nb_numbers < nb_characters - nb_specials - nb_upper_letters:
            return nb_numbers

def generate_password() -> str:

    clear_screen()

    print_menu()
    
    print("")
    goOrNot = input()

    if goOrNot == "go" or goOrNot == "GO":

        nb_characters = 18
        
        nb_specials = 5
    
        nb_upper_letters = 4
    
        nb_numbers = 4
    
        full_password = ""

        special_letters=["&", "#", "*", "%", "$", "^"]
        upper_letters = list(string.ascii_uppercase)
        other_letters = list(string.ascii_lowercase)
        numbers = list(string.digits) 
    
        password_list = []
        
        for _ in range(nb_specials):
            password_list.append(random.choice(special_letters))
            
        for _ in range(nb_upper_letters):
            password_list.append(random.choice(upper_letters))
    
        for _ in range(nb_numbers):
            password_list.append(random.choice(numbers))
            
        remaining = nb_characters - len(password_list)
        for _ in range(remaining):
            password_list.append(random.choice(other_letters))
            
        random.shuffle(password_list)
        
        full_password = "".join(password_list)
        print(f"Password: " + full_password)
        input()
        return()

    elif goOrNot != "go" or goOrNot!="GO": 

        nb_characters = get_nb_characters()

        nb_specials = get_nb_specials(nb_characters)

        nb_upper_letters = get_nb_upper_letters(nb_characters, nb_specials)

        nb_numbers = get_nb_numbers(nb_characters, nb_specials, nb_upper_letters)

        full_password = ""

        special_letters=["&", "#", "*", "%", "$", "^"]
        upper_letters = list(string.ascii_uppercase)
        other_letters = list(string.ascii_lowercase)
        numbers = list(string.digits) 


        password_list = []
        
        for _ in range(nb_specials):
            password_list.append(random.choice(special_letters))
            
        for _ in range(nb_upper_letters):
            password_list.append(random.choice(upper_letters))

        for _ in range(nb_numbers):
            password_list.append(random.choice(numbers))
            
        remaining = nb_characters - len(password_list)
        for _ in range(remaining):
            password_list.append(random.choice(other_letters))
            
        random.shuffle(password_list)
        
        full_password = "".join(password_list)
        print(f"Password: " + full_password)
        input("(Press Enter to continue)")
