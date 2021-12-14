import sys
board = {}
with open(sys.argv[1], "r") as f:
    lines = f.readlines()
    counter = 0
    for line in lines:
        print('\n', line.strip())
        start, arrow, end = line.split()
        sx,sy = start.split(',')
        ex,ey = end.split(',')
        startx = int(sx)
        starty = int(sy)

        endx =int(ex)
        endy = int(ey)
        dx = (endx!=startx) and (endx-startx>0 and 1 or -1) or 0
        dy = (endy!=starty) and (endy-starty>0 and 1 or -1) or 0
        #print(dx,dy)
        xx = startx
        yy = starty
        while xx != endx + dx or yy != endy + dy:
            #print(xx, yy)
            if (xx, yy) in board:
                board[(xx, yy)] += 1
                #print('DUPLICATE1:',xx, ',', yy)
            else:
                board[(xx,yy)] = 1
            xx += dx
            yy += dy
            
    print('SUMMARY')
    counter = 0
    for pos,val in board.items():
        if val > 1:
            counter += 1
        #print(pos, val)
    print('RESULT:', counter)
