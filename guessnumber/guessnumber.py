import random
def go_guess():
    secret = random.randint(1,20)
    print('I have a number between one and twenty')
    guesses = 0
    while True:
      guess = int(raw_input("guess: "))
      if guess != secret:
        guesses += 1
        if guess > secret:
          print guess, 'is too high'
          # print 'My number was', secret
        else:
          print guess, 'is too low'
          # print 'My number was', secret
      else: 
        print "Right, my numer is", guess
        print "It took you ", guesses, " guesses"
        break
        
go_guess()
