# מחשבון כרטיסים לערב סרט
# תאריך: 21-04-2025

# 1. קלט
age_str = input("Age? ")
day = input("Day (weekday/weekend)? ").lower()
loyalty = input("Loyalty member (y/n)? ").lower()

# 3. בדיקות תקינות
try:
    age = int(age_str)
    if age < 0:
        print("Invalid age")
        exit()
except ValueError:
    print("Invalid age")
    exit()

if day != "weekday" and day != "weekend":
    print("Invalid day")
    exit()

# 2. לוגיקת תמחור
price = 20  # מחיר בסיס

# הנחה לפי גיל
if age < 13:
    price *= 0.5
elif age >= 60:
    price *= 0.7

# תוספת סוף שבוע
if day == "weekend":
    price += 5

# הנחת מועדון לקוחות
if loyalty == "y":
    price -= 2

# 4. פלט
print(f"Total: ${int(price)}")