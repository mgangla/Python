import random

def get_random_word_from_wordlist():
    wordlist = []
    with open("hangman_wordlist.txt", 'r') as file:
        wordlist = file.read().split('\n')
    word = random.choice(wordlist)
    return word

def get_some_letters(word):
    letters = []
    temp = '_'*len(word)
    for char in list(word):
        if char not in letters:
            letters.append(char)
    character = random.choice(letters)
    for num, char in enumerate(list(word)):
        if char == character:
            templist = list(temp)
            templist[num] = char
            temp = ''.join(templist)
    return temp

def draw_hangman(yourchances):
    if yourchances == 6:
        print("________      ")
        print("|      |      ")
        print("|             ")
        print("|             ")
        print("|             ")
        print("|             ")
    elif yourchances == 5:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|             ")
        print("|             ")
        print("|             ")
    elif yourchances == 4:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /       ")
        print("|             ")
        print("|             ")
    elif yourchances == 3:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|      ")
        print("|             ")
        print("|             ")
    elif yourchances == 2:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\     ")
        print("|             ")
        print("|             ")
    elif yourchances == 1:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\     ")
        print("|     /       ")
        print("|             ")
    elif yourchances == 0:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\     ")
        print("|     / \     ")
        print("|             ")

def start_hangman_game():
    word = get_random_word_from_wordlist()
    temp = get_some_letters(word)
    yourchances = 6
    found = False
    while True:
        if yourchances == 0:
            print(f"You Lost, the word was: {word}")
            break
        print(temp, end='')
        print(f"\t(word has {len(word)} letters)")
        print(f"Chances left: { yourchances}")
        character = input("Enter the letter you think the word may have: ")
        if len(character) > 1 or not character.isalpha():
            print("Please enter a single alphabet only")
            continue
        else:
            for num, char in enumerate(list(word)):
                if char == character:
                    templist = list(temp)
                    templist[num] = char
                    temp = ''.join(templist)
                    found = True
        if found:
            found = False
        else:
            yourchances -= 1
        if '_' not in temp:
            print(f"\nYou Won! The word was: {word}")
            break
        else:
            draw_hangman(yourchances)
        print()

print("===== Welcome to Hangman Game =====")
while True:
    choice = input("Do you want to play hangman? (yes/no): ")
    if 'yes' in choice.lower():
        start_hangman_game()
    elif 'no' in choice.lower():
        print('Exit game...')
        break
    else:
        print("Please enter a valid choice.")
    print("\n")

