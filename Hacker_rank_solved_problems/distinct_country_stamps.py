# Task: Count the total number of distinct country stamps collected by Rupal.
# Approach: Use a set to automatically handle uniqueness.
# Input: First line is an integer n (number of stamps). Next n lines are country names.
# Output: Single integer - count of unique country names.

n = int(input())
country_stamps = set()

for _ in range(n):
    country =input()
    country_stamps.add(country)

print(len(country_stamps))