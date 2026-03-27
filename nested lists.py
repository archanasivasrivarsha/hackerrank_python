Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> n = int(input())
... students = []
... 
... for _ in range(n):
...     name = input()
...     grade = float(input())
...     students.append([name, grade])
... 
... grades = sorted({grade for name, grade in students})
... second_lowest = grades[1]
... 
... names_with_second_lowest = [name for name, grade in students if grade == second_lowest]
... names_with_second_lowest.sort()
... 
... for name in names_with_second_lowest:
...     print(name)
