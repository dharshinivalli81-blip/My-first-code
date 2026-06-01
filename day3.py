# Day 3 - Odd or Even Checker
# Dharshini | SASTRA BSc CS | 60 Days Challenge

print("=== Day 3: Odd or Even Checker ===")
print("Oru number kudunga, Even ah Odd ah nu solren!")

# User kitta number vaangrom
number = int(input("Enter a number: "))

# Logic: 2 aala divide panni remainder paakrom
if number % 2 == 0:
    print(f"Result: {number} is an EVEN number ✅")
else:
    print(f"Result: {number} is an ODD number ✅")

print("\nDay 3 Complete ✅ Tomorrow Day 4: Biggest of 3 Numbers")