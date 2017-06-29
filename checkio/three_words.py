'''
Mission - Three Words
Let's teach the Robots to distinguish words and numbers.

You are given a string with words and numbers separated by whitespaces 
(one space). The words contains only letters. You should check if the string 
contains three words in succession. For example, the string "start 5 one two 
three 7 end" contains three words in succession.

Input: A string with words.

Output: The answer as a boolean.
'''
def checkio(words):
    word_count = 0
    words = words.split()
    for word in words:
        if word[0] in "0123456789":
            word_count = 0
        else:
            word_count += 1
        if word_count == 3:
            return True
    return False

