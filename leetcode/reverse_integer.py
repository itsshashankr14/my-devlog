class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x_abs = abs(x)
        reversed_num = int(str(x_abs)[::-1]) * sign

        # Check 32-bit signed integer bounds
        if -2**31 <= reversed_num <= 2**31 - 1:
            return reversed_num
        else:
            return 0
# class Solution:
#     def reverse(self, x: int) -> int:
#         INT_MIN, INT_MAX = -2**31, 2**31 - 1
#         res = 0
#         sign = -1 if x < 0 else 1
#         x = abs(x)
#
#         while x != 0:
#             digit = x % 10
#             x //= 10
#
#             # Check for overflow before multiplying/reserving
#             if res > (INT_MAX - digit) // 10:
#                 return 0  # overflow
#             res = res * 10 + digit
#
#         return sign * res
# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.reverse(123))     # Output: 321
    print(sol.reverse(-123))    # Output: -321
    print(sol.reverse(120))     # Output: 21
    print(sol.reverse(0))       # Output: 0