# 1. Create a greeting for your program.

# 2. Ask the user for the city that they grew up in.

# 3. Ask the user for the name of a pet.

# 4. Combine the name of their city and pet and show them their band name.

# 5. Make sure the input cursor shows on a new line.

print("Hello there! Welcome to the band name generator.")

cityName = input("What city did you grew up in?\n")

petName = input("What is the name of your pet?\n")

bandName = cityName + " " + petName

print("Your band name is here! - " + bandName)

""" Output
Hello there! Welcome to the band name generator.
What city did you grew up in?
Bagalkot
What is the name of your pet?
Rocky
Your band name is here! - Bagalkot Rocky
"""