"""
Exercise 1
"""

# PART 1: Gather Information
#
# ----------------- STACK TRACE -------------------
# Traceback (most recent call last):
#   File "/Users/Temp/dev/courses/spd2.3/SPD-2.3-Debugging-Steps-Lab/exercise-1.py", line 31, in <module>
#     answer = find_largest_diff([5, 3, 1, 2, 6, 4])
#   File "/Users/Temp/dev/courses/spd2.3/SPD-2.3-Debugging-Steps-Lab/exercise-1.py", line 23, in find_largest_diff
#     diff = abs(list_of_nums[i] - list_of_nums[i+1])
# IndexError: list index out of range

# Gather information about the source of the error and paste your findings here. E.g.:
# - What is the expected vs. the actual output?
# The expected output is 4, as the largest diff between consecutive numbers is between 2 and 6,
# the actual output is an IndexError.

# - What error message (if any) is there?
# There is an IndexError on line 23.

# - What line number is causing the error?
# Line 23 is causing the error

# - What can you deduce about the cause of the error?
# The cause of the error is because the varriable i is greater than or equal to the length of the list.

# PART 2: State Assumptions
#
# State your assumptions here or say them out loud to your partner ...
# Make sure to be SPECIFIC about what each of your assumptions is!

# "The first thing that occurs in the function is to set largest_diff to 0.""
# 
# "Next, we loop over the length of list_of_nums and set its index to the variable i.
# We can print out the variable i at the start of the loop to see if this is true... which it is."
# 
# "Then we calculate the difference between the current and next element of the list.
# Does each element with index i have an element with index i+1?... Nope, when i is
# equal to 5 (the last element of the list) it tries to get element i+1 which is outside
# of our list.  That is what's causing the bug."
# 
# "The way to fix this is to simply decrease our range in our for loop with a -1 as seen on line 50."

def find_largest_diff(list_of_nums):
    """Find the largest difference between *consecutive* numbers in a list."""
    largest_diff = 0
    # for i in range(len(list_of_nums)):     original ver
    for i in range(len(list_of_nums) - 1): # fixed ver
        diff = abs(list_of_nums[i] - list_of_nums[i+1])
        if diff > largest_diff:
            largest_diff = diff

    return largest_diff

if __name__ == '__main__':
    print('### Problem 1 ###')
    answer = find_largest_diff([5, 3, 1, 2, 6, 4])

    # This should print 4, as the largest diff between consecutive numbers is between 2 and 6
    print(answer)