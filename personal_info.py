# Personal Information Manager
# Author: Surajit Chakraborty

print("=" * 40)
print("   PERSONAL INFORMATION MANAGER")
print("=" * 40)
print()

# Static info
name = "Surajit Chakraborty"
age = 21
city = "Kolkata"
hobby = "Learning Programming"

# User input
food = input("Enter your favorite food: ")
while food == "":
    print("Food cannot be empty!")
    food = input("Enter your favorite food: ")

color = input("Enter your favorite color: ")
while color == "":
    print("Color cannot be empty!")
    color = input("Enter your favorite color: ")

# Calculation
age_months = age * 12

# Output
print("\n" + "=" * 40)
print("        YOUR DETAILS")
print("=" * 40)

print(f"Name: {name}")
print(f"Age: {age} years ({age_months} months)")
print(f"City: {city}")
print(f"Hobby: {hobby}")

print(f"Favorite Food: {food}")
print(f"Favorite Color: {color}")

print("=" * 40)
print("Thank you for using this program!")
