# 1. Create a greeting for tip calculator.

# 2. Ask the user for the total bill amount.

# 3. Ask the user for the percent of tip.

# 4. Ask for how many people the tip has to be split.

# 5. Display the total bill split.

print("Welcome to the tip calculator!")
bill_amount = int(input("What is the total bill amount?\n$: "))
tip_percent = int(input("How much tip would you like to give?\nPercent: "))
total_people = int(input("How many people to split the bill?\nPeople: "))

bill_per_person = ((bill_amount * tip_percent/100) + bill_amount ) / total_people

print("Each person should pay: $", bill_per_person)

