import random

def main():
    list_of_words = ["permission", "systematic", "overcharge", "reputation", "acceptance"]
    random_index = random.randint(0, len(list_of_words) - 1)
    random_word = list_of_words[random_index]
    turns = len(random_word) + 5
    correct_chars = []

    print()
    for i in range(len(random_word)):
        correct_chars.append('_')

    while turns > 0:
        if correct_chars == list(random_word):
            for i in correct_chars:
                print(i, end = ' ')
            print()
            break

        for i in correct_chars:
            print(i, end = ' ')

        print(f'\n\nTurns left: {turns}')
        guess = input("\nEnter a character or word: ")

        for i in guess:
            if i in correct_chars:
                continue
            elif i in random_word:
                for j in range(len(random_word)):
                    if i == random_word[j]:
                        correct_chars.pop(j)
                        correct_chars.insert(j, i)
            else:
                turns -= 1

    if "_" in correct_chars:
        print()
        print(f"You lose! The correct word is: {random_word}")
    elif "_" not in correct_chars:
        print()
        print("You win!")

main()

