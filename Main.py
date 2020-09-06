#HANGMAN Virtual Learning Edition

#Please refer to the Game Rules File to learn how to play the game


import random


print ("Lets play!")



list_of_words = ["zoom", "webcam", "mute", "email", "wfh", "covid", "online", 
    "Microsoft", "mask", "computer", "laptop", "virtual", "outlook"]

random_word = random.choice(list_of_words)
    
already_guessed = []


def collection_of_guesses(letter):
    already_guessed.append(letter)



def turns(guess):

    print ("you have", guess, "guesses left")
    


def hangman():
    random_word = random.choice(list_of_words)
    
    hangman_blank = "_ " * len(random_word)

    print(hangman_blank)

    guesses = 6

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
                if guessed_letter in already_guessed:
                    print("you already guessed this letter")
                else:
                    collection_of_guesses(guessed_letter)
                    guesses -= 1
                    turns(guesses)
                    print ("Letters you have already guessed", already_guessed)
            
            #elif the letter has already been guessed, let the user know and add to thier guesse attempts
            elif guessed_letter in already_guessed:
                print ("you have guessed this letter already!")
                guesses -= 1
                turns(guesses)
            #else the letter is in the word, print a message to the user, add to thier guesses
            # and add the letter to thier guessed letters list
            else:
                print ("Correct!", guessed_letter)
                collection_of_guesses(guessed_letter)
                guesses -= 1
                turns(guesses)
            
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

    print("Game Over")
    print("Here are the letters you guessed: ", already_guessed)

hangman()
     
