import time
import random

name=input("What is your name?")

print("Hello,"+ name,"Time To Play!")

#wait for 1 second
time.sleep(1)

print("Start guessing...")
time.sleep(0.5)

#here we set the secret
words=["adventure","relive","ability","absolute","accurate"]

word = random.choice(words)

#create an empty variable
guesses=" "

#determine number of turns
turns=10

#check if the turn is less than zero or not
while(turns>0):
    #make a counter that starts with zero

    failed=0

    #for every character in secret_word
    for char in word:
    #see if the character is in the player's guess
       if char in guesses:

        print (char)

       else:
          # if not found print dash
          print("_")

          failed +=1

    if failed == 0:
        print("YOU WON!!")
        break

    guess = input("Guess a character:")

    #set the players guess to guesses
    guesses += guess

    #if the guess is not found in the secret word
    if guess not in word:

        #turns counter decreases with 1
        turns-=1

        print("Wrong")
        #how many turns are left
        print("You have ",+ turns, "more guesses")

        #if the turns are equal to zero
        if turns ==0:
            print("You Lose")
            
    
    
        
        

