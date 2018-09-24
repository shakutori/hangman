# http://tinyurl.com/h9q2cpc

import random
def hangman(word):
    wrong = 0
    stages = ["",
              "             ",
              "_______      ",
              "|             ",
              "|      |      ",
              "|      O      ",
              "|     /||     ",
              "|     /|      ",
              "|             ",
              ]
    rletters = list(word)
    board = ["__"] *len(word)
    win = False
    print("Welcome to Hangman")

    while wrong < len (stages) - 1:
        
        print("\n")
        msg = "Guess a letter: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
            
        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong]))
        print("You lose! It was {}.".format(word))
                        
word_lst = [ "apple", "dog", "cat", "phone", "tree",
             "car", "face", "hand", "eye", "egg" ]
word_num = len(word_lst)
rand_num = random.randrange(0,word_num)
rand_word = word_lst[rand_num]
hangman(rand_word)
