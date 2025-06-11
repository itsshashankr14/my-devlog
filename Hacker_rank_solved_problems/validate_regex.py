import re

n = int(input().strip())

for _ in range(n):
    pattern = input().strip()
    try:
        re.compile(pattern)
        print("True")
    except re.error:
        print("False")
