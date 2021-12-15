lines = open('input.txt', 'r').read().splitlines()
inputs = [[set(sorted(word)) for word in line.replace('|', '').split()] for line in lines]
outputs = [line.split('|')[1].split() for line in lines]
def digit_set(digit, length):
    return next(filter(lambda x: len(x) == length, digit))
res = 0
for ip, out in zip(inputs, outputs):
    digits = [{}] * 10
    digits[1] = digit_set(ip, 2)
    digits[4] = digit_set(ip, 4)
    digits[7] = digit_set(ip, 3)
    digits[8] = digit_set(ip, 7)
    ip = filter(lambda x: len(x) not in [2, 4, 3, 7], ip)
    for digit in ip:
        d = set([c for c in digit])
        if len(digit) == 5:
            if len(digit.intersection(digits[1])) == 2:
                digits[3] = digit
            elif len(digit.intersection(digits[4])) == 3:
                digits[5] = digit
            else:
                digits[2] = digit
        elif len(digit) == 6:
            if len(digit.intersection(digits[4])) == 4:
                digits[9] = digit
            elif len(digit.intersection(digits[1])) == 2:
                digits[0] = digit
            else:
                digits[6] = digit
    res += int("".join(str(digits.index(set(sorted(digit)))) for digit in out))
print(res)
