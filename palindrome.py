# def is_palindrome(s):
#     s = s.replace(" ", "")
#     s = s.lower()
#     if s == s[::-1]:
#         return True
#     else:
#         return False
#
#
# is_palindrome("Go hang a salami Im a lasagna hog")
# is_palindrome("Helleh")
# is_palindrome("Hello olleh")

import re


def is_palindrome(s):
    forward = "".join(re.findall(r'[a-z]+', s.lower()))
    backward = forward[::-1]
    print(forward == backward)


is_palindrome("Go hang a salami - I'm a lasagna hog")
is_palindrome("Palap is not ton, sip a lap")
is_palindrome("Hello World")
