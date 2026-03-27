Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> if __name__ == '__main__':
...     n = int(input())
...     student_marks = {}
...     for _ in range(n):
...         name, *line = input().split()
...         scores = list(map(float, line))
...         student_marks[name] = scores
...     query_name = input()
...     marks = student_marks[query_name]
...     average = sum(marks) / len(marks)
...     
...     # print with 2 decimal places
...     print(f"{average:.2f}")
