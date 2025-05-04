students_info = {
    "אליס": {"grade": 85, "age": 16},
    "בוב": {"grade": 78, "age": 17},
    "צ'ארלי": {"grade": 92, "age": 16}
}

print("המילון ההתחלתי של פרטי התלמידים:")
print(students_info)
# 2.1 הוספת תלמיד חדש
students_info["דוד"] = {"grade": 76, "age": 15}
print("\nהמילון לאחר הוספת תלמיד חדש:")
print(students_info)
# 2.2 עדכון ציון של תלמיד קיים
students_info["בוב"]["grade"] = 82
print("\nהמילון לאחר עדכון הציון של בוב:")
print(students_info)
# 2.3 הסרת תלמיד מהמילון
del students_info["צ'ארלי"]
print("\nהמילון לאחר הסרת צ'ארלי:")
print(students_info)
# 2.4 חישוב והדפסת הציון הממוצע
total_grade = 0
num_students = len(students_info)

for student in students_info:
    total_grade += students_info[student]["grade"]

if num_students > 0:
    average_grade = total_grade / num_students
    print(f"\nהציון הממוצע של כל התלמידים: {average_grade:.2f}")
else:
    print("\nאין תלמידים במילון כדי לחשב ממוצע.")
    # 2.5 מציאת והדפסת שם התלמיד עם הציון הגבוה ביותר
highest_grade = -1
student_with_highest_grade = ""

for student in students_info:
    if students_info[student]["grade"] > highest_grade:
        highest_grade = students_info[student]["grade"]
        student_with_highest_grade = student

if student_with_highest_grade:
    print(f"\התלמיד עם הציון הגבוה ביותר הוא: {student_with_highest_grade} עם ציון {highest_grade}.")
else:
    print("\nאין תלמידים במילון כדי למצוא את הציון הגבוה ביותר.")