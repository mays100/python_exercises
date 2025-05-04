def display_menu():
    """מציג את תפריט האפשרויות למשתמש."""
    print("\n===== מנהל רשימת קניות =====")
    print("1. הוסף פריט")
    print("2. הסר פריט")
    print("3. הצג רשימה")
    print("4. נקה רשימה")
    print("5. יציאה")
    print("============================")

def add_item(shopping_list, item):
    """מוסיף פריט לרשימת הקניות אם הוא אינו קיים בה כבר."""
    if not item:
        print("שגיאה: לא ניתן להוסיף פריט ריק.")
        return
    if item in shopping_list:
        print(f"'{item}' כבר קיים ברשימה.")
    else:
        shopping_list.append(item)
        print(f"'{item}' נוסף לרשימה.")

def remove_item(shopping_list, item):
    """מסיר פריט מרשימת הקניות אם הוא קיים בה; אחרת, מציג אזהרה."""
    if not item:
        print("שגיאה: לא ניתן להסיר פריט ריק.")
        return
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' הוסר מהרשימה.")
    else:
        print(f"'{item}' לא נמצא ברשימה.")

def show_list(shopping_list):
    """מציג את כל הפריטים הנוכחיים ברשימת הקניות, או הודעה אם הרשימה ריקה."""
    if not shopping_list:
        print("רשימת הקניות ריקה.")
    else:
        print("\nרשימת הקניות הנוכחית:")
        for item in shopping_list:
            print(f"- {item}")

def clear_list(shopping_list):
    """מרוקן את רשימת הקניות לאחר קבלת אישור מהמשתמש."""
    if not shopping_list:
        print("רשימת הקניות כבר ריקה.")
        return
    confirmation = input("האם אתה בטוח שברצונך לנקות את כל רשימת הקניות? (כן/לא): ").lower()
    if confirmation == 'כן':
        shopping_list.clear()
        print("רשימת הקניות נוקתה.")
    elif confirmation == 'לא':
        print("ניקוי הרשימה בוטל.")
    else:
        print("קלט לא חוקי. ניקוי הרשימה בוטל.")

# אתחול רשימת הקניות
shopping_list = []

# לולאה ראשית של התוכנית
while True:
    display_menu()
    choice = input("בחר פעולה (הקלד את המספר): ").strip()  # שימוש ב-strip() להסרת רווחים מיותרים

    if choice == '1':
        item = input("הכנס פריט להוספה: ").strip()
        add_item(shopping_list, item)
    elif choice == '2':
        item = input("הכנס פריט להסרה: ").strip()
        remove_item(shopping_list, item)
    elif choice == '3':
        show_list(shopping_list)
    elif choice == '4':
        clear_list(shopping_list)
    elif choice == '5':
        print("יציאה מהתוכנית. להתראות!")
        break
    else:
        print("בחירה לא חוקית, אנא נסה שוב.")

# סיום התוכנית