# Finding the largest out of the three numbers
import time 
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

#pseudocode

#Open the program
def main():
    state = "on"

    while True:
        print(Fore.CYAN + Style.BRIGHT + f"The current state is {state}")
        time.sleep(0.5)
        print(Fore.BLACK + Style.BRIGHT + "Enter 'off' to turn it off, 'solve' to solve a problem, or 'exit to quit:")
        user_input = input(Fore.CYAN + Style.BRIGHT + "> " + Fore.YELLOW + Style.BRIGHT)

        if user_input == "off":
            state = "off"
        elif user_input == "solve":
            solve_problem() #Call to solve the problem
        elif user_input == "exit":
            print(Fore.CYAN + Style.BRIGHT + "Exiting the program.")
            break
        else:
            print(Fore.CYAN + Style.BRIGHT + "Invalid input. Please enter 'off', 'solve', or 'exit'.")

#Ask user to state the problem
def solve_problem():
    print(Fore.GREEN + Style.BRIGHT + "C4 is now online.")
    time.sleep(0.5)
    user_input = input(Fore.MAGENTA + Style.BRIGHT + "Please state your problem: " + Fore.YELLOW + Style.BRIGHT)
    
    # Check if the user wants to find the largest number
    if user_input.strip() == "Find the largest number":
         input_number()
    
    else:
        print(Fore.CYAN + Style.BRIGHT + "Problem-solving capabilties limited to finding the largest number at the moment")

def input_number():
    num_1 = int(input(Fore.MAGENTA + Style.BRIGHT + "Enter the first number: " + Fore.YELLOW + Style.BRIGHT))
    time.sleep(0.5)
    num_2 = int(input(Fore.MAGENTA + Style.BRIGHT + "Enter the second number: " + Fore.YELLOW + Style.BRIGHT))
    time.sleep(0.5)
    num_3 = int(input(Fore.MAGENTA + Style.BRIGHT + "Enter the third number: " + Fore.YELLOW + Style.BRIGHT))
        
    #Check is num_1 is the biggest
    if num_1 >= num_2 and num_1 >= num_3:
            largest = num_1
        
    #Check if num_2 is the biggest
    elif num_2 >= num_1 and num_2 >= num_3:
        largest = num_2

    #If neither of the two is the biggest, num_3 is the biggest=
    else:
        largest = num_3

    time.sleep(1)
    largest_colored = f"{Fore.GREEN}{Style.BRIGHT}{largest}"
    print(Fore.GREEN + Style.BRIGHT + "The largest number is",largest_colored)

    time.sleep(0.5)
    another_problem = input(Fore.MAGENTA + Style.BRIGHT + "Do you want to solve another problem? (yes/no): " + Fore.YELLOW + Style.BRIGHT)
    if another_problem.lower() == "yes":
        time.sleep(0.5)
        input_number()

    else: 
        time.sleep(0.5)
        print(Fore.CYAN + Style.BRIGHT + "Returning to Main Menu.")
        time.sleep(1)

main()