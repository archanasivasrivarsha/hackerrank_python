Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import re
... 
... # Read rows and columns
... rows, cols = map(int, input().split())
... 
... # Read the matrix
... matrix = [input() for _ in range(rows)]
... column_text = ''.join(''.join(col) for col in zip(*matrix))
... 
... # Replace non-alphanumeric sequences between alphanumerics with a space
... decoded = re.sub(r'(?<=\w)([^\w]+)(?=\w)', ' ', column_text)
... 
... print(decoded)
