def remove_fourth_character(word: str) -> str:
    before_four = word[:3]
    after_four = word[4:]
    new_string = before_four + after_four
    return new_string

# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
