#HANGMAN Virtual Learning Edition



import random

#creating a function to get the rules from the game_rules.txt file
def get_rules():
    txt_file = open("game_rules.txt", "r")
    rules = txt_file.read()
    print (rules)

#starting text for the user and displaying the rules
print ("Lets play Hangman!")
print ("Here are the Rules:")
get_rules()

#created my own list of words related to online learning
list_of_words = ["zoom", "webcam", "mute", "email", "wfh","capstone", "covid", "online", 
    "Microsoft", "mask", "computer", "laptop", "virtual", "outlook"]

#grabbed a random word from the list and created an empty list of already guessed letters
random_word = random.choice(list_of_words)
    
already_guessed = []

#function to add letters to the already guessed list and let the user know which letters they have already guessed
def collection_of_guesses(letter):
    already_guessed.append(letter)
    print ("Letters you have already guessed", already_guessed)


#function to display how many turns are left 
def turns(guess):
    print ("you have", guess, "guesses left")
    
#function to display the hangman guy
def display_man(tries):
    man = ["YOU KILLED THE MAN", """
     
    O  
        
        
       """, """
    
    O   
    |   
        
       """, """
    
    O   
   /|   
        
       """, """
    
    O   
   /|\  
        
       """, """
    
    O   
   /|\  
   /    
       """, """
    
    O   
   /|\  
   / \  
       """]
    print(man[tries])



#main gameplay function
def hangman():
    #pick a random word & print it with blank underscores to let the user know how many letters are in the word
    random_word = random.choice(list_of_words)
    
    hangman_blank = "_ " * len(random_word)

    print(hangman_blank)

    #establish a guesses limit, a binary for the while loop and an incorrent guesses count
    guesses = 10

    gameplay = True

    incorrect_guesses = 7

    #main while loop
    while gameplay and guesses > 0 and incorrect_guesses > 0:
    
        #asks the user to enter a letter, converts it to lowercase 
        guessed_letter = input("Please enter a letter to guess: ").lower()

        #ensures the user is only entering 1 letter and it is a letter
        if len(guessed_letter) == 1 and guessed_letter.isalpha():

            #if the letter is not in the word: print a message, 
            # let the user know if they have already guessed this letter,
            # add it to thier collection of guesses, 
            # add to thier turn count and incorrect guess count, display the man 
            if guessed_letter not in random_word:
                print(guessed_letter, " is not in the word")
                if guessed_letter in already_guessed:
                    print("you already guessed this letter")
                else:
                    collection_of_guesses(guessed_letter)
                    guesses -= 1
                    turns(guesses)
                    incorrect_guesses -= 1
                    display_man(incorrect_guesses)
            
            #else the letter is in the word, print a message to the user, add to thier guesses
            # and add the letter to thier guessed letters list
            else:
                print ("Correct!", guessed_letter, " is in the word!")
                if guessed_letter in already_guessed:
                    print ("although, you already guessed this letter!")
                else:
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

        #if the user enters the whole word and guesses it correctly            
        elif guessed_letter == random_word:
            print ("You guessed the word!")
            gameplay = False
        #if the user enters something other than a letter
        else:
            print ("please enter a valid input or the full correct word")

    #End of while loop ad end of game, let the user know, 
    # the game is over, what the word was and what letters they guessed
    print("Game Over")
    print("The word was", random_word,"!")
    print("Here are the letters you guessed: ", already_guessed)

#call the function
hangman()
     
