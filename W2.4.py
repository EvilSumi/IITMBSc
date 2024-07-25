'''You are tasked with creating a multi-purpose application that performs various operations based on user input. The application should take the operation name from the input and execute the corresponding task.

The operations your application should support are as follows:

Odd number checker: Check whether the input number is odd.
Name: odd_num_check
Inputs: number:int
Output: "yes" if the number is odd, "no" otherwise.
Perfect square checker: Check whether the input number is a perfect square.
Name: perfect_square_check
Inputs: number:int
Output: "yes" if the number is a perfect square, "no" otherwise.
Vowel checker: Check if a string has a vowel in it.
Name: vowel_check
Inputs: text:str
Output: "yes" if the string contains a vowel, "no" otherwise.
Divisibility checker: Check if a number is divisible by 2 or 3.
Name: divisibility_check
Inputs: number:int
Output: "divisible by 2" if the number is divisible by 2, "divisible by 3" if divisible by 3, "divisible by 2 and 3" if divisible by both, "not divisible by 2 and 3" otherwise.
Palindrominator: Takes a string and joins it with the same string reversed. Eg. "cal" -> "calac".
Name: palindrominator
Inputs: text:str
Output: string representing the input string joined with its reverse(the last characte should not be repeated twice)
Simple interest calculator with inputs with a higher interest rate if long term.
Name: simple_interest
Inputs: principal_amount:int, n_years:int (number of years)
Output: Simple interest with a 5% interest rate if less than 10 years, else 8%. Round the result to integer using round function.
If the operation name is not any of the above print "Invalid Operation".'''

import math
import sys

def odd_num_check(number):
    return "yes" if number % 2 != 0 else "no"

def perfect_square_check(number):
    sqrt_number = int(math.sqrt(number))
    return "yes" if sqrt_number * sqrt_number == number else "no"

def vowel_check(text):
    vowels = set("aeiouAEIOU")
    return "yes" if any(char in vowels for char in text) else "no"

def divisibility_check(number):
    divisible_by_2 = number % 2 == 0
    divisible_by_3 = number % 3 == 0
    if divisible_by_2 and divisible_by_3:
        return "divisible by 2 and 3"
    elif divisible_by_2:
        return "divisible by 2"
    elif divisible_by_3:
        return "divisible by 3"
    else:
        return "not divisible by 2 and 3"

def palindrominator(text):
    return text + text[::-1][1:]

def simple_interest(principal_amount, n_years):
    rate = 0.05 if n_years < 10 else 0.08
    interest = principal_amount * rate * n_years
    return round(interest)

def main():
    input_lines = sys.stdin.read().strip().split('\n')
    operation = input_lines[0]
    
    if operation == "odd_num_check":
        number = int(input_lines[1])
        print(odd_num_check(number))
    
    elif operation == "perfect_square_check":
        number = int(input_lines[1])
        print(perfect_square_check(number))
    
    elif operation == "vowel_check":
        text = input_lines[1]
        print(vowel_check(text))
    
    elif operation == "divisibility_check":
        number = int(input_lines[1])
        print(divisibility_check(number))
    
    elif operation == "palindrominator":
        text = input_lines[1]
        print(palindrominator(text))
    
    elif operation == "simple_interest":
        principal_amount = int(input_lines[1])
        n_years = int(input_lines[2])
        print(simple_interest(principal_amount, n_years))
    
    else:
        print("Invalid Operation")

if __name__ == "__main__":
    main()
