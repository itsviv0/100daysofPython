# 1. Password Generator
# 2. Ask for number of letters, numbers and symbols from the user.
# 3. Randomize the required letters, numbers and symbols and make a password
# 4. Ensure that the password is of minimum length 8, else give a message weak password.

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', ',', '/', '{', ']', '}', ']', '_', '^']

print("Strong Password Generator!")
nletters= (input("How many letters would you like in your password?\n"))
nsymbols = (input(f"How many symbols would you like?\n"))
nnumbers = (input(f"How many numbers would you like?\n"))

if not nletters.isdigit() or not nsymbols.isdigit() or not nnumbers.isdigit():
  print("Invalid value, enter a number instead.")
else:
  password = []
  
  for i in range(0, int(nletters)):
    random_letter = random.randint(0, 51)
    password.append(letters[random_letter])
  
  for i in range(0, int(nnumbers)):
    random_number = random.randint(0,9)
    password.append(str(random_number))

  for i in range(0, int(nsymbols)):
    random_symbol = random.randint(0,16)
    password.append(symbols[random_symbol])
  	
  random.shuffle(password)
  print(f"Generated random strong password: {''.join(password)}\n")
  
  if len(password) < 8:
    print("Your password is weak, try to include at least 8 characters for a stronger password.")
  elif len(password) == 8:
    print("Your password is just right.")
  else:
    print("Your password is strong.")
  	
