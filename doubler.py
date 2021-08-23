# Doubler
# Write a method doubler(numbers) that takes an array of numbers and returns a new array where every element of the original array is multiplied by 2.

def doubler():
    numbers = [8, 12, 14, 20, 26, 29]
    print ("The original array is:" + str(numbers))
    new_array = []
    for val in numbers:
        new_array.append(val + val)
    print("The new array is: " + str(new_array))
    
doubler()