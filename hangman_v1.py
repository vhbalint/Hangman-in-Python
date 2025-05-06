import random
import os
import sys
import time

def get_data():
    f = open("countries-and-capitals.txt", "r")
    content = f.read()
    lines = content.split("\n")
    dictionary = {}
    for item in lines:
        a = item.split(" | ")
        dictionary[a[0]] = a[1]
    return dictionary


#words = country.replace(" ","")

def medium_diff():
    x = get_data()
    country = random.choice(list(x.keys()))
    global words
    words = country

def hard_diff():
    x = get_data()
    capital = random.choice(list(x.values()))
    global words
    words = capital

def animated_print(text):
    for item in text:
        sys.stdout.write(item)
        sys.stdout.flush()
        time.sleep(0.2)

hangman_art = {0:("__________ ",
                  " | /    |  ",
                  " |/        ",
                  " |         ",
                  " |         ",
                  " |         ",
                  " |         ",
                  "========== ",
                  "/        \\"),
               1:("__________ ",
                  " | /    |  ",
                  " |/     O  ",
                  " |         ",
                  " |         ",
                  " |         ",
                  " |         ",
                  "========== ",
                  "/        \\"),
               2:("__________ ",
                  " | /    |  ",
                  " |/     O  ",
                  " |      |  ",
                  " |         ",
                  " |         ",
                  " |         ",
                  "========== ",
                  "/        \\"),
               3:("__________ ",
                  " | /    |  ",
                  " |/     O  ",
                  " |     /| ",
                  " |         ",
                  " |         ",
                  " |         ",
                  "========== ",
                  "/        \\"),
               4:("__________ ",
                  " | /    |  ",
                  " |/     O  ",
                  " |     /|\\",
                  " |      |  ",
                  " |         ",
                  " |         ",
                  "========== ",
                  "/        \\"),
               5:("__________ ",
                  " | /    |  ",
                  " |/     O  ",
                  " |     /|\\",
                  " |      |  ",
                  " |     /   ",
                  " |         ",
                  "========== ",
                  "/        \\"),
               6:("__________ ",
                  " | /    |  ",
                  " |/     O     ___                   ___                     ",
                  " |     /|\\   / __|__ _ _ __  ___   / _ \\__ _____ _ _      ",
                  " |      |   | (_ / _` | '  \\/ -_) | (_) \\ V / -_) '_|     ",
                  " |     / \\   \\___\\__,_|_|_|_\\___|  \\___/ \\_/\\___|_|  ",
                  " |         ",
                  "========== ",
                  "/        \\")}

def display_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("\n")

def display_hint(hint):
    print("".join(hint))

def display_answear(answear):
    print("".join(answear))

def play():
    os.system("cls")
    answear = "".join(words.lower())
    hint = ["_"] * len(answear)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            os.system("cls")
            print("Invalid answear, try again!")
            continue

        if guess in guessed_letters:
            os.system("cls")
            print(f"{guess} is already guessed, try again!")
            continue
        
        guessed_letters.add(guess)
        
        if guess in answear:
            for index in range(len(answear)):
                if answear[index] == guess:
                    hint[index] = guess

        else:
            wrong_guesses += 1

        if "_" not in hint:
            os.system("cls")
            display_man(wrong_guesses)
            display_answear(answear)
            print("CONGRATUALTION! YOU WIN!")
            selected = input("Return to MAIN MENU? (y/n): ")
            if selected == "y":
                menu()
            if selected == "n":
                quit()
        
        elif wrong_guesses >= len(hangman_art) - 1:
            os.system("cls")
            display_man(wrong_guesses)
            display_answear(answear)
            print("YOU LOSE!")
            selected = input("Return to MAIN MENU? (y/n): ")
            if selected == "y":
                menu()
            if selected == "n":
                quit()

        os.system("cls")

def difficulty():
      os.system("cls")
      print(" ___ ___ ___ ___ ___ ___ _   _ _  _______   __")
      print("|   \_ _| __| __|_ _/ __| | | | ||_   _\ \ / /")
      print("| |) | || _|| _| | | (__| |_| | |__| |  \ V / ")
      print("|___/___|_| |_| |___\___|\___/|____|_|   |_| ")
      print("\n")
      print("MODERATE - COUNTRIES - press M\nHARD - CAPITALS - press h\nBACK TO THE MAIN MENU - press b\n")
      selected = input("Choose: ")
      if selected.lower() == "m":
          medium_diff()
          menu()
          
      if selected.lower() == "h":
          hard_diff()
          menu()

      if selected.lower() == "b":
          menu()                                      

def menu():
    os.system("cls")
    print(" __  __ ___ _  _ _   _ ")
    print("|  \/  | __| \| | | | |")
    print("| |\/| | _|| .` | |_| |")
    print("|_|  |_|___|_|\_|\___/ ")
    print("\n")
    print ("PLAY - press p\nDIFFICULTY - press d\nEXIT - press e")
    selected = input("Choose: ")
    if selected.lower() == "p":
        play()
    if selected.lower() == "d":
        difficulty()
    if selected.lower() == "e":
        os.system("cls")
        animated_print("GOOD BYE!")
        time.sleep(2)
        quit()

if True:
    menu()