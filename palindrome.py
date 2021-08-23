# Is Palindrome
# Write a method is_palindrome(word) that takes in a string word and returns the true if the word is a palindrome, false otherwise. A palindrome is a word that is spelled the same forwards and backwards.

def is_palindrome ():
    word = input("What word would you like to check? ") #asking the user to enter a word to check if it is a palindrome or not
    reverse = word[::-1] #-1 reverses a string
    if(word == reverse):
        print(True)
    else:
        print(False)
    
is_palindrome()