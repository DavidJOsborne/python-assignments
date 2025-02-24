alphabet = 'abcdefghijklmnopqrstuvwxyz'
newWord = ""
option = raw_input("Would you like to encrypt (type 1) or decrypt (type 2)")
if option == "1":
  character = raw_input("what would you like to encrypt?")
  key = raw_input("what is the key?")
  for i in character:
    newWord += alphabet[(alphabet.find(i) + int(key)) % 26]
  print newWord
elif option == "2":
  character = raw_input("what would you like to decrypt?")
  key = raw_input("what is the key?")
  for i in character:
    newWord += alphabet[(alphabet.find(i) - int(key)) % 26]
  print newWord
else:
  print("error. type 1 or type 2.")
