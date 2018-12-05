with open('input', 'r') as file:
    input = file.read()

lines = input.split('\n')

paper = 0
ribbon = 0

for line in lines:
    dims = line.split('x')
    dims = [int(x) for x in dims]

    # part 1
    areas = [dims[0] * dims[1], dims[0] * dims[2], dims[1] * dims[2]]
    for area in areas:
        paper += (2 * area)
    paper += min(areas)

    # part 2
    smallest = min(dims)
    dims.remove(smallest)
    mid = min(dims)
    dims.remove(mid)
    ribbon += (2* smallest)
    ribbon += (2* mid)
    ribbon += (smallest * mid * dims[0])

print("Part 1: ", paper)
print("Part 2: ", ribbon)