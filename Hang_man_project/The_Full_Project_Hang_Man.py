def Open_Game():
    """
    print the post screen of the game
    :return:
    """

    HANGMAN_ASCII_ART = ("""
  _    _
 | |  | |
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \\
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |
                     |___/

""")
    print(HANGMAN_ASCII_ART + "the tries you have: " + str(7))


def choose_word(file_path, index):
    """
    get file and index it return the secret word from a file with words.
    :param file_path: file
    :param index: int
    :return: the_word = the secret word
    retype: string
    """
    dict_of_words = {}  # list of all the words in the file without deplucation
    with open(file_path, "r") as file:
        for line in file:
            singals_word = line.split(" ")  # all the words in the file.
    for word in range(len(singals_word)):
        check_if_double = 0  # it give me the option to know if there is aword in my dict and then i can know if i need to add the word to the dict
        for apper in dict_of_words:
            if singals_word[word] == dict_of_words[apper]:
                check_if_double = 1
                break
        if check_if_double == 0:
            dict_of_words[word + 1] = singals_word[word]
    long = len(singals_word)
    len_of_the_list_words = index % long
    len_of_words_without_dobles = len(dict_of_words)  # this is what my retun value will be the numbers of words
    the_word = dict_of_words[len_of_the_list_words]  # this is my secert word
    The_Answer = (len_of_words_without_dobles, the_word)
    return the_word  # i cchange it to the word because you asked from us to reurn only the world


def check_valid_input(letter_guessed, old_letters_guessed):
    """
    the func checking if the letter is in the list of the guessed and if the letter is ok
    :param letter_guessed: string
    :param old_letters_guessed: list
    :return: True or False
    """
    if old_letters_guessed == []:
        return True
    bool = True
    if (len(letter_guessed) == 1) and (letter_guessed.isalpha()):
        for i in old_letters_guessed:
            if i == letter_guessed:
                bool = False
        return bool
    else:
        return bool


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
     checking if the letter is valid if it is he check if he part of the list and if it is not  in the list it add it
     to the list else print error
    :param letter_guessed: string
    :param old_letters_guessed: list
    :return: True or False if the letter add to the list if didn't  it print a message
    """
    if check_valid_input(letter_guessed, old_letters_guessed):  # exercise 6.4.1 use the function
        old_letters_guessed += letter_guessed
        return True
    else:
        arrow = " -> "
        arrow = arrow.join(old_letters_guessed)
        print("X\n" + arrow + "\nFalse \nguess another letter")
        return False


def is_valid_input(letter_guessed):
    """
    check if the letter stanג in the standards of normality
    :param letter_guessed:string
    :return: True Or False
    """
    if letter_guessed.isalpha():
        if len(letter_guessed) == 1:
            return True
        else:
            print("E1 -> you need to write only 1 letter in english")
            return False
    else:
        if len(letter_guessed) == 1:
            print("E2 -> you need to write only english letter")
            return False
        else:
            print("E3 -> you need to write only 1 letter in english")
            return False


def print_hangman(num_of_tries):
    """
    it gets the number of mistakes the player did and print the position of him
    :param num_of_tries: int
    :return: null
    """
    HANGMAN_PHOTOS = {1: '''x-------x'''
        , 2: '''x-------x
|
|
|
|
|'''
        , 3: '''x-------x
|       |
|       0
|
|
|'''
        , 4: '''x-------x
|       |
|       0
|       |
|
|'''
        , 5: '''x-------x
|       |
|       0
|      /|\\
|
|'''
        , 6: '''x-------x
|       |
|       0
|      /|\\
|      /
|'''
        , 7: '''x-------x
|       |
|       0
|      /|\\
|      / \\
|'''}
    for i in HANGMAN_PHOTOS:
        if i == num_of_tries:
            print(HANGMAN_PHOTOS[i])


def show_hidden_word(secret_word, old_letters_guessed):
    """
    print the secert word with the letters that the player already guessed  and True or False if  the letter part of the
    word
    :param secret_word: string
    :param old_letters_guessed: list
    :return: bool
    retype: boolean
    """
    bool = True
    string = " "
    for i in secret_word:
        if i in old_letters_guessed:
            string += " " + str(i)
            bool = False  # retun False if the letter part of the word
        else:
            string += " _"
    print("the letters you already guessed:{0} \n {1} ".format(str(old_letters_guessed), string))
    return bool


def check_win(secret_word, old_letters_guessed):
    """
    check if the player win. if he win it return True. checking if all the letters that the player guessed is in the
    secret word
    :param secret_word: string
    :param old_letters_guessed: list
    :return: null
    """
    for i in secret_word:
        if i in old_letters_guessed:
            pass
        else:
            return False
    print("the word is: {0}".format(secret_word))
    return True


def check_if_letter_is_part_of_the_word(secert_word, the_guess):
    """
    check if the letter part of the word
    :param secert_word: string
    :param the_guess: string
    :return: True or False
    """
    for i in secert_word:
        if the_guess == i:
            return True
    return False


def start_tne_game(old_letters_guessed):
    """
    get the list of the letters we guessed and restart the list for a new game and restart the index
    :param old_letters_guessed:  list
    :return: index
    retype: int
    """
    old_letters_guessed.clear()
    index = int(input("Enter index: "))
    print("Let’s start again!")
    print_hangman(1)
    return index


def main():
    """
    the main pogram, the game.
    :return: null
    """
    asking = 0  # int that decide if the player want to play again
    num_of_tries = 1
    check_if_win = False
    old_letters_guessed = []
    Open_Game()
    null = True
    file_path = input("Enter file path: ")
    index = int(input("Enter index: "))
    print("Let’s start!")
    print_hangman(num_of_tries)
    secret_word = choose_word(file_path, index)  # file_path instead the text
    len_secret_word = len(secret_word)
    print("\t" + "GOOD LUCK:  " + "_ " * len_secret_word)
    while null:
        the_guess = input("Guess a letter^^^: ").lower()
        check1 = is_valid_input(the_guess)
        if check1 is True:  # check if the value we input is good
            check1 = try_update_letter_guessed(the_guess, old_letters_guessed)  # update the list of the letters we
            # guessed and return true if is a new word
            check2 = check_if_letter_is_part_of_the_word(secret_word, the_guess)  # check2 is boolean and if it true
            # the guess is part of the secret word
            if check1:
                if not check2:
                    num_of_tries += 1
                    print(":( \n {0}".format(print_hangman(num_of_tries)))
                    show_hidden_word(secret_word, old_letters_guessed)
                else:
                    show_hidden_word(secret_word, old_letters_guessed)
            if check_win(secret_word, old_letters_guessed):
                asking = int(input("you win my friend :) \ndo you want play another game? 1 for yes and 0 for no"))
                if asking == 1:
                    index = start_tne_game(old_letters_guessed)
                    num_of_tries = 1
                    asking = -1
                else:
                    null = False
        if (num_of_tries == 7) and (null is True) and (asking != 1):
            asking = int(input("You lose. \ndo you want to play again ? 1 for yes and 0 or no: "))
            if asking == 1:
                index = start_tne_game(old_letters_guessed)
                num_of_tries = 1
                asking = 0
            else:
                null = False


if __name__ == '__main__':
    main()
