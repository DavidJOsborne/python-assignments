def canvote():
  age = raw_input("How old are you?")
  if int(age) < 18:
    print "You cant vote"
  else:
    print "You can vote"
canvote()
