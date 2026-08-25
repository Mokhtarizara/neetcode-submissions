from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    count = {}
    # key = char 
    # value = count of each char

    # the word each letter cheack on by one
    for char in word: 
        if char in count: #check if i have in jar 
    # already have jar , yes add 1 coin        
            count[char] += 1
        else:
    # if no, new letter add new jar and add coin 
            count[char] = 1 
    return count # return the result 

# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
