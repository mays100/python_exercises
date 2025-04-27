def rectangle_area(length, width):
  """
  מחשבת את שטח מלבן.

  ארגומנטים:
    length: אורך המלבן (מספר).
    width: רוחב המלבן (מספר).

  החזרות:
    שטח המלבן המחושב.
  """
  area = length * width
  return area

# בדיקת הפונקציה
print(f"שטח מלבן באורך 5 ורוחב 3: {rectangle_area(5, 3)}")   # 15
print(f"שטח מלבן באורך 10 ורוחב 4.5: {rectangle_area(10, 4.5)}") # 45.0
print(f"שטח מלבן באורך 0 ורוחב 7: {rectangle_area(0, 7)}")    # 0
print(f"שטח מלבן באורך 2.5 ורוחב 2.5: {rectangle_area(2.5, 2.5)}") # 6.25