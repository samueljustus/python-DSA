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

import time

# def addition(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total


# total = addition(1, 2, 3, 4, 6, 8, 9, 3)
# print(f"The total is {total}")


# person = [num + 2 for num in range(1, 21)]

# print(person)

# for num in range(1, 21):
#     if num % 2 == 0:
#         print(f"{num} is even")
#     else:
#         print(f"{num} is odd")


# function that displays balance

def display_balance(balance):
    print(f"Your balance is ${balance:.2f}")


def make_deposit():
    amount = float(input("How much do you want to deposit: "))

    if amount < 0:
        print("please deposit a valid amount")
        return 0

    else:
        print(f"You have deposited ${amount:.2f}")
        return amount


def withdrawal(balance):
    amount = float(input("How much do you want to withdraw: "))

    if amount > balance:
        print("Insufficient funds")
        return 0

    elif amount < 0:
        print("Please enter a valid amount to withdraw")
        return 0

    else:
        print(f"You have withdrawn ${amount:.2f}")
        return amount


def main():

    balance = 0
    is_running = True

    while is_running:
        print('Banking Program')
        print('1. Balance')
        print('2. Deposit')
        print('3. Withdrawal')
        print('4. Exit')
        choice = input('Choose an option(1 - 4): ')
        print('')

        if choice == '1':
            display_balance(balance)
        elif choice == '2':
            balance += make_deposit()

        elif choice == '3':
            balance = balance - withdrawal(balance)

        elif choice == '4':
            print('Exiting program...')
            time.sleep(1)
            is_running = False

        else:
            print('please pick a valid option')

    print('Thank you for banking with us')


stock_prices = [298, 305, 320, 301, 292, 320, 315, 330, 340, 350]

#on what day was price 301

# for day in (len(stock_prices)):
#     if stock_prices[day] == 301:
#         print (day)

#         Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,

# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

expenses = [2200, 2350, 2600, 2130, 2190]

# =======================2============================


# total = 0

# for expense in range(len(expenses) - 2):
#    total = total + expenses[expense]
# print(total)

# big O is O(n)
# ===============================3========================


print(2000 in expenses)


# ============================4============================


# expenses.append(1980)

# big O is O(1)




# ============================5============================



expenses[3] -= 200

print(expenses)


