Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
def validate_uid(uid):
    if len(uid) != 10:
        return "Invalid"
...     if not uid.isalnum():
...         return "Invalid"
...     if len(set(uid)) != 10:  # check for repeats
...         return "Invalid"
...     
...     upper_count = sum(1 for c in uid if c.isupper())
...     digit_count = sum(1 for c in uid if c.isdigit())
...     
...     if upper_count < 2 or digit_count < 3:
...         return "Invalid"
...     
...     return "Valid"
... 
... if __name__ == '__main__':
...     n = int(input())
...     for _ in range(n):
...         uid = input().strip()
...         print(validate_uid(uid))
