from typing import List

def read_integers() -> List[int]:
    user_input = input() # getting input from user 
    strings = user_input.split(',') # spliting the each line with comma
    list_int = []
    for i in strings:
        list_int.append(int(i))
    return (list_int)
# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
