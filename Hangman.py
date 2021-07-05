import requests, random

word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"

response = requests.get(word_site)
words = response.content.splitlines()
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

hangmen = {
    1: ' +---+\n     |\n     |\n     |\n    ===',
    2: ' +---+\n O   |\n     |\n     |\n    ===',
    3: ' +---+\n O   |\n |   |\n     |\n    ===',
    4: ' +---+\n O   |\n/|   |\n     |\n    ===',
    5: ' +---+\n O   |\n/|\  |\n     |\n    ===',
    6: ' +---+\n O   |\n/|\  |\n/    |\n    ===',
    7: ' +---+\n O   |\n/|\  |\n/ \  |\n    ==='
}

def getWord(words, minLen, maxLen):
    while True:
        word = words[random.randint(0,25486)]
        word = word.decode('utf-8')
        if len(word) < 3:
            continue
        elif str(word[2]).isupper() == False and maxLen >= len(word) >= minLen:
            return word

def printMan(wordRevealed, missedLetters, deathProgress, hangmen):
    print(hangmen[deathProgress])
    print('Missed letters: ' + missedLetters)
    print('Revealed letters: ' + ' '.join(wordRevealed))
    
while True:
    while True:
        while True:
            try:
                minLen = int(input('Please select a minimum word length. It must be at least 3: ') or '3')
            except ValueError:
                continue
            if minLen >= 3:
                break
        while True:
            try:
                maxLen = int(input('Please select a maximum word length. It must be at least 3: ') or '100')
            except ValueError:
                continue
            if maxLen >= 3:
                break
        if minLen <= maxLen:
            break
    word = getWord(words, minLen, maxLen)
    deathProgress = 1
    wordRevealed = []
    for letter in range(len(word)):
        wordRevealed.append('_')
    missedLetters = ''
    while True:
        printMan(wordRevealed, missedLetters, deathProgress, hangmen)
        while True:
            guessedLetter = input('Guess a letter!\n').lower()
            if guessedLetter in alphabet:
                break
        if guessedLetter in word:
            for letter in range(len(word)):
                if guessedLetter == word[letter]:
                    wordRevealed[letter] = word[letter]
        else:
            missedLetters += (' ' + guessedLetter)
            deathProgress += 1
        if deathProgress == 7:
            print('You have lost!')
            break
        if ''.join(wordRevealed) == word:
            print('You have won!')
            break
    print('The word was: ' + word + '.\n')
