import sys

empty = { 0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0 }
with open(sys.argv[1], "r") as f:
    numbers = [int(n) for n in f.readline().split(',')]
    numbermap = empty.copy()
    for n in numbers:
        numbermap[n] += 1
    print(numbermap)
    for counter in range(256):
        result = {}
        result[0] = numbermap[1]
        result[1] = numbermap[2]
        result[2] = numbermap[3]
        result[3] = numbermap[4]
        result[4] = numbermap[5]
        result[5] = numbermap[6]
        result[6] = numbermap[7]+numbermap[0]
        result[7] = numbermap[8]
        result[8] = numbermap[0]

        numbermap = result.copy()

        print('After ', counter+1, 'days:', sum(numbermap.values()))
    print('RESULT:',len(numbermap))
