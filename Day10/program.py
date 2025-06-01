# Day 10 – Atoi String to Integer Conversion Without Built-in Functions

class Solution:
    def myAtoi(self, s):
        sign = 1
        res = 0
        idx = 0
        n = len(s)

        # Step 1: Skip leading whitespaces
        while idx < n and s[idx] == ' ':
            idx += 1

        # Step 2: Handle optional sign
        if idx < n and (s[idx] == '+' or s[idx] == '-'):
            if s[idx] == '-':
                sign = -1
            idx += 1

        # Step 3: Convert digits
        while idx < n and '0' <= s[idx] <= '9':
            digit = ord(s[idx]) - ord('0')

            # Step 4: Overflow check
            if res > (2**31 - 1) // 10 or (res == (2**31 - 1) // 10 and digit > 7):
                return (2**31 - 1) if sign == 1 else -2**31

            res = res * 10 + digit
            idx += 1

        return sign * res


# 🚀 Example Test Cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.myAtoi("-123"))                  # -123
    print(sol.myAtoi("  -"))                   # 0
    print(sol.myAtoi(" 1231231231311133"))     # 2147483647
    print(sol.myAtoi("-999999999999"))         # -2147483648
    print(sol.myAtoi("  -0012gfg4"))           # -12
    print(sol.myAtoi("words and 987"))         # 0
    print(sol.myAtoi("+42"))                   # 42
    print(sol.myAtoi("   +0 123"))             # 0