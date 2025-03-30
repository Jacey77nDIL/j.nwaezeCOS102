def calculate_atr(years_experience, age):

    if years_experience > 25 and age >= 55:
        return 5600000.0  # N5,600,000
    elif years_experience > 20 and age >= 45:
        return 4480000.0  # N4,480,000
    elif years_experience > 10 and age >= 35:
        return 1500000.0  # N1,500,000
    else:
        return 550000.0   # N550,000

# Get input from the user
years = int(input("Enter the staff's years of experience: "))
age = int(input("Enter the staff's age: "))

atr = calculate_atr(years, age)
print(f"For a staff with {years} years of experience and age {age}, the ATR is N{atr:,.2f}")