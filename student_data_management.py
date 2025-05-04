# ניהול נתוני תלמידים
# תאריך: 26-01-2025

# הגדרת משתנים למקצועות בעברית
tanach = "תנ\"ך"
sport = "ספורט"
math = "מתמטיקה"

# 1. יצירת המילון הראשוני
students = {
    "אליס": {"age": 16, "subjects": ["מתמטיקה", "אנגלית", "מדעים"], "grades": {90, 85, 92}},
    "בוב": {"age": 17, "subjects": ["היסטוריה", "ספרות", "אנגלית"], "grades": {78, 88, 80}},
    "צ'ארלי": {"age": 16, "subjects": ["מתמטיקה", "פיזיקה"], "grades": {95, 88}}
}

print("המילון ההתחלתי של פרטי התלמידים:")
print(students)

# 2.1 הוספת תלמיד חדש
students["דוד"] = {"age": 15, "subjects": [tanach, sport, math], "grades": {80, 92, 88}}
print("\nהמילון לאחר הוספת דוד:")
print(students)

# 2.2 עדכון ציונים של תלמיד קיים
students["אליס"]["grades"].add(98)
print("\nהמילון לאחר עדכון הציונים של אליס:")
print(students)

# 2.3 הסרת מקצוע מרשימת המקצועות של תלמיד
students["בוב"]["subjects"].remove("אנגלית")
print("\nהמילון לאחר הסרת 'אנגלית' מרשימת המקצועות של בוב:")
print(students)

# 2.4 מציאת הציון הממוצע של תלמיד ספציפי
student_name = "אליס"
grades_list = list(students[student_name]["grades"])
average_grade = sum(grades_list) / len(grades_list)
print(f"\nהציון הממוצע של {student_name}: {average_grade:.2f}")

# 2.5 מציאת התלמיד עם הציון הממוצע הגבוה ביותר
highest_average_grade = -1
student_with_highest_average = None

for name, info in students.items():
    grades_list = list(info["grades"])
    if grades_list:
        average = sum(grades_list) / len(grades_list)
        if average > highest_average_grade:
            highest_average_grade = average
            student_with_highest_average = name
            highest_average_info = info

if student_with_highest_average:
    print(f"\nהתלמיד עם הציון הממוצע הגבוה ביותר:")
    print(f"שם: {student_with_highest_average}")
    print(f"גיל: {highest_average_info['age']}")
    print(f"מקצועות: {highest_average_info['subjects']}")
else:
    print("\nאין תלמידים במערכת.")

# 3. יצירת טאפלים עבור כל תלמיד והדפסה ממוינת
student_tuples = []
for name, info in students.items():
    num_subjects = len(info["subjects"])
    student_tuple = (name, info["age"], num_subjects)
    student_tuples.append(student_tuple)

# מיון הטאפלים לפי מספר המקצועות (האיבר השלישי בטאפל)
sorted_student_tuples = sorted(student_tuples, key=lambda student: student[2])

print("\nטאפלים של תלמידים (שם, גיל, מספר מקצועות) ממוינים לפי מספר מקצועות:")
for student_tuple in sorted_student_tuples:
    print(student_tuple)