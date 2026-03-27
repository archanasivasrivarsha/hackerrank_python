Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> # Read input
... x = int(input())
... y = int(input())
... z = int(input())
... n = int(input())
... 
... # Generate the list using list comprehension
... coordinates = [[i, j, k] 
...                for i in range(x+1) 
...                for j in range(y+1) 
...                for k in range(z+1) 
...                if i + j + k != n]
... 
... # Print the result
... print(coordinates)
