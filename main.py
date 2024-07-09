import random
import hangman_words
import hangman_art
# from hangman_words import word_list
print(hangman_art.logo)
choosen_word=(random.choice(hangman_words.word_list))
# print(choosen_word)
lives=6
display=[]
for i in range(0,len(choosen_word)):
    display.append("__")
print(display)  
end_of_game=False
while not end_of_game:
    guess=input("Guess a letter:").lower()
    if guess in display:
        print(f"you've already guessed {guess}word.You loose a life")
    for position in range(len(choosen_word)):
    # for letter in range(0,len(choosen_word)): only use for asining rangeto "letter"
        # print(letter)
        letter=choosen_word[position]
        if guess==letter:
            display[position]=letter
    if guess not in choosen_word:
        lives-=1    
        if(lives==0):
            end_of_game=True
            print("you loose")
    print(display)
    if "__" not in display:
        end_of_game=True
        print("you win")
    print(hangman_art.stages[lives])
       