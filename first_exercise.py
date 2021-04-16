###############
# Exercise #1 #
###############

def fibonacci(currentInteger):
    if currentInteger <= 1:
        return currentInteger
    else:
        return(fibonacci(currentInteger - 1) + fibonacci(currentInteger - 2))

# Main Function
def fibonacciMain():
    count = int(input("Enter number: "))

    if count <= 0:
        print("Please enter a positive int")
    else:
        for index in range(count):
            print(fibonacci(index))

# Call Main Function
fibonacciMain()

###############
# Exercise #2 #
###############
            
def isWordPalindrom(word):
    return word == word[::-1]

word = input("Enter a word: ")
print(isWordPalindrom(word))

###############
# Exercise #3 #
###############

def countUppers(word):
    return sum(map(str.isupper, word))
            
def countVowels(word):
    return sum(1 if c.lower() in 'aeiou' else 0 for c in word)

word = input("Enter a word: ")

print(countUppers(word))
print(countVowels(word))