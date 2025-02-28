#Write a Python program that matches a string that has an 'a' followed by two to three 'b'.

import re

def match_string(text):
    pattern = r'ab{2,3}'
    if re.search(pattern, text):
        return True
    else:
        return False

test_strings = ["a", "ab", "abb", "abbb", "abbbb", "ac", "b", "abc", "aab", "cabbbd"]

for s in test_strings:
    if match_string(s):
        print(f"'{s}' matches the pattern.")
    else:
        print(f"'{s}' does not match the pattern.")

#'a' does not match the pattern.
#'ab' does not match the pattern.
#'abb' matches the pattern.
#'abbb' matches the pattern.
#'abbbb' matches the pattern.
#'ac' does not match the pattern.
#'b' does not match the pattern.
#'abc' does not match the pattern.
#'aab' does not match the pattern.
#'cabbbd' matches the pattern.