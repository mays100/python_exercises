# משימה 1: הדמיית מרוץ - יצירת משתנים למקומות 1-5
place1 = "מתחרה א'"
place2 = "מתחרה ב'"
place3 = "מתחרה ג'"
place4 = "מתחרה ד'"
place5 = "מתחרה ה'"

print("תוצאות המרוץ (5 המקומות הראשונים):")
print(f"מקום ראשון: {place1}")
print(f"מקום שני: {place2}")
print(f"מקום שלישי: {place3}")
print(f"מקום רביעי: {place4}")
print(f"מקום חמישי: {place5}")

print("\n--- הדגמה לשמירת 1000 מקומות ---")

# שימוש ברשימה לשמירת 1000 מקומות (הדגמה חלקית)
results_list = []
for i in range(1, 1001):
    results_list.append(f"מתחרה מספר {i}")

print("\n5 המקומות הראשונים באמצעות רשימה:")
print(f"מקום ראשון: {results_list[0]}")
print(f"מקום שני: {results_list[1]}")
print(f"מקום שלישי: {results_list[2]}")
print(f"מקום רביעי: {results_list[3]}")
print(f"מקום חמישי: {results_list[4]}")

print(f"\nהמקום ה-100 באמצעות רשימה: {results_list[99]}")
print(f"המקום ה-1000 באמצעות רשימה: {results_list[999]}")

# שימוש במילון לשמירת 1000 מקומות (הדגמה חלקית)
results_dict = {}
for i in range(1, 1001):
    results_dict[i] = f"מתחרה מספר {i}"

print("\n5 המקומות הראשונים באמצעות מילון:")
print(f"מקום ראשון: {results_dict[1]}")
print(f"מקום שני: {results_dict[2]}")
print(f"מקום שלישי: {results_dict[3]}")
print(f"מקום רביעי: {results_dict[4]}")
print(f"מקום חמישי: {results_dict[5]}")

print(f"\nהמקום ה-100 באמצעות מילון: {results_dict[100]}")
print(f"המקום ה-1000 באמצעות מילון: {results_dict[1000]}")