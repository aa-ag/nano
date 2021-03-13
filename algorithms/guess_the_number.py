###--- IMPORTS ---###
import random


###--- GLOBAL VARIABLES ---###
total_tries = 7
start_range = 1
end_range = 100


###--- CODE ---###
def guess_the_number(total_tries, start_range, end_range):
    '''
     guess a random number between 1 and 100, 
     you will have 7 tries
    '''

    if start_range > end_range:
        start_range, end_range = end_range, start_range

    random_number = random.randint(start_range, end_range)

    success_message = "Awesome! You guessed correctly"
    failure_message = "Sorry! No more retries left: let's play again."
    miss_message = "Oops! That's incorrect"

    num_tries = 0

    # TODO:
    # - repeated inputs,
    # - negative numbers,
    # - numbers higher than 100,
    # - exit command,
    # - replay commands
    while num_tries < total_tries:
        try:

            attempt = int(input("Guess the number: "))

            if attempt == 'q':
                print("Thanks for playing!")
                return

            # base case/success case
            if attempt == random_number:
                print(success_message)
                return
            print(miss_message)

            if attempt < random_number:
                print("Go higher!")
            else:
                print("Go lower!")
            num_tries += 1

        except:
            print("Don't know how to handle that, "
                  "pls enter a number between 1 and 100")

    print(failure_message)


def run():
    '''
     get user input and control game
    '''

    global total_tries, start_range, end_range

    controls = input('Enter "p" (or any key) to play, and "q" to quit/exit": ')

    while controls != 'q':
        guess_the_number(total_tries, start_range, end_range)

    print("thanks for playing!")


###--- DRIVER CODE ---###
if __name__ == '__main__':
    run()
