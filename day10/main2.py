import sys

s = { ')': 1, ']': 2, '}':3, '>':4}

def parse(line, pos, maxpos):
    stack = []
    while pos < maxpos:
        current = line[pos]
        if current == '(':
            stack.append(')')
        elif current == '{':
            stack.append('}')
        elif current == '[':
            stack.append(']')
        elif current == '<':
            stack.append('>')
        else:
            top = stack.pop()
            if top != current:
                raise Exception(top, current)
        pos+=1
    result = 0
    for v in stack[::-1]:
        result *= 5
        result += s[v]
        #print(result)
    print(''.join(stack[::-1]), result)
    return result 

points ={
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

with open(sys.argv[1], "r") as f:
    lines = f.readlines()
    counter = 0
    sum = 0
    scores = []
    for line in lines:
        counter +=1
        try:
            t = parse(line.strip(), 0, len(line)-1)
            scores.append(t)
        except Exception as exc:
            e,g = exc.args
            print(counter, 'Expected:', e, 'but found', g, 'instead')
            sum += points[g]
    print('RESULT:', sum)
    sscores = sorted(scores)
    print('SCORE:', sscores[len(sscores)//2])