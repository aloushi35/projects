# Fakhreddine, Ali


#Problem 1

def Factorial(n):
    if n == 0:
        return 1
    return n * Factorial(n-1)


#Problem 2

def Palindrome(word):
    if (word == word[::-1]):
        print("True")
    else:
        print("False")


#Problem 3

def ListMult(lst):
    res = [(max(lst) * (i / min(lst))) for i in lst]
    return res


#Problem 4

from collections import namedtuple
Employee = namedtuple("Employee","name position salary full_time ")
def EmployeeManager(p1):
    print("Name:",p1.name)
    print("Position:",p1.position)
    if p1.full_time == True:
        print("Full Time: Yes")
        print("Paycheck:",int(p1.salary/12))
    else:
        print("Full Time: No")
        print("Paycheck:",int(p1.salary/24))



#Problem 5

def IsSublist(lst1,lst2):
    if lst1 == []:
        result = True
    if (all(x in lst2 for x in lst1)):
        result = True
    else:
        result = False
    return result
                
          
#Problem 6

def translator(s):
    sentence = str(s).split()
    newsentence = str()
    for words in sentence:
        newsentence += words[1:] + words[0] + 'ay' + " "
    return newsentence

#Problem 7

def hangman(word):
    print('Welcome to Hangman!')
    guesses = ' '
    turns = 8
    while turns > 0:
        failed = 8
        for char in word:
            if char in guesses:
                char
            else:
                "_"
                failed -= 1
        if failed == 8:
            print("Congratulations, you have won the game! The word is", word)
            break
        guess = input('Guess a character:')
        guesses += guess
        if guess in word:
            print(guess, "is in the word")
            print("Strike Count =", +turns)
        if guess not in word:
            turns -= 1
            print(guess, "not in the word")
            print("Strike Count =", +turns)

        if turns == 0:
            print("I'm sorry, you lost. The word was", word)
