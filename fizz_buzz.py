# Fizz Buzz
# Write a method fizz_buzz(max) that takes in a number max and returns an array containing all numbers greater than 0 and less than max that are divisible by either 4 or 6, but not both.

def fizz_buzz(max):
    for val in range(1, max+1):
        if(val % 4 == 0 or val % 6 == 0) and not (val % 4 == 0 and val % 6 == 0):
            print(val) 
 


fizz_buzz(37)