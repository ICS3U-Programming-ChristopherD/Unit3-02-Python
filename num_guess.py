#!/usr/bin/env python3

# Created By: Chris Di Bert
# Date: Oct. 5, 2022
# This program checks if the user guessed a number correctly


# Imports the secret number
import constants


def main():
    print("Try and guess my secret number. \n")
    print("It is within the range of 0-9")

    # Stores the user's guess
    user_guess = float(input("Enter your guess: "))

    # If the user guessed correctly
    if user_guess == constants.NUMBER:
        print("Correct!")

    # If the user guessed incorrectly
    else:
        print("Incorrect.")


if __name__ == "__main__":
    main()
