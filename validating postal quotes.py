Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> regex_integer_in_range = r"^[1-9][0-9]{5}$"
... regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"
... 
... import re
... P = input()
... 
... print (bool(re.match(regex_integer_in_range, P)) 
