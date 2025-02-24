def sigmabot():
  sigma = str(raw_input("are you a sigma?"))
  if sigma == "y" or sigma == "yes" or sigma == "yup" or sigma == "yep" or sigma == "yeah" or sigma == "yea":
    aura = 0
    print("if you are a true sigma, then complete this test to test your aura.")
    print("question 1:")
    q1 = str(raw_input("what is the best show ever?"))
    if q1 == "skibidi toilet":
      aura += 100
      print("correct! you have earned 100 aura points.")
    else:
      aura -= 100
      print("incorrect! you have lost 100 aura points.")
    print("you currently have " + str(aura) + " aura points.")
    print("question 2:")
    q2 = str(raw_input("who is calling?"))
    if q2 == "john pork":
      print("yes! john pork is calling! you have earned 100 aura points.")
      aura += 100
    elif q2 == "freakbob":
      print("hide your tushie! because freakbob is calling! that wasn't the answer i was looking for, but it's a good one! you have earned 50 aura points.")
      aura += 50
    else:
      print("incorrect! clearly you have no one cause it seems like you dont know what it looks like when someone is calling you. you have lost 100 aura points.")
      aura -= 100
    print("you currently have " + str(aura) + " aura points.")
    print("question 3:")
    q3 = str(raw_input("what type of surgery is tomorrow?"))
    if q3 == "knee":
      print("correct! knee surgery is tomorrow and i have that feeling when knee surgery is tomorrow. you have earned 100 aura points.")
      aura += 100
    elif q3 == "plastic":
      print("you are not kanye's ex wife. you have lost 100 aura points.")
      aura -= 100
    else:
      print("incorrect! you have lost 100 aura points.")
      aura -= 100
    print("you currently have " + str(aura) + " aura points.")
    print("question 4:")
    q4 = str(raw_input("who is the king of rizz?"))
    if q4 == "rizzler" or q4 == "the rizzler":
      print("correct! the rizzler is the king of rizz. you know him as the rizzler, he's the panther dressed in black, and when he gives your girl the rizz face there's no chance she's going back! you have earned 100 aura points.")
      aura += 100
    elif q4 == "duke dennis" or q4 == "duke":
      print("duke dennis is not the king of rizz, but he is pretty rizzy. you have earned 50 aura points.")
      aura += 50
    elif q4 == "baby gronk":
      print("baby gronk is not the king of rizz, but he is pretty rizzy. you have earned 50 aura points.")
      aura += 50
    else: 
      print("incorrect! i've never heard of this rizzler. you have lost 100 aura points.")
      aura -= 100
    print("you currently have " + str(aura) + " aura points.")
    q4 = str(raw_input("who taxes you?"))
    if q4 == "fanum" or q4 == "fanum tax":
      print("correct! you have earned 100 aura points.")
      aura += 100
    elif q4 == "irs" or q4 == "the irs" or q4 == "the government" or q4 == "government":
      print("incorrect! only fanum is allowed to tax sigmas. you have lost 100 aura points.")
      aura -= 100
    else:
      print("incorrect! you have lost 100 aura points.")
      aura -= 100
    print("you currently have " + str(aura) + " aura points.")
    q5 = str(raw_input("what is the best podcast?"))
    if q5 == "talk tuah":
      print("hawk tuah spit on that thang! you got it correct! you have earned 100 aura.")
      aura += 100
    elif q5 == "ear biscuits":
      print("yesssuuhhhhhh")
      aura += 500
    elif q5 == "joe rogan" or q5 == "rogan":
      print("bruh, get a job")
      aura -= 100
    else:
      print("incorrect! you have lost 100 aura.")
      aura -= 100
    print("you currently have " + str(aura) + " aura points.")
    q6 = str(raw_input("how do you like your cheese?"))
    if q6 == "drippy" or q6 == "drippy bruh":
      print("i like my cheese drippy bruh. you have earned 100 aura.")
      aura += 100
    elif q6 == q6 == "grippy" or q6 == "grippy bruh":
      print("nahh you FREAKY freaky. i respect it tho, you have earned 150 aura")
      aura += 150
    else:
      print("incorrect! you have lost 100 aura")
      aura -= 100
    print("you currently have " + str(aura) + " aura points.")
    q7 = str(raw_input("finish the sentence. we bring the ____!"))
    if q7 == "BOOM" or q7 == "boom" or q7 == "BOOM!" or q7 == "boom!":
      print("WE BRING THE BOOM! correct! you have earned 100 double chunk chocolate cookies.")
      aura += 100
    else: 
      print("incorrect! you have lost 100 aura.")
      aura -= 100
    print("you currently have " + str(aura) + " aura points.")
    print("CONGRATULATIONS! you have completed the test!")
    print("you finished the test with a total of " + str(aura) + " aura points!")
  elif sigma == "n" or sigma == "no" or sigma == "nope" or sigma == "nah":
    print("not sigma.")
    alpha = str(raw_input("are you at least an alpha?"))
    if alpha == "y" or alpha == "yes" or alpha == "yep" or alpha == "yup" or alpha == "yea" or alpha == "yeah":
      print("you're still not a sigma.")
    elif alpha == "n" or alpha == "no" or alpha == "nope" or alpha == "nah":
      print("you're not even an alpha? smh.")
    else:
      print("answer with y/n")
  else: 
    print("answer with y/n")
sigmabot()
