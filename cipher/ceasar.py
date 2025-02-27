alphabet = 'abcdefghijklmnopqrstuvwxyz'
while True:
  newWord = ""
  option = raw_input("Choose an option\nencrypt (type 1)\ndecrypt with key (type 2)\ndecrypt with brute force (type 3)")
  if option == "1":
    print ""
    character = raw_input("what would you like to encrypt?\n")
    key = int(raw_input("what is the key?\n"))
    print ""
    for i in character:
      if i.lower() in alphabet:
        newWord += alphabet[(alphabet.find(i.lower()) + key) % 26]
      else:
        newWord += i
    print newWord
  elif option == "2":
    print ""
    character = raw_input("what would you like to decrypt?")
    key = int(raw_input("what is the key?"))
    for i in character:
      if i.lower() in alphabet:
        newWord += alphabet[(alphabet.find(i.lower()) - key) % 26]
      else:
        newWord += i
    print newWord
  elif option == "3":
    print ""
    character = raw_input("what would you like to decrypt?")
    key = 1
    while key < 26:
      newWord = ""
      for i in character:
        if i.lower() in alphabet:
          newWord += alphabet[(alphabet.find(i.lower()) - key) % 26]
        else:
          newWord += i
      print key,":",newWord
      key+=1
    print ""
  else:
    print("invalid input")
