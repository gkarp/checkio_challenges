'''
Mission - Monkey Typing

The infinite monkey theorem states that a monkey hitting keys at random on a 
typewriter keyboard for an infinite length of time will almost surely type out 
a given text, such as the complete works of John Wallis, or more likely, 
a Dan Brown novel.
Let's suppose our monkeys are typing, typing and typing, and have produced a 
wide variety of short text segments. Let's try to check them for sensible word
inclusions.
You are given some text potentially including sensible words. You should count 
how many words are included in the given text. A word should be whole and may 
be a part of other word. Text letter case does not matter. Words are given in 
lowercase and don't repeat. If a word appears several times in the text, it 
should be counted only once.
For example, text - "How aresjfhdskfhskd you?", words - 
("how", "are", "you", "hello"). The result will be 3.
Input: Two arguments. A text as a string (unicode for py2) and words as a set 
of strings (unicode for py2).
Output: The number of words in the text as an integer.

'''
#Note I improved my solution after seeing Simm0000 's solution
def count_words(text, words):
    word_count = 0
    text = text.lower()
    for word in words:
        if word in text:
            word_count += 1
    return word_count


'''
Much more elegant solution from user Sim00000:
    

def count_words(text, words):
    return sum(w in text.lower() for w in words)
    
Seeing the above solution, I can made my solution a little cleaner with the 
"in" operator.

Old solution:

def count_words(text, words):
    word_count = 0
    text = text.lower()
    for word in words:
        start_index = 0
        end_index = len(word)
        characters_parsed = 0
        while characters_parsed < len(text):
            if word == text[start_index:end_index]:
                word_count += 1
                break
            else:
                start_index += 1
                characters_parsed += 1
                end_index += 1
    return word_count
'''