# def reverse_string(text):
#   """
#   הופכת מחרוזת נתונה באמצעות slicing.

#   ארגומנטים:
#     text: המחרוזת אותה יש להפוך.

#   החזרות:
#     המחרוזת הפוכה.
#   """
#   return text[::-1]

# # בדיקת הפונקציה
# print(reverse_string("שלום"))
# print(reverse_string("Python"))
# print(reverse_string("12345"))

# ועכשיו פתרון ללא שימוש בslicing:

def reverse_string_no_slicing(text):
  """
  הופכת מחרוזת נתונה ללא שימוש ב-slicing.

  ארגומנטים:
    text: המחרוזת אותה יש להפוך.

  החזרות:
    המחרוזת הפוכה.
  """
  reversed_text = ""
  for char in text:
    reversed_text = char + reversed_text
  return reversed_text

# בדיקת הפונקציה
print(reverse_string_no_slicing("שלום"))
print(reverse_string_no_slicing("Python"))
print(reverse_string_no_slicing("12345"))