Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> n = int(input())
... scores = list(map(int, input().split()))
... 
... max_score = max(scores)
... scores = [score for score in scores if score != max_score]
... runner_up = max(scores)
... 
... print(runner_up)
