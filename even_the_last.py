'''
Mission - Even the last

You are given an array of integers. 
You should find the sum of the elements with even indexes (0th, 2nd, 4th...) 
then multiply this summed number and the final element of the array together. 
Don't forget that the first element has an index of 0.
For an empty array, the result will always be 0 (zero).
Input: A list of integers.
Output: The number as an integer.

'''
def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """
    x = 0
    sum = 0
    while x < len(array):
        sum += array[x]
        x += 2
    try: 
        return sum * array[-1]
    except IndexError:
        return 0
        
'''
Much better solution from user monkshorin-

def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """
    if len(array) == 0: return 0
    return sum(array[0::2]) * array[-1]   
'''