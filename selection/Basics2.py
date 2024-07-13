grade = float(input("Grade: "))

if grade >= 80 and grade <= 100:
    print(f'{grade} is A')

elif grade >= 70 and grade <= 79:
    print(f'{grade} is B')

elif grade >= 50 and grade <= 69:
    print(f'{grade} is C')

elif grade >= 40 and grade <= 49:
    print(f'{grade} is D')

elif grade >= 0 and grade <= 39:
    print(f'{grade} is F')

else:
    print("Invalid grade")

