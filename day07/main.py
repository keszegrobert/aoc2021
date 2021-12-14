import sys

def cost(nums, pos):
    c = 0
    for num in nums:
        c+= abs(num-pos)
    return c

def cost2(nums, pos):
    c = 0
    for num in nums:
        diff = abs(num - pos)
        co = ( diff * (diff+1) ) / 2
        #print('From', num, 'to', pos, ':', co, 'fuel')
        c += co
    return c

with open(sys.argv[1], "r") as f:
    numbers = [int(n) for n in f.readline().split(',')]
    print(numbers)
    prev = 1000000
    for i in range(1000000):
        total = cost(numbers, i)
        print('#',i, ':', total)
        if prev < total:
            print('RESULT:',i-1, ':', prev)
            break
        prev = total

    prev = 1000000000
    for i in range(1000000000):
        total = cost2(numbers, i)
        print('#',i, ':', total)
        if prev < total:
            print('RESULT2:',i-1, ':', prev)
            break
        prev = total
