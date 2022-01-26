"""
Exercise 3
"""

# PART 1: Gather Information
# 
# Stack Trace:
# Traceback (most recent call last):
#   File "exercise-3.py", line 34, in <module>
#     answer = insertion_sort([5, 2, 3, 1, 6])
#   File "exercise-3.py", line 26, in insertion_sort
#     while key < arr[j] : 
# IndexError: list index out of range
# 
# According to the stack trace, there is an IndexError on line 26. That must mean that the variable 
# j is outside of the bounds of the list. That means we need to find out why j has a value that's
# greater than or equal to the length of the list.


# PART 2: State Assumptions
# 
# "Firstly, we loop over each number in the arr inputed starting with the second element.
# We'll place a print statement for i underneath to check... We see that the value of i goes
# through the numbers 1, 2 and 3 meaning that the third loop is where we encounter our error.  What
# makes our 3rd loop different than our first two loops?"
# 
# "To take a look at what might be happening during the loops, we can place a print statement
# for the arr at the end of the for loop to see what the arr looks like after each insertion sort step...
# In this we see our problem visually.  The arr after the 1st loop looks like [6, 5, 3, 1, 2] when it
# should look like [2, 5, 3, 1, 6].  This means that the function is comparing and replacing the 
# first and last element of the array."
# 
# "The reason this might occur is because the function is 
# comparing index 0 (the first element) with index -1 (the last element).  In fact on line 45, we can
# follow the while loop key < arr[j] and we see that the loop comparisons don't stop until the loop
# finds an element with less value than the variable key."
# 
# "We can fix this by placing a stop in our while loop so that we don't let our function compare
# negative indices.  We add to the while loop 'and j >= 0'.  After running, the output is [1, 2, 3, 5, 6]
# which is what we've come to expect if the function is working."

def insertion_sort(arr):
    """Performs an Insertion Sort on the array arr."""
    for i in range(1, len(arr)):
        key = arr[i] 

        j = i-1
        while key < arr[j] and j >= 0: 
            arr[j+1] = arr[j] 
            j -= 1
        arr[j+1] = key
    return arr

if __name__ == '__main__':
    print('### Problem 3 ###')
    answer = insertion_sort([5, 2, 3, 1, 6])
    print(answer)

