Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> n = int(input().strip())
... 
... if n % 2 == 1:
...     print("Weird")
... else:
...     if 2 <= n <= 5:
...         print("Not Weird")
...     elif 6 <= n <= 20:
...         print("Weird")
...     else:
...         print("Not Weird")
