import sys

def printboards(boards):
    for board in boards:
        print(board)

def check_score(score):
    successcolumn = False
    successrow = False
    for i in range(5):
        sor=0
        oszlop=0
        for j in range(5):
            sor += int(score[i*5+j])
            oszlop += int(score[j*5+i])
        if sor == 5:
            successrow = True
            print('Success in row:',i)
            break
        if oszlop == 5:
            successcolumn = True
            print('Success in column:',i)
            break
    return successrow, successcolumn


with open(sys.argv[1], "r") as f:
    lines = f.readlines()

    counter = 0
    numbers = []
    board = []
    boards = []
    scores = []
 
    for line in lines:
        counter += 1
        if counter == 1:
            numbers =[str(n) for n in lines[0].split(',')]
            continue
        if counter > 2 and counter % 6 == 2:
            scores.append(['0']*25)
            boards.append(board.copy())
            board = [] 
            continue
        board.extend(line.split())
    boards.append(board.copy())
    scores.append(['0']*25)
    printboards(boards)
    sum = 0

    winners = []
    w = set()
    for number in numbers:
        numSuccess = False
        print('#',number)
        counter = 0
        for counter in range(len(boards)):
            if counter in w:
                continue
            try:
                ix = boards[counter].index(number)
                print('found ',number, ' on ', ix)
                score = scores[counter]
                score[ix] = '1'
            except ValueError:
                continue

            successrow,successcolumn = check_score(scores[counter])
            if (successrow or successcolumn ):
                print('Match in board:', counter)
                
                numSuccess = True
                print(board)
                print(scores[counter])
                for x in range(25):
                    sum += (1-int(scores[counter][x]))*int(boards[counter][x])
                print('The SUM is:',sum)
                winners.append((counter, sum, int(number)))
                sum = 0
                w.add(counter)

        if numSuccess:
            print('The current number is:', number)
            print('RESULT IS:', sum*int(number))
            #break

    print(winners)
    lastboard, lastsum, lastnum = winners[-1]
    print('RESULT:', lastsum*lastnum)