'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21

'''
def reverse(x: int) -> int:
    # Define the range for 32-bit signed integers
    INT_MIN, INT_MAX = -2**31, 2**31 - 1

    # Get the sign of the integer
    sign = -1 if x < 0 else 1

    # Reverse the digits of the absolute value
    reversed_num = int(str(abs(x))[::-1]) * sign

    # Check if the reversed number is within the range
    if reversed_num < INT_MIN or reversed_num > INT_MAX:
        return 0

    return reversed_num