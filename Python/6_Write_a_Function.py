'''
Task

Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

Input Format
Read the year to test.

Output Format
The function must return a Boolean value (True/False). Output is handled by the provided code stub.
'''


def is_leap(year):
    leap = False

    # Write your logic here
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        leap = True

    else:
        leap = False

    return leap


year = int(input())
print(is_leap(year))
