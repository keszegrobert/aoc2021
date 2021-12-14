import sys

def asorted(digit):
    d = []
    d[:0] = digit
    s = sorted(d)
    return ''.join(s)

def solve(digits):
    mapping = {}
    for digit in digits:
        if len(digit) == 7:
            mapping[asorted(digit)] = 8
        if len(digit) == 2:
            mapping[asorted(digit)] = 1
        if len(digit) == 4:
            mapping[asorted(digit)] = 4
        if len(digit) == 3:
            mapping[asorted(digit)] = 7

    return mapping

with open(sys.argv[1], "r") as f:
    numbers = [ line.split('|') for line in f.readlines()]
    counter = 0
    sum = 0
    for digits, number in numbers:
        print(number.split())
        for n in number.split():
            if len(n) in [2,4,3,7]:
                counter +=1

        mapping = solve(digits.split())
        nn = 0
        for n in number.split():
            nn *= 10
            ns = asorted(n)
            nn += mapping[ns]
        sum += nn
            
    print('RESULT:', counter)
    print('RESULT2:',sum)


