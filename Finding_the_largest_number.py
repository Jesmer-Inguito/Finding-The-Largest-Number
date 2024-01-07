# Finding the largest out of the three numbers

#pseudocode

#Ask user to input three different numbers
num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
num_3 = int(input("Enter the third number: "))

#Check if num_1 is the biggest
if num_1 >= num_2 and num_1 >= num_3:
    largest = num_1

#Check if num_2 is the biggest
elif num_2 >= num_1 and num_2 >= num_3:
    largest = num_2

#If neither of the two is the biggest, num_3 is the biggest
else:
    largest = num_3

#Display the biggest number