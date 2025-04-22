# תרגיל 1: Salary Breakdown
gross_salary = float(input("הכנס את המשכורת ברוטו שלך: "))
tax_rate = 0.22
net_income = gross_salary * (1 - tax_rate)
rent = 3000
savings_goal = 1000

if net_income >= rent + savings_goal:
    print("Rent and save!")
elif net_income >= rent:
    print("Just rent.")
else:
    print("Not enough.")

print(f"המשכורת נטו שלך היא: {net_income:.2f}")
print("-" * 30)

# תרגיל 2: Shipping Calculator
item_price = float(input("הכנס את מחיר הפריט: "))
quantity = int(input("הכנס את כמות הפריטים: "))
total = item_price * quantity
shipping_fee = 0

free_shipping_applied = False
discount_applied = False

if total > 200:
    shipping_fee = 0
    free_shipping_applied = True

if total > 500:
    discount = total * 0.10
    total -= discount
    discount_applied = True

final_cost = total + shipping_fee
print(f"העלות הכוללת היא: {final_cost:.2f}")
print(f"האם הוחל משלוח חינם? {free_shipping_applied}")
print(f"האם הוחל הנחה? {discount_applied}")
print("-" * 30)

# תרגיל 3: Medieval Guard Duty
age = int(input("הכנס את גיל המבקר: "))
has_gold_pass = input("האם למבקר יש כרטיס זהב? (True/False): ").lower() == "true"
is_royal = input("האם המבקר חלק ממשפחת המלוכה? (True/False): ").lower() == "true"
is_blacklisted = input("האם המבקר ברשימה השחורה? (True/False): ").lower() == "true"

allowed_in = age >= 18 and (has_gold_pass or is_royal) and not is_blacklisted

if allowed_in:
    print("המבקר רשאי להיכנס.")
else:
    print("למבקר אסור להיכנס.")
print("-" * 30)

# תרגיל 4: Car Insurance Quote
driver_age = int(input("הכנס את גיל הנהג: "))
accident_count = int(input("הכנס את מספר התאונות שהיו לנהג: "))
base_premium = 0

if driver_age < 25:
    base_premium = 3000
else:
    base_premium = 2000

premium = base_premium + (accident_count * 500)

if premium > 5000:
    print("High Risk")
else:
    print("Standard")
print(f"הפרמיה הראשונית היא: {base_premium}")
print(f"הפרמיה הסופית היא: {premium}")
print("-" * 30)

# תרגיל 5: Lab Safety Checklist
temperature = float(input("הכנס את הטמפרטורה: "))
pressure = float(input("הכנס את הלחץ: "))
voltage = float(input("הכנס את המתח: "))

safe_temperature = 20 <= temperature <= 80
safe_pressure = pressure < 50
safe_voltage = 200 <= voltage <= 250

if safe_temperature and safe_pressure and safe_voltage:
    print("Safe to proceed")
else:
    print("Unsafe conditions")
print("-" * 30)

# תרגיל 6: Wizard’s Final Exam
spell_power = int(input("הכנס את עוצמת הכישוף (0-100): "))
accuracy = int(input("הכנס את דיוק הכישוף (0-100): "))
control = int(input("הכנס את שליטה בכישוף (0-100): "))

average_score = (spell_power + accuracy + control) / 3

if spell_power < 40 or accuracy < 40 or control < 40:
    grade = "Fail"
elif average_score >= 90:
    grade = "Archmage"
elif average_score >= 75:
    grade = "Mage"
elif average_score >= 60:
    grade = "Apprentice"
else:
    grade = "Fail"

print(f"ציון ממוצע: {average_score:.2f}")
print(f"דרגה: {grade}")
print("-" * 30)