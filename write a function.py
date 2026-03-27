Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> def is_leap(year):
...     leap = False
...     
...     if year % 4 == 0:
...         if year % 100 == 0:
...             if year % 400 == 0:
...                 leap = True
...             else:
...                 leap = False
...         else:
...             leap = True
...     else:
...         leap = False
...         
...     return leap
