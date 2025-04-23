while True:
    user_input = input("הכנס מספר (או 'q' כדי לצאת): ")
    if user_input.lower() == 'q':
        break
    try:
        number = int(user_input)
        if number % 2 == 0:
            print("Even")
        else:
            print("Odd")
    except ValueError:
        print("קלט לא חוקי. אנא הזן מספר שלם או 'q'.")