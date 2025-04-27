import math

def is_prime(num):
  """
  בדיקה האם מספר נתון הוא מספר ראשוני.

  ארגומנטים:
    num: המספר השלם לבדיקה.

  החזרות:
    True אם המספר ראשוני, False אחרת.
  """
  if num <= 1:
    return False
  # אופטימיזציה: בודקים מחלקים עד לשורש הריבועי של המספר
  for i in range(2, int(math.sqrt(num)) + 1):
    if num % i == 0:
      return False
  return True

# בדיקת הפונקציה עם קלטים שונים
print(f"האם 2 מספר ראשוני? {is_prime(2)}")   # True
print(f"האם 10 מספר ראשוני? {is_prime(10)}")  # False
print(f"האם 17 מספר ראשוני? {is_prime(17)}")  # True
print(f"האם 1 מספר ראשוני? {is_prime(1)}")   # False
print(f"האם 0 מספר ראשוני? {is_prime(0)}")   # False
print(f"האם -5 מספר ראשוני? {is_prime(-5)}")  # False
print(f"האם 29 מספר ראשוני? {is_prime(29)}")  # True