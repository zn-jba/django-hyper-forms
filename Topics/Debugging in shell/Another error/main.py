def add_underscores(word: str) -> str:
    return f"_{'_'.join([letter for letter in word])}_"

user_input = input()
print(add_underscores(user_input))
