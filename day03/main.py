import sys

def get_counts(lines):
    counts = [ 0 ]* (len(lines[0])-1)
    for line in lines:
        line = line.strip()
        for i in range(len(line)):
            counts[i] += int(line[i])

    print(counts)
    return counts

with open( sys.argv[1], "r" )as f:
    lines = f.readlines()
    counts = get_counts(lines)
    gamma_rate = 0
    alfa_rate = 0
    for count in counts:
        gamma_rate *= 2
        alfa_rate *= 2
        if count > len(lines) / 2:
            gamma_rate += 1
        else:
            alfa_rate += 1

    print(gamma_rate)
    print(alfa_rate)
    print("result: ", alfa_rate*gamma_rate)

    column = 0

    ogen_rating = lines
    while len(ogen_rating) > 1:
        counts = get_counts(ogen_rating)
        if counts[column] >= len(ogen_rating) - counts[column]:
            ogen_rating = list(filter(lambda l: l[column] == '1', ogen_rating))
        else:
            ogen_rating = list(filter(lambda l: l[column] == '0', ogen_rating))
        #print(ogen_rating)
        column += 1 

    print('OXYGEN RATING:',ogen_rating[0])
    o2 = int(ogen_rating[0], 2)

    co2_rating = lines
    column = 0
    while len(co2_rating) > 1:
        print("column #", column)
        counts = get_counts(co2_rating)
        if counts[column] >= len(co2_rating) - counts[column]:
            co2_rating = list(filter(lambda l: l[column] == '0', co2_rating))
        else:
            co2_rating = list(filter(lambda l: l[column] == '1', co2_rating))
        print(len(co2_rating))
        column += 1 

    print(co2_rating[0])
    co2 = int(co2_rating[0],2)

    print('RESULT2:',o2,' * ',co2, ' = ', o2*co2)