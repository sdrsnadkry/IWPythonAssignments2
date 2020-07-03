def is_palindrome(word):
    rev = word[::-1]
    if word == rev:
        return True
    else:
        return False


word = input("Enter a word: ")
print(is_palindrome(word))