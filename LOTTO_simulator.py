import random

"""
Lottery Number Guessing Program

This program allows the user to input six unique numbers between 1 and 49. 
It then generates six random lottery numbers and compares the user's input 
with the drawn numbers to see how many they guessed correctly. 
"""


def get_unique_numbers():
    """
       Prompts the user to enter six unique numbers between 1 and 49.
       Checks that each number:
         - Is a valid integer
         - Is within the range 1-49
         - Has not been entered previously

       Returns:
           list: Sorted list of six unique numbers entered by the user.
       """
   numbers = set()
   while len(numbers) < 6:
       try:
           num = int(input("Enter a number between 1 and 49: "))
           if num < 1 or num > 49:
               print("Please enter a number between 1 and 49")
               continue
           elif num in numbers:
               print("You have already entered this number. Choose a different number.")
               continue
           numbers.add(num)
       except ValueError:
           print("Please enter a valid integer")
   return sorted(numbers)


def generate_random_numbers():
    """
        Generates six random, unique numbers between 1 and 49.

        Returns:
            list: Sorted list of six random numbers representing the lottery draw.
    """
    return sorted(random.sample(range(1,50),6))


def check(user_numbers, drawn_numbers):
    """
        Compares user-selected numbers to drawn lottery numbers to find matches.

        Returns:
            tuple: Consisting of:
                - int: Count of matching numbers.
                - set: Set of the matching numbers.
    """
    hits = set(user_numbers) & set(drawn_numbers)
    return len(hits), hits


if __name__ == '__main__':
   user_numbers = get_unique_numbers()
   print(f"Your numbers are {user_numbers}")

   drawn_numbers = generate_random_numbers()
   print(f"Lottery numbers are {drawn_numbers}")

   hit_count, hits = check(user_numbers,drawn_numbers)
   print(f"You hited {hit_count} numbers:",sorted(hits))











