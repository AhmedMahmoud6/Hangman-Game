# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    is_guessed = False
    for i in secret_word:
        if i in letters_guessed:
            is_guessed = True
        else:
            is_guessed = False
            break

    return is_guessed


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    result = ''
    for i in secret_word:
        if i in letters_guessed:
            result += i
        else:
            result += '_ '
    return result


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    words = string.ascii_lowercase
    result = ''
    for i in words:
        if i not in letters_guessed:
            result += i
    return result


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''

    index_buffer = 0
    is_true = True
    my_word = my_word.replace("_ ", "_")
    print(my_word)
    if len(my_word) != len(other_word):
        return False
    else:
        for i in my_word:
            if i != '_':
                if i == other_word[index_buffer]:
                    is_true = True
                    index_buffer += 1
                else:
                    is_true = False
                    break
            else:
                if other_word[index_buffer] in my_word:
                    is_true = False
                    break
                else:
                    is_true = True
                    index_buffer += 1

    return is_true


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------
def len_unique_letters_dict(secret_word):
    my_dict = {}

    for i in secret_word:
        my_dict[i] = 'True'

    return len(my_dict)


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    guesses = 6
    warnings = 3
    user_guess_list = []
    vowels = ['a', 'e', 'i', 'o', 'u']

    print('welcome to the game hangman!')
    print(f'I am thinking of a word that is {len(secret_word)} letters long')
    print('-----------------')

    while True:
        if is_word_guessed(secret_word, user_guess_list) is False and guesses < 1:  # the loss condition
            print("YOU DIDN'T CATCH THE WORD... YOU LOST!")
            print(f"The word was: {secret_word}")
            break

        elif is_word_guessed(secret_word, user_guess_list):  # the win condition
            total_score = guesses * len_unique_letters_dict(secret_word)  # calculates the score
            print("Congratulations! you guessed the word right!")
            print(f'Your score is: {total_score}')
            break

        print(f'you have {guesses} guesses left')
        userinput = input('please guess a letter: ').lower()  # user input lowercase

        if len(userinput) > 1:  # to prevent the user from typing more than one letter
            print("That's more than one letter... try again")
            continue

        for i in user_guess_list:  # the letter repetition checker
            if i == userinput:
                if warnings < 1:
                    guesses -= 1
                    print('You have no warnings left so you lose one guess')
                else:
                    warnings -= 1
                    if warnings != 0:
                        print(f'Oops! You have already guessed that letter. you have {warnings} warnings left: {get_guessed_word(secret_word, user_guess_list)}')
                    else:  # if warnings is 0
                        guesses -= 1
                        print('You have no warnings left so you lose one guess')

        if not str.isalpha(userinput) and userinput not in user_guess_list:  # makes sure if it's alpha or not
            if warnings < 1:
                guesses -= 1
                print('You have no warnings left so you lose one guess')
            else:
                warnings -= 1
                if warnings != 0:
                    print(f'Oops! That is not a valid letter. you have {warnings} warnings left: {get_guessed_word(secret_word, user_guess_list)}')
                else:  # if warnings is 0
                    guesses -= 1
                    print('You have no warnings left so you lose one guess')
            continue

        elif userinput in secret_word and userinput not in user_guess_list:  # if the word is in the secret word
            user_guess_list.append(userinput)  # we add the guessed word to the user_guess_list array
            print('Good guess: ' + get_guessed_word(secret_word, user_guess_list))

        elif userinput not in secret_word and userinput not in user_guess_list and userinput not in vowels:  # consonant letters
            user_guess_list.append(userinput)  # we add the guessed word to the user_guess_list array
            print('that letter is not in my word: ' + get_guessed_word(secret_word, user_guess_list))
            guesses -= 1

        elif userinput not in secret_word and userinput not in user_guess_list and userinput in vowels:  # vowels letters
            user_guess_list.append(userinput)  # we add the guessed word to the user_guess_list array
            print('that letter is not in my word: ' + get_guessed_word(secret_word, user_guess_list))
            guesses -= 2

        print('Available letters: ' + get_available_letters(user_guess_list))
        print('-----------------')


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.
    '''
    is_true = False
    similar_words = []
    my_word = my_word.replace("_ ", "_")
    for i in wordlist:
        if len(i) == len(my_word):
            for j in range(0, len(my_word)):
                if my_word[j] != "_":
                    if my_word[j] == i[j]:
                        is_true = True
                    else:
                        is_true = False
                        break
        if is_true:
            similar_words.append(i)

    if len(similar_words) == 0:
        return 'No matches found'
    else:
        return similar_words


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    guesses = 6
    warnings = 3
    user_guess_list = []
    vowels = ['a', 'e', 'i', 'o', 'u']

    print('welcome to the game hangman!')
    print(f'I am thinking of a word that is {len(secret_word)} letters long')
    print('-----------------')
    while True:
        if is_word_guessed(secret_word, user_guess_list) is False and guesses < 1:  # the loss condition
            print("YOU DIDN'T CATCH THE WORD... YOU LOST!")
            print(f"The word was: {secret_word}")
            break

        elif is_word_guessed(secret_word, user_guess_list):  # the win condition
            total_score = guesses * len_unique_letters_dict(secret_word)  # calculates the score
            print("Congratulations! you guessed the word right!")
            print(f'Your score is: {total_score}')
            break

        print(f'you have {guesses} guesses left')
        userinput = input('please guess a letter: ').lower()  # user input lowercase

        if len(userinput) > 1:  # to prevent the user from typing more than one letter
            print("That's more than one letter... try again")
            continue

        if userinput == "*":
            if match_with_gaps(get_guessed_word(secret_word, user_guess_list),secret_word):
                print(show_possible_matches(get_guessed_word(secret_word, user_guess_list)))

        for i in user_guess_list:  # the letter repetition checker
            if i == userinput and i != '*':
                if warnings < 1:
                    guesses -= 1
                    print('You have no warnings left so you lose one guess')
                else:
                    warnings -= 1
                    if warnings != 0:
                        print(f'Oops! You have already guessed that letter. you have {warnings} warnings left: {get_guessed_word(secret_word, user_guess_list)}')
                    else:  # if warnings is 0
                        guesses -= 1
                        print('You have no warnings left so you lose one guess')

        if not str.isalpha(userinput) and userinput not in user_guess_list and userinput != '*':  # makes sure if it's alpha or not
            if warnings < 1:
                guesses -= 1
                print('You have no warnings left so you lose one guess')
            else:
                warnings -= 1
                if warnings != 0:
                    print(f'Oops! That is not a valid letter. you have {warnings} warnings left: {get_guessed_word(secret_word, user_guess_list)}')
                else:  # if warnings is 0
                    guesses -= 1
                    print('You have no warnings left so you lose one guess')
            continue

        elif userinput in secret_word and userinput not in user_guess_list:  # if the word is in the secret word
            user_guess_list.append(userinput)  # we add the guessed word to the user_guess_list array
            print('Good guess: ' + get_guessed_word(secret_word, user_guess_list))

        elif userinput not in secret_word and userinput not in user_guess_list and userinput not in vowels and userinput != '*':  # consonant letters
            user_guess_list.append(userinput)  # we add the guessed word to the user_guess_list array
            print('that letter is not in my word: ' + get_guessed_word(secret_word, user_guess_list))
            guesses -= 1

        elif userinput not in secret_word and userinput not in user_guess_list and userinput in vowels and userinput != '*':  # vowels letters
            user_guess_list.append(userinput)  # we add the guessed word to the user_guess_list array
            print('that letter is not in my word: ' + get_guessed_word(secret_word, user_guess_list))
            guesses -= 2

        print('Available letters: ' + get_available_letters(user_guess_list))
        print('-----------------')



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############

# To test part 3 re-comment out the above lines and
# uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
