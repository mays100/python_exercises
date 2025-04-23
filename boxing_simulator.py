import random

# הגדרת מהלכי איגרוף ומספרים מייצגים
MOVES = {
    1: "Jab",
    2: "Cross",
    3: "Hook",
    4: "Uppercut"
}

# הגדרת חוקי ניצחון (ודא שכל מהלך מנצח ומפסיד)
WIN_RULES = {
    1: 3,  # Jab מנצח Hook
    2: 1,  # Cross מנצח Jab
    3: 4,  # Hook מנצח Uppercut
    4: 2   # Uppercut מנצח Cross
}

def simulate_round():
    """מדמה סיבוב איגרוף אחד."""
    while True:
        try:
            user_choice = int(input("בחר מהלך (1: Jab, 2: Cross, 3: Hook, 4: Uppercut): "))
            if 1 <= user_choice <= 4:
                break
            else:
                print("בחירה לא חוקית. אנא בחר מספר בין 1 ל-4.")
        except ValueError:
            print("קלט לא חוקי. אנא הזן מספר.")

    opponent_choice = random.randint(1, 4)

    user_move = MOVES[user_choice]
    opponent_move = MOVES[opponent_choice]

    print(f"\nאתה בחרת: {user_move}")
    print(f"היריב בחר: {opponent_move}")

    if user_choice == opponent_choice:
        print("תיקו בסיבוב!")
    elif opponent_choice == WIN_RULES.get(user_choice):
        print("ניצחת בסיבוב הזה!")
    else:
        print("היריב ניצח בסיבוב הזה.")

if __name__ == "__main__":
    simulate_round()