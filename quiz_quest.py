import random

# 2. Define the question bank
questions = {
    "מדע": [
        {"q": "מהי נוסחת המים?", "a": "H2O"},
        {"q": "מי גילה את חוקי התנועה?", "a": "אייזק ניוטון"},
        {"q": "מהו היסוד הכי נפוץ באטמוספירה של כדור הארץ?", "a": "חנקן"}
    ],
    "היסטוריה": [
        {"q": "באיזו שנה החלה מלחמת העולם הראשונה?", "a": "1914"},
        {"q": "מי היה הנשיא הראשון של ארצות הברית?", "a": "ג'ורג' וושינגטון"},
        {"q": "מהי המהפכה הצרפתית?", "a": "תקופה של שינוי חברתי ופוליטי קיצוני בצרפת בין השנים 1789 ל-1799"}
    ],
    "תרבות פופ": [
        {"q": "מי שר את השיר 'Thriller'?", "a": "מייקל ג'קסון"},
        {"q": "באיזו סדרת טלוויזיה הדמות של וולטר ווייט מופיעה?", "a": "שובר שורות"},
        {"q": "מי כתבה את סדרת הספרים 'הארי פוטר'?", "a": "ג'יי קיי רולינג"}
    ]
}

# 3. Initialize game variables
players = []
scores = {}
rounds = 3

# 4. Write helper functions
def ask_question(player):
    print(f"\n{player}, אנא בחר קטגוריה: מדע, היסטוריה, תרבות פופ")
    category = input("הקטגוריה שבחרת: ").lower()

    if category not in questions:
        print("קטגוריה לא חוקית. תורך הסתיים.")
        return

    available_questions = questions[category]
    if not available_questions:
        print(f"אין כרגע שאלות זמינות בקטגוריית {category}.")
        return

    question_data = random.choice(available_questions)
    question = question_data["q"]
    correct_answer = question_data["a"]

    print(f"\nהשאלה שלך בקטגוריית {category}:")
    print(question)
    user_answer = input("תשובתך: ").strip()

    if user_answer.lower() == correct_answer.lower():
        print("תשובה נכונה!")
        scores[player] += 1
    else:
        print(f"תשובה שגויה. התשובה הנכונה היא: {correct_answer}")

def show_scores():
    print("\n--- טבלת הניקוד הנוכחית ---")
    for player, score in scores.items():
        print(f"{player}: {score} נקודות")
    print("--------------------------")

def declare_winner():
    if not scores:
        print("\nלא היו שחקנים במשחק.")
        return

    max_score = max(scores.values())
    winners = [player for player, score in scores.items() if score == max_score]

    print("\n--- סיום המשחק ---")
    if len(winners) == 1:
        print(f"המנצח הוא: {winners[0]} עם {max_score} נקודות!")
    else:
        winners_str = ", ".join(winners)
        print(f"יש תיקו! המנצחים הם: {winners_str} עם {max_score} נקודות!")
    print("-------------------")

# 5. Build the main game flow
def main():
    print("ברוכים הבאים למסע חידונים!")

    while True:
        try:
            num_players = int(input("כמה שחקנים ישחקו? "))
            if num_players < 1:
                print("מספר השחקנים חייב להיות לפחות 1.")
                continue
            break
        except ValueError:
            print("קלט לא חוקי. אנא הזן מספר.")
            return

    for i in range(num_players):
        player_name = input(f"הזן את שם שחקן {i+1}: ")
        players.append(player_name)
        scores[player_name] = 0

    for round_num in range(1, rounds + 1):
        print(f"\n--- סבב {round_num} ---")
        for player in players:
            ask_question(player)
        show_scores()

    declare_winner()

if __name__ == "__main__":
    main()