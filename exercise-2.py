"""
Exercise 2
"""

# PART 1: Gather Information
#
# Gather information about the source of the error and paste your findings here. E.g.:
# - What is the expected vs. the actual output?
# Expected output is False, actual output is False
#                    True                    False

# - What error message (if any) is there?
# There is no error message.

# - What line number is causing the error?
# Line 33: the return statement.

# - What can you deduce about the cause of the error?
# The ifelse case in the for loop both ends with a return and therefore exits the loop after the first iteration.


# PART 2: State Assumptions
#
# State your assumptions here or say them out loud to your partner ...
# Make sure to be SPECIFIC about what each of your assumptions is!

# "Firstly, we loop over the range of numbers within our list_of_nums - 2."
# 
# "Next, we check if the element with index i+1 (the next element) is 1 greater than our
# current element and also if the element with index i+2 (the next, next element) is 2
# greater than our current element.  This would mark our three consecutive numbers as
# indicated by returning True and exiting the loop."
# 
# "If the above case fails, then it loops back to check the next set of three elements in
# the list, is that what happens?... Nope, because we have an else statement that returns
# False, it exits the loop immediately. This is what's causing our bug."
# 
# The easy solution is to remove the else statement entirely.

def contains_3_consecutive(list_of_nums):
    """Return True if the list contains 3 consecutive numbers each increasing by 1."""
    for i in range(len(list_of_nums) - 2):
        if (list_of_nums[i+1] == list_of_nums[i] + 1 and
            list_of_nums[i+2] == list_of_nums[i] + 2):
            return True
        # else:
        #     return False

    return False

if __name__ == '__main__':
    print('### Problem 2 ###')
    answer1 = contains_3_consecutive([1, 2, 4])
    print(answer1) # should print False

    answer2 = contains_3_consecutive([4, 1, 2, 3])
    print(answer2) # should print True