# Profile Builder
# Asks the user for information and displays a formatted summary

print("--- Profile Builder ---")
print()

name = input("What is your name? ")
age = int(input("How old are you? "))
height = float(input("How tall are you in metres? "))

print()
print("--- Your Profile ---")
print(f"Name:   {name}")
print(f"Age:    {age} years old")
print(f"Height: {height:.2f} metres")
print(f"In 10 years you will be {age + 10} years old.")