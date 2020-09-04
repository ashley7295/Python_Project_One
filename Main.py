#HANGMAN Virtual Learning Edition

#User will input when they are ready to start and 
# the game will randomly generate 1 of 13 words related to virtual learning. 
#The game will then ask the user to enter a letter and output an updated "_ _ _ _" type template
#The game will give the user 10 Gueses before they lose the game


import random

#create a list of words, this could be its own file that i call in
list_of_words = ["zoom", "webcam", "mute", "email", "wfh", "covid", "online", 
"Microsoft", "mask", "computer", "laptop", "virtual", "outlook"]


#select a random word from the list
random_word = random.choice(list_of_words)

print ("Lets play!")

#changing all characters in the word to an underscore, this is where i first got stuck
hangman = "_ " * len(random_word)

print(hangman)

#gives the user 10 trys to achieve the word, adds each guess into a list and a binary is created to work the while loop
guesses = 10

already_guessed = []

gameplay = True

while gameplay and guesses > 0:
    
    #asks the user to enter a letter, converts it to lowercase 
    guessed_letter = input("Please enter a letter to guess: ").lower()

    #ensures the user is only entering 1 letter and it is a letter
    if len(guessed_letter) == 1 and guessed_letter.isalpha():

        #if the letter is not in the word: print a message, 
        # add to our guesses and print the list of guesses
        if guessed_letter not in random_word:
            print(guessed_letter, " is not in the word")
            already_guessed.append(guessed_letter)
            guesses -= 1
            print ("Letters you have already guessed", already_guessed)
        #elif the letter has already been guessed, let the user know and add to thier guesse attempts
        elif guessed_letter in already_guessed:
            print ("you have guessed this letter already!")
            guesses -= 1
        #else the letter is in the word, print a message to the user, add to thier guesses
        # and add the letter to thier guessed letters list
        else:
            print ("Correct!", guessed_letter)
            already_guessed.append(guessed_letter)
            guesses -=1
            
            #create a string for displaying to the user
            display = str()
            #for each character in the random word, replace it with the guessed letter or use "_"
            for char in random_word:
                display += char if char in already_guessed else " _"
            #print the displayed string
            print (display)
            
            print("Letters you have already guessed", already_guessed)
            #if the display string is the word, let the user know they have guessed the word
            if display == random_word:
                print ("You win! the word was: ", random_word)
                #turn the game play "off" or false
                gameplay = False
    #if the user enters the whole word and guesses it correctly            
    elif guessed_letter == random_word:
        print ("You guessed the word!")
        gameplay = False
    #if the user enters something other than a letter
    else:
        print ("please enter a valid input")

           
#end of game
print("Game Over")
print("Here are the letters you guessed: ", already_guessed)

     
