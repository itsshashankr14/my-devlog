# Sort a given alphanumeric string such that:
#
# Lowercase letters → Uppercase letters → Odd digits →
# Even digits, all sorted within their category.

s = input()
print(''.join(sorted(s,key=lambda c: (c.isdigit(), c.isupper(),c.isdigit() and int(c) % 2 == 0, c))))
