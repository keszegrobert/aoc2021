import sys
lines = []
with open(sys.argv[1], "r") as f:
    lines = f.readlines()

    counter = 0
    previous = 0
    counter2 = 0
    c = 0
    s = 0
    A = 0
    B = 0
    C = 0
    for line in lines:
        meas = int(line)
        if c > 0:
            if meas > previous:
                counter += 1

            if s == 0:
                if previous < meas:
                    s = 1
                    A = meas
            elif s == 1:
                if previous < meas:
                    s = 2
                    B = meas
                else:
                    s = 0
            elif s == 2:
                if previous < meas:
                    s = 3
                    counter2 += 3
                    C = meas
                else:
                    s = 0
            else:
                if previous < meas:
                    s = 3
                    counter2 += 1
                else:
                    s = 0
        previous = meas
        c += 1
        print("c:",c,"meas:",meas,"s",s, "counter2:", counter2)
    
    print("counter:", counter)

    lines2 = lines[1:]
    lines3 = lines[2:]
    sums = [ int(lines[i]) + int(lines[i+1]) + int(lines[i+2]) for i in range(len(lines)-2)]
    print(sums)

    counter2 = 0
    for line in sums:
        meas = int(line)
        if c > 0:
            if meas > previous:
                counter2 += 1
        
        previous = meas
        c += 1
        print("c:",c,"meas:",meas,"s",s, "counter2:", counter2)

    print("sums:", counter2)
