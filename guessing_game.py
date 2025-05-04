# משחק ניחושים
# תאריך: 26-01-2025

import random

def play_guessing_game():
    """מריץ משחק ניחושים חדש."""
    random_number = random.randint(1, 20)
    attempts = 0
    max_attempts = 5
    guessed_correctly = False

    print("אני חושב על מספר בין 1 ל-20. נסה לנחש!")

    while attempts < max_attempts and not guessed_correctly:
        try:
            guess = int(input(f"ניסיון {attempts + 1}/{max_attempts}: הכנס ניחוש: "))
            attempts += 1

            if guess < random_number:
                print("נמוך מדי!")
            elif guess > random_number:
                print("גבוה מדי!")
            elif guess == random_number:
                print(f"נכון! ניחשת נכון תוך {attempts} ניסיונות!")
                guessed_correctly = True
            else:
                print("קלט לא תקין. אנא הכנס מספר.")

        except ValueError:
            print("קלט לא תקין. אנא הכנס מספר שלם.")

    if not guessed_correctly:
        print(f"המשחק נגמר! המספר הנכון היה {random_number}.")

if __name__ == "__main__":
    while True:
        play_guessing_game()
        play_again = input("האם תרצה לשחק שוב? (כן/לא): ").lower()
        if play_again != "כן":
            break
    print("תודה ששיחקת!")