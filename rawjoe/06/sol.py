with open('input', 'r') as file:
    input = file.read()

lines = input.split ('\n')

lights = [[0] * 1000 for i in range(1000)]

for line in lines:
    parts = line.split(' ')
    if parts[0] == 'toggle':
        (sx,sy) = parts[1].split(',')
        (fx,fy) = parts[3].split(',')
        for x in range(int(sx), int(fx)+1):
            for y in range(int(sy), int(fy)+1):
                if lights[x][y] == 0:
                    lights[x][y] = 1
                else:
                    lights[x][y] = 0
    else:
        if parts[1] == 'on':
            val = 1
        else:
            val = 0
        (sx,sy) = parts[2].split(',')
        (fx,fy) = parts[4].split(',')
        for x in range(int(sx), int(fx)+1):
            for y in range(int(sy), int(fy)+1):
                lights[x][y] = val

total = 0
for row in lights:
    total += sum(row)

print("Part 1: ", total)

lights = [[0] * 1000 for i in range(1000)]

for line in lines:
    parts = line.split(' ')
    if parts[0] == 'toggle':
        (sx,sy) = parts[1].split(',')
        (fx,fy) = parts[3].split(',')
        for x in range(int(sx), int(fx)+1):
            for y in range(int(sy), int(fy)+1):
                lights[x][y] += 2
    else:
        if parts[1] == 'on':
            val = 1
        else:
            val = -1
        (sx,sy) = parts[2].split(',')
        (fx,fy) = parts[4].split(',')
        for x in range(int(sx), int(fx)+1):
            for y in range(int(sy), int(fy)+1):
                lights[x][y] += val
                if lights[x][y] < 0:
                    lights[x][y] = 0

total = 0
for row in lights:
    total += sum(row)

print("Part 2: ", total)