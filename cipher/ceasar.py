alphabet = 'abcdefghijklmnopqrstuvwxyz'
while True:
  newWord = ""
  option = raw_input("Choose an option\nencrypt (type 1)\ndecrypt with key (type 2)\ndecrypt with brute force (type 3)")
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
  elif option == "3":
    character = raw_input("what would you like to decrypt?")
    l = 1
    while l < 26:
      newWord = ""
      for i in character:
        newWord += alphabet[(alphabet.find(i) - int(l)) % 26]
      print newWord
      l+=1
  else:
    print("invalid input")
