with open('input', 'r') as file:
    input = file.read()

up = input.count('(')
down = input.count(')')

print("Part 1: %d" % (up-down))

floor = 0
count = 0
for c in input:
    count += 1
    if c is '(':
        floor += 1
    else:
        floor -= 1
    
    if floor == -1:
        break

print("Part 2: %d" % count)
