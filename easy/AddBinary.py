class Solution:
    def addBinary(self, a: str, b: str) -> str:
        dummy = ''
        carry = 0
        a = list(a)
        b = list(b)
        while a or b or carry:
            if a:
                print(a[-1])
                carry += int(a[-1])
                a.pop()
            if b:
                carry += int(b[-1])
                b.pop()
            dummy += str(carry % 2)
            carry //= 2
        return dummy[::-1]


sol = Solution()
a = '1010'
b = '1011'
print(sol.addBinary(a, b))
