# Write a method average_of_three(num1, num2, num3) that returns the average of three numbers

def average_of_three():
    num1=int(input("Enter a value for num1:"))
    num2=int(input("Enter a value for num2:"))
    num3=int(input("Enter a value for num3:"))
    average = (num1 + num2 + num3)/3
    print("The average of the three numbers you chose =", average)
    
average_of_three() 
