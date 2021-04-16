from math import gcd

###############
# Exercise #1 #
###############
def isWordPalindromBoolean(word):
    return word == word[::-1]

def printIsWordPalindrom(word):
    print(f"Yes, the word {word} is palindrom") if word == word[::-1] else print(f"No, the word '{word}' does not match its' reverse '{word[::-1]}'")

word = input("Enter a word: ")

print(isWordPalindromBoolean(word))
printIsWordPalindrom(word)

###############
# Exercise #2 #
###############

def calculateGcd(firstNumber, secondNumber):
    return gcd(firstNumber, secondNumber)

print(calculateGcd(60, 48))