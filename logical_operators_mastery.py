# חלק 1: הערכה ידנית
manual_evaluation_results = [
    True,
    True,
    False,
    False,
    True
]
print("Part 1: Manual Evaluation Results:", manual_evaluation_results)
print("-" * 30)

# חלק 2: כתיבת ביטויים בוליאניים
# 1.
expression1 = "10 <= x <= 20"
print("Part 2 - Expression 1:", expression1)
# 2.
expression2 = "s and 'py' in s"
print("Part 2 - Expression 2:", expression2)
# 3.
expression3 = "n < 0 or abs(n) > 100"
print("Part 2 - Expression 3:", expression3)
# 4.
expression4 = "(user_role == 'admin' and active) or superuser"
print("Part 2 - Expression 4:", expression4)
# 5.
expression5 = "not (temperature < 0 or temperature > 35)"
print("Part 2 - Expression 5:", expression5)
print("-" * 30)

# חלק 3: בודק זכאות גישה
print("Part 3: Access Eligibility Checker")
age = int(input("הכנס גיל: "))
if age < 0:
    print("Invalid age")
    exit()
has_ticket = input("האם יש כרטיס? (y/n): ").lower()
vip_code = input("הכנס קוד VIP (השאר ריק אם אין): ").upper()

eligible = (age >= 18 and has_ticket == "y") or (vip_code == "GOLDVIP")
print("Access granted:", eligible)
print("-" * 30)

# חלק 4: בודק תקינות טופס קלט
print("Part 4: Form Input Validator")
username = input("הכנס שם משתמש: ")
password = input("הכנס סיסמה: ")
email = input("הכנס אימייל: ")

is_username_valid = bool(username)
is_password_valid = len(password) >= 8 and any(char.isdigit() for char in password)
is_email_valid = email.count("@") == 1 and email.endswith(".com")

if is_username_valid and is_password_valid and is_email_valid:
    print("Form valid")
else:
    print("Form invalid")
print("-" * 30)

# חלק 5: מחשבון הנחה ותוספת תשלום
print("Part 5: Discount & Surcharge Calculator")
order_amount = float(input("הכנס סכום הזמנה: "))
customer_type = input("הכנס סוג לקוח (regular, member, vip): ").lower()
coupon_code = input("הכנס קוד קופון (השאר ריק אם אין): ").upper()

final_amount = order_amount

# תוספת תשלום
if order_amount < 50:
    final_amount *= 1.05

# הנחה רגילה
if customer_type == "member" or customer_type == "vip":
    final_amount *= 0.90

# הנחת VIP עם קופון
if customer_type == "vip" and coupon_code == "SAVE15":
    final_amount *= 0.85

print(f"Final total: ${final_amount:.2f}")