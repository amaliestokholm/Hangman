"""
A very short game of Hangman. The secret_word is the word, the user is
suppose to guess. The user/player have 10 turns.
"""

print('Hello and welcome to Hangman!')

secret_word = 'hangman'
secret_word = secret_word.upper()
life = 10
guesses = ''

while life > 0:
    # Fails counts the missing letters
    fails = 0
    for char in secret_word:
        if char in guesses:
            print(char)
        else:
            print('_')
            fails += 1

    if fails == 0:
        print('You won!')
        break

    # This lets the user come with an input
    print('Guess:')
    guess = input()
    guess = guess.upper()
    guesses += guess

    if guess not in secret_word:
        life -= 1
        print('Wrong, you have %s lifes left' % life)
    if life == 0:
        print('You Loose!')
