import sys
board = {}
with open(sys.argv[1], "r") as f:
    lines = f.readlines()
    for line in lines:
        start, arrow, end = line.split()
        sx,sy = start.split(',')
        ex,ey = end.split(',')
        startx = min(int(sx),int(ex))
        starty = min(int(sy),int(ey))
        endx = max(int(sx),int(ex))
        endy = max(int(sy),int(ey)) 
        if not(startx == endx or starty == endy):
            continue
        for i in range(startx, endx+1):
            for j in range(starty,endy+1):
                if (i,j) in board:
                    board[(i,j)] += 1
                else:
                    board[(i,j)] = 1

    counter = 0
    for pos,value in board.items():
        if value > 1:
            counter += 1
    print('RESULT:', counter)
