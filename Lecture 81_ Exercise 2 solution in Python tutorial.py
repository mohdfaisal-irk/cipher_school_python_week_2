# Exersice

# def is_palindrom(word):
#     reversed_word = word[::-1]
#     if word == reversed_word:
#         return True
#     else:
#         return False
#

# def is_palindrom(word):
# reversed_word = word[::-1]
# if word == reversed_word:
# return True
# return False

def is_palindrom(word):
    return word == word[::-1]


print(is_palindrom("nan"))
