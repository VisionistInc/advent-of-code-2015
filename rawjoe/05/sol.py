with open('input', 'r') as file:
    input = file.read()

lines = input.split ('\n')

nice = 0

for line in lines:
    if 'ab' in line:
        continue
    if 'cd' in line:
        continue
    if 'pq' in line:
        continue
    if 'xy' in line:
        continue
    
    vowles = line.count('a') + line.count('e') + line.count('i') + line.count('o') + line.count('u')
    if vowles < 3:
        continue
    
    double = False
    for i in range(len(line)-1):
        if line[i] == line[i+1]:
            double = True
            break
    if double:
        nice += 1

print("Part 1: ", nice)

nice = 0

for line in lines:

    pair = False
    for i in range(len(line)-1):
        one = line[i:i+2]
        for j in range(i+2, len(line)-1):
            if one == line[j:j+2]:
                pair = True
                break
        if pair:
            break
    if not pair:
        continue
    
    match = False
    for i in range(len(line)-2):
        if line[i] == line[i+2]:
            match = True
            break
    if match:
        nice += 1

print("Part 2: ", nice)