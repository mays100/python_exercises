# מספרים המתחלקים ב-3 (עם אתגר נוסף)
# תאריך: 26-01-2025

def find_divisible_numbers(start, end, divisor=3, use_while=False):
    """
    מוצא ומדפיס מספרים המתחלקים במחלק בטווח נתון.

    Args:
        start (int): המספר ההתחלתי של הטווח (כולל).
        end (int): המספר הסופי של הטווח (כולל).
        divisor (int): המספר שבו יש לבדוק חלוקה (ברירת מחדל: 3).
        use_while (bool): אם True, משתמש בלולאת while במקום for.
    """
    count = 0
    print(f"מספרים המתחלקים ב-{divisor} בטווח שבין {start} ל-{end}:")

    if use_while:
        current = start
        while current <= end:
            if current % divisor == 0:
                print(current)
                count += 1
            current += 1
    else:
        for number in range(start, end + 1):
            if number % divisor == 0:
                print(number)
                count += 1

    print(f"\nסך הכל מספרים המתחלקים ב-{divisor} בטווח: {count}")

if __name__ == "__main__":
    try:
        start_range = int(input("הכנס את המספר ההתחלתי של הטווח: "))
        end_range = int(input("הכנס את המספר הסופי של הטווח: "))
        custom_divisor_input = input("האם תרצה להשתמש במחלק מותאם אישית? (כן/לא, ברירת מחדל: לא): ").lower()

        if custom_divisor_input == "כן":
            divisor = int(input("הכנס את המחלק המותאם אישית: "))
            use_while_loop = input("האם תרצה להשתמש בלולאת while במקום for? (כן/לא, ברירת מחדל: לא): ").lower()
            find_divisible_numbers(start_range, end_range, divisor, use_while_loop == "כן")
        else:
            use_while_loop = input("האם תרצה להשתמש בלולאת while במקום for? (כן/לא, ברירת מחדל: לא): ").lower()
            find_divisible_numbers(start_range, end_range, use_while=use_while_loop == "כן")

    except ValueError:
        print("קלט לא תקין. אנא הכנס מספרים שלמים.")