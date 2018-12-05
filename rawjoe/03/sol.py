with open('input', 'r') as file:
    input = file.read()

houses = set()
x = 0
y = 0

houses.add("0,0")

for c in input:
    if c is '>':
        x += 1
    elif c is '<':
        x -= 1
    elif c is '^':
        y += 1
    elif c is 'v':
        y -= 1
    houses.add("%d,%d" % (x,y))

print("Part 1: ", len(houses))

houses = set()
x1 = 0
y1 = 0
x2 = 0
y2 = 0

houses.add("0,0")

for i in range(len(input)):
    c = input[i]
    if i % 2 == 0:
        if c is '>':
            x1 += 1
        elif c is '<':
            x1 -= 1
        elif c is '^':
            y1 += 1
        elif c is 'v':
            y1 -= 1
        houses.add("%d,%d" % (x1,y1))
    else:
        if c is '>':
            x2 += 1
        elif c is '<':
            x2 -= 1
        elif c is '^':
            y2 += 1
        elif c is 'v':
            y2 -= 1
        houses.add("%d,%d" % (x2,y2))

print("Part 2: ", len(houses))