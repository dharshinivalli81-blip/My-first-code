# Day 2 - Simple Calculator 
# Dharshini | SASTRA BSc CS 2026-2029 | Future Zoho Engineer

print("=== Dharshini's Day 2 Calculator ===")
print("60 Days Challenge: Day 2 ✅")

# User kitta 2 numbers vaanguram
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nEnna pannanum?")
print("1 = Add")
print("2 = Subtract") 
print("3 = Multiply")
print("4 = Divide")

choice = input("Enter 1/2/3/4: ")

# Condition check panni calculate panrom
if choice == '1':
    print(f"Result: {num1} + {num2} = {num1 + num2}")
elif choice == '2':
    print(f"Result: {num1} - {num2} = {num1 - num2}")
elif choice == '3':
    print(f"Result: {num1} * {num2} = {num1 * num2}")
elif choice == '4':
    if num2 == 0:
        print("Error ma: Zero vaala divide panna mudiyadhu!")
    else:
        print(f"Result: {num1} / {num2} = {num1 / num2}")
else:
    print("Invalid choice! 1,2,3,4 la onnu podu ma")

print("\nDay 2 Complete ✅")
print("Tomorrow Day 3 la paakalam 🚀")