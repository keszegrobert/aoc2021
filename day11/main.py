import sys
    
t = [
    1,1,1,1,1,
    1,9,9,9,1,
    1,9,1,9,1,
    1,9,9,9,1,
    1,1,1,1,1
]

class Territory:
    def __init__(self, _t, _h, _w):
        self.table = _t
        self.height = _h
        self.width = _w

    def print_table(self):
        for i in range(self.height):
            l = ''
            for j in range(self.width):
                decorator = ' '
                current = self.table[i*self.width+j]
                l += str(current) + decorator
            print(l)
        print()

    def count_flash_neighbours(self, posy, posx):
        inc = 0
        for ii in range(posy-1,posy+2):
            if ii < 0:
                continue
            if ii >= self.height:
                continue
            for jj in range(posx-1, posx+2):
                if jj < 0:
                    continue
                if jj >= self.width:
                    continue
                if ii == posy and jj == posx:
                    continue
                #print(ii,jj)
                if self.table[ii*self.width+jj] > 9:
                    inc += 1
        #print('for',posy, posx, 'returning', inc)
        return inc

    def update_neighbours(self, posy, posx):
        if self.table[posy*self.width+posx] < 10:
            return
        for ii in range(posy-1,posy+2):
            if ii < 0:
                continue
            if ii >= self.height:
                continue
            for jj in range(posx-1, posx+2):
                if jj < 0:
                    continue
                if jj >= self.width:
                    continue
                if ii == posy and jj == posx:
                    continue
                #print(ii,jj)
                self.table[ii*self.width+jj] += 1

    def step(self):
        p = self.table.copy()
        self.print_table()

        for i in range(self.height):
            for j in range(self.width):
                p[i*self.width+j] += 1

        self.table = p.copy()
        print('After incrementing')
        self.print_table()

        for i in range(self.height):
            for j in range(self.width):
                self.update_neighbours(i, j)

        print('After updating the neighbours')
        self.print_table()

        counter = 0
        for i in range(self.height):
            for j in range(self.width):
                if self.table[i*self.width+j] > 9:
                    self.table[i*self.width+j] = 0

        print('After zeroing')
        self.print_table()
        return p

terr = Territory(t, 5, 5)
p = terr.step()
p = terr.step()
#exit()
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
    terr = Territory(territory, height, width)
    counter = 0
    for i in range(2):
        terr.step()
