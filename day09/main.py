import sys

with open(sys.argv[1], "r") as f:
    territory = []
    width = 0
    height = 0
    for row in f.readlines():
        width = len(row.strip())
        for number in row.strip():
            territory.append(int(number))
        height += 1

    print('HEIGHT:', height)
    print('WIDTH:', width)

    counter = 0
    for i in range(height):
        l = ''
        for j in range(width):
            decorator = ' '
            neighbours = []
            current = territory[i*width+j]
            if i > 0:
                neighbours.append(territory[(i-1)*width+j])
            if i < height-1:
                neighbours.append(territory[(i+1)*width+j])
            if j > 0:
                neighbours.append(territory[i*width+(j-1)])
            if j < width-1:
                neighbours.append(territory[i*width+(j+1)])
            
            lowest = True
            for n in neighbours:
                lowest &= ( current < n )

            if lowest:
                decorator = '*'
                counter += 1+current
            
            l += str(territory[i*width+j]) + decorator
        print(l)
    print('RESULT:', counter)
