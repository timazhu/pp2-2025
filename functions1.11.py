#Write a Python function that checks whether a word or phrase is palindrome or not. Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam

def palindrome(s):
    s = ''.join([c for c in s if c.isalnum()]).lower()
    reversed_s = ""
    for i in range(len(s)-1, -1, -1):
        reversed_s += s[i]
    return s == reversed_s

print(palindrome("madam")) #True
print(palindrome("Patrick")) #False
