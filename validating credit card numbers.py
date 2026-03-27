Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import re
... 
... def validate_credit_card(card):
...     # Check format (digits only or groups of 4 separated by '-')
...     pattern = re.compile(r'^[456]\d{3}(-?\d{4}){3}$')
...     if not pattern.match(card):
...         return "Invalid"
...     
...     # Remove hyphens to check consecutive digits
...     card_digits = card.replace('-', '')
...     
...     # Check for 4 or more consecutive repeated digits
...     if re.search(r'(\d)\1{3,}', card_digits):
...         return "Invalid"
...     
...     return "Valid"
... 
if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        card = input().strip()
        print(validate_credit_card(card))
