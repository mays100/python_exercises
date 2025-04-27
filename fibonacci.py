def fibonacci_iterative(n):
  """
  יוצר את n האיברים הראשונים של סדרת פיבונאצ'י באופן איטרטיבי.

  ארגומנטים:
    n: מספר האיברים בסדרה.

  החזרות:
    רשימה המכילה את n האיברים הראשונים של סדרת פיבונאצ'י.
  """
  if n <= 0:
    return []
  elif n == 1:
    return [0]
  else:
    list_fib = [0, 1]
    while len(list_fib) < n:
      next_fib = list_fib[-1] + list_fib[-2]
      list_fib.append(next_fib)
    return list_fib

# בדיקת הפונקציה האיטרטיבית
print(f"סדרת פיבונאצ'י עבור n = 0: {fibonacci_iterative(0)}")   # []
print(f"סדרת פיבונאצ'י עבור n = 1: {fibonacci_iterative(1)}")   # [0]
print(f"סדרת פיבונאצ'י עבור n = 2: {fibonacci_iterative(2)}")   # [0, 1]
print(f"סדרת פיבונאצ'י עבור n = 10: {fibonacci_iterative(10)}") # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
print(f"סדרת פיבונאצ'י עבור n = 5: {fibonacci_iterative(5)}")  # [0, 1, 1, 2, 3]