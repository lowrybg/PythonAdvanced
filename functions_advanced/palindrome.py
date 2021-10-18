def palindrome(text, index=0, right_index=-1):
    if index == len(text)//2:
        return f'{text} is a palindrome'
    if not text[index] == text[right_index]:
        return f'{text} is not a palindrome'
    return palindrome(text, index + 1, right_index -1)


print(palindrome("abcba", 0))