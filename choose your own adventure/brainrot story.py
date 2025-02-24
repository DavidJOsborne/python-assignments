import time
while True:
  start = raw_input("Are you ready to start your freaky haircut adventure? \n y/n \n")
  print("")
  if start == "n":
    print("Too bad, you're going on this freaky haircut adventure whether you like it or not.\n")
  elif start == "y":
      print("Okay weirdo, why are you so desperate for a freaky haircut? \nI guess you can go on the freaky haircut adventure, but just know you're weird for it. \n")
  print("INTRODUCTION \n")
  print("You walk out of your LA mansion. Today is the day you will be getting your hair cut, you just don't know it yet.\n")
  print("PART ONE: The Begining\n")
  print("You wake up. \nToday is errand day, not your favorite, but you still like it because you get to spend money on stuff.\n")
  outta = raw_input("Get out of bed? \n\n Select an option: \n 1. Just five more minutes \n 2. Okay fine, I'll get up. \n 3. ???\n")
  if outta == "1":
    print("You close your eyes, hoping to get just five more minutes of sleep, but you end up sleeping until 8:22 pm, ruinimg your errand day.\n")
    tryagain = raw_input("Try again? y/n\n")
    if tryagain == "y":
      print("There are no do-overs, you failed.")
    else: 
     print("Pathetic.")
  elif outta == "2":
    print("You get out of bed, stretch, and get ready for the day.\n")
    vehicle = raw_input("How will you get to the store?\n 1. Walk\n 2. Lambo\n 3. Tesla\n 4. Bike\n")
    if vehicle == "1":
      print("Great choice! Walking is a great form of excersize! \n You go out the door and start walking in the direction of the nearest Target.\n")
      distance = 0
      time.sleep(2)
      while distance < 2253:
        time.sleep(1)
        distance += 1
        print "You have traveled", str(distance * 3), "feet, only", str(13728 - (distance * 3)), "feet left to go until Target.\n"
      print("You have been hit by a car and killed.\n")
      break
    elif vehicle == "2":
      print("You decide to take the lambo. \n You grab your Lambo keys and head to your garage, as you pull out of the driveway a car whizzes by, that was a close one.")
      print("You get to Target and get out of your vehicle, but unfortunately a boat falls out of the sky and lands on your head.")
      break
    elif vehicle == "3":
      print("You decided to take your Tesla. \n When you arrive to Target you notice a Sports Clips and realize how long your hair has gotten.\n")
      low = raw_input("1. Continue to Target\n2. Forget the groceries, I'm getting a haircut.\n")
      if low == "1":
        print("You walk into target, oh no, you forgot your shopping list!\nYou burst into flames spontaneously, your skin starts to char and peel, you scream out in agony 'WHY DIDNT I GET A LOW TAPER FADE?!'")
        break
      elif low == "2":
        print("You enter the Sports Clips, it seems busy, it makes sense since the custer base is MASSIVE.\n'You wanna know what else is massive?' says the lead hair stylist.\n'What?' you respond.")
        print("'Sit down' says the stylist.\n 'Uh, okay' you say\n")
        print("The hair stylist begins combing, cutting, buzzing, and shaving. Smoke begins to come off your head as hair flies everywhere.\n'LLLLOOOOOOOOOOOWWWWWWW TAPERRRRRRRR FAAADDEEEEEE' says the stylist.\n the cloud of smoke and hair subsides and you see yourself in the mirror. You havent seen anything more beautiful. 'Thats crazy' you say, 'No, its massive'.\n")
        print("The MASSIVE end.")
        break
    elif vehicle == "4":
      print("You chose to take your bike, but it has a flat tire dummy.")
      break
  elif outta == "3":
    print("restart.\n")
    break
