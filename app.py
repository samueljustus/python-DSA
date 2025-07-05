import random

# print(help(random))q

# lowest_num = 1
# highest_num = 20
# answer = random.randint(lowest_num, highest_num)
# guesses = 0
# is_running = True


# print("PYTHON NUMBER GUESSING GAME")

# print("-------------------------")

# print(
#     f"Welcome to the guessing game pick a number between {lowest_num} and {highest_num}")


# while is_running:

#     guess = input("Enter your guess: ")

#     if guess.isdigit():

#         guess = int(guess)
#         guesses += 1
#         if guess < lowest_num or guess > highest_num:
#             print(
#                 f"Please enter a number between {lowest_num} and {highest_num}")
#         elif guess < answer:
#             print("Too low, try again")
#         elif guess > answer:
#             print("Too high, try again")
#         else:
#             print(
#                 f"Congratulations! You guessed the number {answer} in {guesses} guesses!")
#             is_running = False
#             ("This code would never run because at this point we have already broken pout of the loop ")
#     else:
#         print("Please Enter a valid guess")


# print("Break out")


def addition(*args):
    total = 0
    for arg in args:
       total += arg
    return total
    

total = addition(1, 2, 3, 4, 6, 8, 9, 3)
print(f"The total is {total}")

