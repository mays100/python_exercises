code1 = input().lower()
code2 = input().lower()
code3 = input().lower()
numA = int(input())
numB = int(input())

# אימות מילים
if not code1.isalpha() or not code2.isalpha() or not code3.isalpha():
    print("Invalid codeword")
    exit()

# אימות מספרים
if numA < 1 or numB < 1:
    print("Invalid numbers")
    exit()

# פעולות על משתנים
combined = f"{code1}-{code2}-{code3}"
secret_number = (numA * numB) + numA - numB
swapped_A = numB
swapped_B = numA
avg_value = (numA + numB) / 2
message_length = len(combined)
is_palindrome = combined.replace("-", "") == combined.replace("-", "")[::-1]

# פלט
print(f"Secret Code: {combined}")
print(f"Secret Number: {secret_number}")
print(f"Swapped Values: A={swapped_A}, B={swapped_B}")
print(f"Average of Originals: {avg_value}")
print(f"Combined Length: {message_length}")
print(f"Palindrome: {is_palindrome}")