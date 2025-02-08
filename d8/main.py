# 1. create a ceasar function.
# 2. the function takes the text, shift position and whether to cypher or decypher.
# 3. Run a while loop to start the program.
# 4. Ask whether to encrypt or decrypt.
# 5. A case to handle the termination.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_position, cipher_direction):
  end_text = ""
  if cipher_direction == "1":
    shift_position *= -1
  for char in start_text:
    if char.isalpha():
      position = alphabet.index(char)
      new_position = position + shift_position
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}\n")

while True:
  direction = input("Type '1' to encrypt, type '2' to decrypt:\n")
  while direction not in {'1', '2'}:
    print("Option not available!")
    direction = input("Type '1' to encrypt, type '2' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  if shift > 26:
    shift = shift % shift == 0

  caesar(start_text=text, shift_position=shift, cipher_direction=direction)
  choice = input("Do you want to decode more?\nType 'yes' or 'no': ")
  while choice not in ['yes', 'no']:
    choice = input("Wrong input\n Enter either 'yes' or 'no': ")
  if choice == 'no':
    print("Closing the decrypter.")
    break
