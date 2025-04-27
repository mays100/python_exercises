# 1. יצירת רשימה של מילוני תלמידים
students = [
    {'name': 'איתי', 'grades': [80, 90, 75, 85]},
    {'name': 'נועה', 'grades': [92, 88, 95, 90]},
    {'name': 'דניאל', 'grades': [60, 55, 70, 65]},
    {'name': 'יעל', 'grades': []},  # תלמיד ללא ציונים לבדיקת טיפול בשגיאות
    {'name': 'אדם', 'grades': [95, 95, 95, 95]}
]

# 2.1. חישוב ממוצע ציון לכל תלמיד
print("### ממוצעי ציונים לכל תלמיד: ###")
for student in students:
    if student['grades']:
        average_grade = sum(student['grades']) / len(student['grades'])
        print(f"{student['name']}: ממוצע - {average_grade:.2f}")
    else:
        print(f"{student['name']}: אין ציונים זמינים")

# שמירת ממוצעי הציונים במילונים עבור שימוש עתידי
for student in students:
    if student['grades']:
        student['average_grade'] = sum(student['grades']) / len(student['grades'])
    else:
        student['average_grade'] = None  # או ערך אחר לבחירתך כדי לסמן שאין ממוצע

# 2.2. מציאת תלמידים שעברו בהצלחה (ממוצע 50 ומעלה)
print("\n### תלמידים שעברו בהצלחה (ממוצע 50 ומעלה): ###")
passed_students = filter(lambda student: student['average_grade'] is not None and student['average_grade'] >= 50, students)
for student in passed_students:
    print(f"{student['name']}: ממוצע - {student['average_grade']:.2f}")

# 2.3. מיון תלמידים לפי ממוצע הציונים בסדר יורד
print("\n### תלמידים ממוינים לפי ממוצע ציון (בסדר יורד): ###")
# חשוב לטפל במקרה של תלמידים ללא ציונים במיון. נניח שנדאג שהם יופיעו בסוף.
# נשתמש בערך שלילי גדול מאוד עבורם כדי שימוינו אחרונים.
sorted_students = sorted(students, key=lambda student: student['average_grade'] if student['average_grade'] is not None else -float('inf'), reverse=True)
for student in sorted_students:
    if student['average_grade'] is not None:
        print(f"{student['name']}: ממוצע - {student['average_grade']:.2f}")
    else:
        print(f"{student['name']}: אין ציונים זמינים")

# 2.4. הגדלת ציון כל תלמיד ב-5 נקודות (מקסימום 100)
print("\n### ציונים מעודכנים לאחר הוספת 5 נקודות: ###")
updated_students = []
for student in students:
    updated_grades = list(map(lambda grade: min(grade + 5, 100), student['grades']))
    updated_students.append({'name': student['name'], 'grades': updated_grades})
    print(f"{student['name']}: ציונים מעודכנים - {updated_grades}")

# נעדכן את רשימת הסטודנטים המקורית עם הציונים החדשים עבור המשימות הבאות, אם צריך.
# students = updated_students # אם ברצונך לעבוד עם הציונים המעודכנים בהמשך

# 2.5. טיפול בשגיאות (כבר טופל בסעיף 2.1, נדגים שוב ליתר ביטחון)
print("\n### בדיקת טיפול בשגיאות (תלמידים ללא ציונים): ###")
for student in students:
    if not student['grades']:
        print(f"{student['name']}: אין ציונים זמינים")
    # (חישוב הממוצע כבר בוצע וטופל בסעיף 2.1)

# 2.6. יצירת דו"ח סיכום
print("\n### דו''ח סיכום ציונים: ###")

# יצירת רשימת tuples של שם וממוצע ציון (כולל טיפול בתלמידים ללא ציונים)
student_averages = []
for student in students:
    if student['average_grade'] is not None:
        student_averages.append((student['name'], student['average_grade']))

# מציאת הציון הגבוה ביותר בכל הכיתה
# נתעלם מתלמידים ללא ציונים בחישוב הציון הגבוה ביותר.
all_grades = []
for student in students:
    all_grades.extend(student['grades'])

if all_grades:
    highest_grade_class = max(all_grades)
    print(f"הציון הגבוה ביותר בכיתה: {highest_grade_class}")

    # מציאת התלמיד(ים) שהשיגו את הציון הגבוה ביותר
    top_students = [student['name'] for student in students if student['grades'] and max(student['grades']) == highest_grade_class]
    print(f"התלמיד(ים) שהשיג(ו) את הציון הגבוה ביותר: {', '.join(top_students)}")
else:
    print("אין ציונים זמינים בכיתה.")

# דוגמה נוספת לדו"ח סיכום עם list comprehension כפי שנדרש
summary_report = [(student['name'], student['average_grade']) for student in students if student['average_grade'] is not None]
print("\n### דו''ח סיכום (באמצעות רשימת הבנה): ###")
print(summary_report)