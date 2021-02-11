word = input ('insert a word: ')
word = word.lower()
show_word = '_' *len(word)
print('\n' * 100)

count = 0 
guesses = 10
guessed_letter =set()

while True:
    guess = input(f'guess a letter or word: {show_word}\n')
    print (f'your guess {guessed_letter}')
    if len(guess) == 1:
        guessed_letter.add(guess.lower())
        show_word = ''.join([c if c in guessed_letter else '_' for c in word])
        if '_' not in show_word:
            print(f'you guessed the word: {word}')
            break
    if len(guess) > 1:
        if guess == word:
             print (f'you gessd the word: {word}')
             break
        else:
             print(f'{guess} you worng')
    guesses -=1
    if not guesses:
         print(f' sorry, the game has ended. the word was {word}')
         break
        
