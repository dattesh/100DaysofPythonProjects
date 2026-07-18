import random



#Lives
lives =6
#List from where word will be Display
word_list=['aardvark','baboon','camel']
#Select random  word from word list
chosen_word=random.choice(word_list)
print(chosen_word)

# Check the Length of chosen_word and Print _ of chosen word's size
word_length=len(chosen_word)
#Create a Placeholder to Print _  of word_length
placeholder = ""

for position in range(word_length) :
    placeholder += '-'
print(placeholder)


# Let the user guess the word
game_over = False
correct_letters=[]

while not game_over:
    guess =input('guess a letter').lower()

    #Check guess letter is in chosen_word
    display =''

    for letter in chosen_word :
        if letter == guess :
            display += guess
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else :
            display += '_'
    print(display)

    if guess not in chosen_word:
        lives -= 1
        if lives > 0:
            print(f"you have {lives} lives")
        if lives == 0:
            game_over =True
            print("you lose")


    if "_" not in display:
        game_over = True
        print('you win')
