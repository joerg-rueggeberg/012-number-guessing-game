# REPLIT VERSION
from replit import clear
from art import logo
from random import randint


def difficulty():
    diff = input("Wähle einen Schwierigkeitsgrad: 'leicht' oder 'schwer': ")
    if diff == "leicht":
        return 10
    elif diff == "schwer":
        return 5
    else:
        guess()


def guess():
    goal = randint(1, 100)
    end = False

    print(logo)
    print("Willkommen zum Zahlenratespiel!")
    print("Ich denke an eine Zahl zwischen 1 und 100.\n")

    counter = difficulty()

    while not end and counter > 0:
        num = int(input(f"Du hast noch <{counter}> Versuche. Tippe eine Zahl von 1 bis 100: "))
        if num == goal:
            print(f"\nKorrekt! Die gesuchte Zahl war: <{goal}> - Du hast gewonnen!")
            end = True
        elif num > goal:
            counter -= 1
            print(f"Zu Groß!")
        elif num < goal:
            counter -= 1
            print(f"Zu klein!")
        else:
            print(f"Falsche Eingabe!")
    if counter == 0:
        print(f"Du hast keine Versuche mehr übrig. Die gesuchte Zahl war: <{goal}> Leider verloren!")
    con = input("\nMöchtest du noch einmal spielen? j/n: ").lower()
    if con == "j":
        goal = randint(1, 100)
        clear()
        guess()
    print("\nDanke, dass du 'Guess the Number' gespielt hast!")


guess()
