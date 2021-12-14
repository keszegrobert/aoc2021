import sys

def parsechar(ch, line, pos, maxpos):
    if line[pos] == ch:
        print(pos, 'Found ', ch)
        return pos+1
    return pos

def parse(line, pos, maxpos):
    if pos+1 == maxpos:
        print('parsing succeeded')
        return maxpos
    print(pos, 'Parsing ', line[pos])
    res = pos
    while res < maxpos:
        res = parsechar('{', line, pos, maxpos)
        if res > pos:
            res = parse(line,res, maxpos)
            post = parsechar('}', line, res, maxpos)
            if post == res:
                raise Exception('}',line[res])
            return post
        res = parsechar('[', line, pos, maxpos)
        if res > pos:
            res = parse(line,res, maxpos)
            post = parsechar(']', line, res, maxpos)
            if post == res:
                raise Exception(']',line[res])
            return post
        res = parsechar('<', line, pos, maxpos)
        if res > pos:
            res = parse(line,res, maxpos)
            post = parsechar('>', line, res, maxpos)
            if post == res:
                raise Exception('>',line[res])
            return post
        res = parsechar('(', line, pos, maxpos)
        if res > pos:
            res = parse(line,res, maxpos)
            post = parsechar(')', line, res, maxpos)
            if post == res:
                raise Exception(')',line[res])
            return post
        break
    return res  
        
with open(sys.argv[1], "r") as f:
    lines = f.readlines()
    for line in lines:
        try:
            parse(line, 0, len(line))
        except Exception as exc:
            e,g = exc.args
            print('Expected:', e, 'but found', g, 'instead')

        print(' ')
        break
