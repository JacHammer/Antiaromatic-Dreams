# Minci
# time elapsed: 37 min
# submitted 2 times


class Solution:
    def calculate(self, s: str) -> int:

        # re-organize spaces
        s = s.replace(' ', '')
        for op in "+-*/":
            s = s.replace(op, str(' ' + op + ' '))

        # separate the list by space
        s = s.split(' ')

        # convert string to int
        for i in range(len(s)):
            if s[i].isnumeric():
                s[i] = int(s[i])

        # compute high order operators
        while "*" in s or "/" in s:
            for i in range(len(s)):
                if s[i] == "*" or s[i] == '/':
                    if s[i] == "*":
                        # a = a*b in ['a', '*', 'b']
                        s[i - 1] *= s[i + 1]
                        # remove last two elements
                        s.pop(i)
                        s.pop(i)
                        break
                    elif s[i] == "/":
                        s[i - 1] //= s[i + 1]
                        s.pop(i)
                        s.pop(i)
                        break

        # compute low order operators
        while "+" in s or "-" in s:
            for i in range(len(s)):
                if s[i] == "+" or s[i] == '-':
                    if s[i] == "+":
                        s[i - 1] += s[i + 1]
                        s.pop(i)
                        s.pop(i)
                        break
                    elif s[i] == "-":
                        s[i - 1] -= s[i + 1]
                        s.pop(i)
                        s.pop(i )
                        break

        # print(s)
        return s[0]


sol = Solution()
sol.calculate("3+5/2")