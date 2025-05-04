# עבודה עם טאפלים וסטים
# תאריך: 26-01-2025

# 1. יצירת סט עם 5 מספרים ייחודיים
my_set = {5, 2, 8, 1, 9}
print("הסט שיצרתי:", my_set)

# 2. יצירת טאפל עם ריבועי המספרים מהסט
my_tuple = tuple(num ** 2 for num in my_set)
print("הטאפל של הריבועים:", my_tuple)

# 3.1 המרת הסט לרשימה ומיון בסדר יורד
my_list = list(my_set)
my_list.sort(reverse=True)
print("הרשימה הממוינת בסדר יורד:", my_list)

# 3.2 מציאת החיתוך בין הסט לטאפל
tuple_as_set = set(my_tuple)
intersection = my_set.intersection(tuple_as_set)
print("החיתוך בין הסט לטאפל:", intersection)

# 3.3 הדפסת האורך של הטאפל והסט
print("אורך הטאפל:", len(my_tuple))
print("אורך הסט:", len(my_set))

# 3.4 ניסיון להוסיף ערך חדש לטאפל
try:
    # my_tuple.append(36) # זו פעולה לא חוקית על טאפל
    new_tuple = my_tuple + (36,) # יצירת טאפל חדש עם הערך הנוסף
    print("הטאפל לאחר ניסיון הוספה (נוצר טאפל חדש):", new_tuple)
except AttributeError as e:
    print(f"שגיאה בניסיון להוסיף לטאפל: {e}")

# 3.5 הדפסת תוצאת החיתוך בין הסט לטאפל
print("תוצאת החיתוך בין הסט לטאפל:", intersection)