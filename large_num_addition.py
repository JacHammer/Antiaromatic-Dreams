# large int addition
def adds(a, b):
    if len(a) < len(b):
        a, b = b, a
    carry = 0
    num = ''
    for i in range(len(b) - 1, -1, -1):
        remainder = int(a[i + (len(a) - len(b))]) + int(b[i]) + carry
        if remainder >= 10:
            remainder %= 10
            carry = 1
            num += str(remainder)
        else:
            carry = 0
            num += str(remainder)
    print(num)
    if len(a) == len(b) and carry == 1:
        num += '1'

    elif len(a) > len(b) and carry == 1:
        trunct_len = len(a) - len(b)
        trunct = a[0:trunct_len]
        temp_num = ''
        carry_a = 1
        for i in range(len(trunct) - 1, -1, -1):
            print(i)
            n = int(trunct[i]) + 1
            if n >= 10:
                n %= 10
                carry_a = 1
                temp_num += str(n)
            else:
                carry_a = 0
                temp_num += str(n)
        if carry_a == 1:
            temp_num += '1'
        print(temp_num)
        num += temp_num

    else:
        trunct_len = len(a) - len(b)
        trunct = a[0:trunct_len]
        print(trunct)
        print(num)
        num += trunct[::-1]
    return num[::-1]


print(adds('36657567', '673537675675'))
