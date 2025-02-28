#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.

import re

def match_string(text):
    pattern = r'^ab*$'

    if re.match(pattern, text):
        return True
    else:
        return False

test = ["a", "ab", "abb", "ac", "b", "abc", "aab"]

for s in test:
    if match_string(s):
        print(f"'{s}' matches the pattern.")
    else:
        print(f"'{s}' does not match the pattern.")

#'a' matches the pattern.
#'ab' matches the pattern.
#'abb' matches the pattern.
#'ac' does not match the pattern.
#'b' does not match the pattern.
#'abc' does not match the pattern.
#'aab' does not match the pattern.