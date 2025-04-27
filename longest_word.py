def longest_word(words):
  """
  מוצאת את המילה הארוכה ביותר ברשימת מחרוזות.

  ארגומנטים:
    words: רשימה של מחרוזות.

  החזרות:
    המילה הארוכה ביותר ברשימה. אם הרשימה ריקה, מחזירה None.
    אם יש מספר מילים באותו אורך מקסימלי, מחזירה את הראשונה מביניהן.
  """
  if not words:
    return None

  longest = words[0]
  for word in words:
    if len(word) > len(longest):
      longest = word
  return longest

# בדיקת הפונקציה
print(f"המילה הארוכה ביותר ב-['apple', 'banana', 'kiwi']: {longest_word(['apple', 'banana', 'kiwi'])}")  # banana
print(f"המילה הארוכה ביותר ב-['cat', 'dog', 'fish']: {longest_word(['cat', 'dog', 'fish'])}")      # fish (אורך שווה, מחזירה את הראשונה)
print(f"המילה הארוכה ביותר ב-['a', 'b', 'c']: {longest_word(['a', 'b', 'c'])}")                # a
print(f"המילה הארוכה ביותר ברשימה ריקה: {longest_word([])}")                                    # None
print(f"המילה הארוכה ביותר ב-['hello', 'world', 'python', 'code']: {longest_word(['hello', 'world', 'python', 'code'])}") # python

def longest_word_with_length(words):
  """
  מוצאת את המילה הארוכה ביותר ברשימת מחרוזות ומחזירה אותה יחד עם אורכה.

  ארגומנטים:
    words: רשימה של מחרוזות.

  החזרות:
    tuple המכיל את המילה הארוכה ביותר ואת אורכה.
    אם הרשימה ריקה, מחזירה (None, 0).
    אם יש מספר מילים באותו אורך מקסימלי, מחזירה את הראשונה מביניהן.
  """
  if not words:
    return (None, 0)

  longest = words[0]
  max_length = len(longest)

  for word in words:
    if len(word) > max_length:
      longest = word
      max_length = len(word)

  return (longest, max_length)

# בדיקת הפונקציה
print(f"המילה הארוכה ביותר ואורכה ב-['apple', 'banana', 'kiwi']: {longest_word_with_length(['apple', 'banana', 'kiwi'])}")  # ('banana', 6)
print(f"המילה הארוכה ביותר ואורכה ב-['cat', 'dog', 'fish']: {longest_word_with_length(['cat', 'dog', 'fish'])}")      # ('fish', 4)
print(f"המילה הארוכה ביותר ואורכה ב-['a', 'b', 'c']: {longest_word_with_length(['a', 'b', 'c'])}")                # ('a', 1)
print(f"המילה הארוכה ביותר ואורכה ברשימה ריקה: {longest_word_with_length([])}")                                    # (None, 0)
print(f"המילה הארוכה ביותר ואורכה ב-['hello', 'world', 'python', 'code']: {longest_word_with_length(['hello', 'world', 'python', 'code'])}") # ('python', 6)