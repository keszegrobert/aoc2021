import sys

with open(sys.argv[1], "r") as f:
    lines = f.readlines()
    depth = 0
    distance = 0
    aim = 0
    depth2 = 0
    for line in lines:
        dir, step = line.split()
        print(dir, step)
        if dir == "forward":
            distance += int(step)
            depth2 += depth*int(step)
        elif dir == "up":
            depth -= int(step)
        elif dir == "down":
            depth += int(step)

print("depth:", depth)
print("distance:", distance)
print("result:",distance*depth)
print("result2:", distance*depth2)