import random
import string

words = ["ema"]

# randomly valib sõna list 
def get_valid_word(words):
    word = random.choice(words) 
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 7

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        print('Sul on', lives, 'elud alles ja sa oled kasutanud need tähed ära: ', ' '.join(used_letters))

        # Mis praegune sõna  (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Praegune sõna : ', ' '.join(word_list))
        
        #pakku täht
        user_letter = input('pakku täht: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  #võttab elu maha
                print('\nSinu tähed,', user_letter, 'ei ole sõnas.')
                
        #error
        elif user_letter in used_letters:
            print('\nJuba oled arvasid seda tähte ')

        else:
            print('\nSee ei ole valid täht.')
            
            
    #kui sured ära
    if lives == 0:
        print(lives_visual_dict[lives])
        print('Sa surid. Sõna oli', word)
    else:
        print('Tubli poiss! Hinne 5!',"sõna oli", word, '!!') #kui võidad

#kuvastab pilte kui valesti paned
if __name__ == '__main__':
    
    lives_visual_dict = {
        0: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |         / \\
               |
           """,
        1: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |         / 
               |
            """,
        2: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |          
               |
            """,
        3: """
                ___________
               | /        | 
               |/        ( )
               |          
               |          
               |
            """,
        4: """
                ___________
               | /        | 
               |/        
               |          
               |          
               |
            """,
        5: """
                ___________
               | /        
               |/        
               |          
               |          
               |
            """,
        6: """
               |
               |
               |
               |
               |
            """,
        7: "",
    }
    
hangman()