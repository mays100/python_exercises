#l1 = [123 , "may" , None , True , [12,45,67]]
#      0     1       2      3         4
#                                   0  1  2

#list_name
#print(l1[5])

# 1. צור רשימה חדשה עם 4 ערכי מספרים
stock_values = [100, 50, 75, 120]

# 2. הוסף 10 למניה הראשונה
stock_values[0] += 10

# 3. הסר 32 מהשנייה
stock_values[1] -= 32

# 4. חלק בשלוש את השלישית
stock_values[2] /= 3

# 5. הכפל ב-1.6 את הרביעית
stock_values[3] *= 1.6

# 6. הדפס את הרשימה המעודכנת
print(stock_values)
# נשתמש ברשימה המעודכנת ממשימה 3
stock_values = [110.0, 18.0, 25.0, 192.0]

# הוסף 3 ערכים נוספים לרשימת המניות באמצעות append()
stock_values.append(85)
stock_values.append(115)
stock_values.append(95)

# הסר את המניות מהאינדקסים 2 ו-3
stock_values.pop(2)  # הסרת האיבר באינדקס 2
stock_values.pop(2)  # הסרת האיבר באינדקס 2 שוב (האיבר שהיה במקור באינדקס 3)

# הדפס את הרשימה המעודכנת
print(stock_values)