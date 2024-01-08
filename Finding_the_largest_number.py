# Finding the largest out of the three numbers
import time 
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

#pseudocode

#Ask user to input three different numbers
def solve_problem():
    num_1 = int(input(Fore.MAGENTA + Style.BRIGHT + "Enter the first number: " + Fore.YELLOW + Style.BRIGHT))
    time.sleep(0.5)
    num_2 = int(input(Fore.MAGENTA + Style.BRIGHT + "Enter the second number: " + Fore.YELLOW + Style.BRIGHT))
    time.sleep(0.5)
    num_3 = int(input(Fore.MAGENTA + Style.BRIGHT + "Enter the third number: " + Fore.YELLOW + Style.BRIGHT))

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
    time.sleep(1)
    largest_colored = f"{Fore.GREEN}{Style.BRIGHT}{largest}"
    print(Fore.MAGENTA + Style.BRIGHT + "The largest number is:",largest_colored)

solve_problem()