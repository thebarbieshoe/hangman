# In this exercise, the task is to write a function that picks a random word
# from a list of words from the SOWPODS dictionary.

# Currently player only has 6 guesses



# STEP ONE: Pick a random number which will correspond with the dictionary
import random
import turtle

def main():
    intro()
    a = random.randint(0, 267751)
    # Open file
    with open ('dictionary.txt', 'r') as open_file:
        # read one specific line, the randomly picked line number
        for i, line in enumerate(open_file):
            if i == a:
               line=open_file.readline()
               hangman_word = line.rstrip()
               #print(hangman_word)
    guess_letter(hangman_word)
    user_choice = (input("Would you like to play again? (Y/N)")).capitalize()
    if user_choice == "Y" or user_choice == "YES":
        main()
    else:
        print("Thank you for playing! Have a good day!")
    
# This function will parse through the hangman_word and decide if the user's
# input matches any letters in the word
def guess_letter(word):
    wrong_count = 0
    LENGTH = len(word)
    # create variable to keep track of what the user has guessed
    userguessedword = []
    for p in range(LENGTH):
        userguessedword.append('_')
    # display current word/number of blanks
    display_userword(userguessedword)
    print()
    
    # Let user have 6 guesses
    for x in range(6):
        letter = (input("Guess your letter: ")).capitalize()

        if is_match(word,letter) == True:
            print ("Correct!", end=" ")
            # add the correct letter to userguessedword variable
            for y in range(LENGTH):
                if letter == userguessedword[y]:
                    print("But you already guessed", letter, ". Try again.")
                    letter = (input("Guess your letter: ")).capitalize()
                elif letter == word[y]:
                    userguessedword[y] = letter
            display_userword(userguessedword)
            print("You have", 5-x, "more guesses")
            
        else:
            print("Incorrect!")
            wrong_count += 1
            draw_man(wrong_count)
            print("You have", 5-x, "more guesses")
        

    user_guess = (input("Guess the word: ")).capitalize()
    if user_guess == word:
        print ("YOU WIN!")
    else:
        print("YOU LOSE!")
        
def is_match(word,letter):
    result = False
    for x in range(len(word)):
        if letter == word[x]:
            return True

def intro():
    print("Hello! Welcome to Hangman!")
    print("You will have 6 chances to guess letters.")

def display_userword(word):
    for l in range(len(word)):
        print(word[l], end=" ")
    print()

def draw_man(count):
    myTurtle = turtle.Turtle()
    myTurtle.hideturtle()
    if count == 1:
        #draw a circle for head
        #start up higher and hide cursor
        myTurtle.penup()
        myTurtle.setposition(0,200)
        myTurtle.pendown()
        myTurtle.circle(50)
    if count == 2:
        # second time wrong
        myTurtle.penup()
        myTurtle.setposition(0,200)
        myTurtle.right(90)
        myTurtle.pendown()
        myTurtle.forward(200)
    if count == 3:
        myTurtle.penup()
        myTurtle.setposition(0,0)
        myTurtle.right(45)
        myTurtle.pendown()
        myTurtle.forward(175)
    if count == 4:
        myTurtle.penup()
        myTurtle.setposition(0,0)
        myTurtle.left(225)
        myTurtle.pendown()
        myTurtle.forward(175)
    
    
main()


