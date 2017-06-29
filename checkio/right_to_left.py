'''
Mission: Right to Left
One of robots is charged with a simple task: to join a sequence of strings in 
one sentence to produce instructions on how to get around the ship. 
But this robot is left-hander and has a tendency to joke around and confuse its
right handed friends.

You are given a sequence of strings. You should join these strings into chunk 
of text where the initial strings are separated by commas. As a joke on the 
right handed robots, you should replace all cases of the words "right" with the
word "left", even if it's a part of another word. All strings are given in 
lowercase.

Input: A sequence of strings as a tuple of strings (unicode).

Output: The text as a string.
'''
def left_join(text):
    new_text = ",".join(text)
    new_text = new_text.replace("right", "left")
    return new_text