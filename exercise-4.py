"""
Exercise 4
"""

# PART 1: Gather Information
#
# NOTE: Not sure if this is part of the exercise, but I'm including it anyway.  
#  File "exercise-4.py", line 22
#    if high == None:
# IndentationError: unindent does not match any outer indentation level
# 
# Problem solved by aligning docstring on line 21 with the rest of the code.
# 
# 
# Stack Trace:
# Traceback (most recent call last):
#   File "exercise-4.py", line 45, in <module>
#     answer = binary_search([1, 2, 4, 5, 7], 7)
#   File "exercise-4.py", line 41, in binary_search
#     return binary_search(arr, element, mid, high)
#   File "exercise-4.py", line 41, in binary_search
#     return binary_search(arr, element, mid, high)
#   File "exercise-4.py", line 41, in binary_search
#     return binary_search(arr, element, mid, high)
#   [Previous line repeated 995 more times]
#   File "exercise-4.py", line 26, in binary_search
#     if high == None:
# RecursionError: maximum recursion depth exceeded in comparison
# 
# According to the stack trace, we see line 41 which is a recurrsion function call being called
# 1000 times resulting in a RecursionError which means there is a problem with never reaching our base case.
# If we can fix our base case situation, then we can fix our bug.

# PART 2: State Assumptions
#
# "The first thing we encounter in our function is to set high to the last index of our array...
# Yes, high is set to 4."
# 
# "We then set a variable called mid to be the middle index of our array... our mid variable is
# set to 2."
# 
# "We then check to see if the element at index mid (2) is the element we are searching for...
# this is false. So we determine if our element at mid index is greater than or not greater than
# our element we are searching for.  We then recursively call the binary_search function with the
# mid index replacing our low or our high index (in this example our low index is replaced)... This
# happens correctly."
# 
# "We then loop again with a shorter array, we can take a peak at our middle index after every loop
# with a print function... we can see that every loop after the first one generates a mid index of 3
# which isn't the element we're searching for (we want index 4) and the function is never changing
# its mid point after that.  Therefore the bug must be occuring on line 61 where the mid point is being
# assigned during every recursive loop."
# 
# "We can assess than when we got to our third loop onward, the high variable was 4 and our low variable was 3,
# therefore our mid point was (4+3) // 2 which equalled 3.  Our mid variable was 3 which resulted in no
# change to any of our other variables and we were stuck in an infinite loop.  The fix to this must be
# to floor and ceiling our mid variable accordingly if our binary search takes us up the array or down the array."
# 
# "I added an extra bool input varaible to toggle between flooring or ceiling our mid index.  I also
# imported the math library to include math.ceil in line 72."

import math
def binary_search(arr, element, low=0, high=None, higher=False):
    """Returns the index of the given element within the array by performing a binary search."""
    if high == None:
        high = len(arr) - 1

    if high < low:
        return -1

    if higher == True:
        mid = math.ceil((high + low) / 2.0)
    else:
        mid = (high + low) // 2

    if arr[mid] == element: 
        return mid

    elif arr[mid] > element:
        return binary_search(arr, element, low, mid, False)

    else:
        return binary_search(arr, element, mid, high, True)


if __name__ == '__main__':
    answer = binary_search([1, 2, 4, 5, 7], 7)
    print(answer)