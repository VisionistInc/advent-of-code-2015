with open('input', 'r') as file:
    input = file.read()

import hashlib

i = 0
while True:
    string = "%s%d" % (input, i)
    hash = hashlib.md5(str.encode(string)).hexdigest()
    if hash.startswith('00000'):
        break
    i += 1

print("Part 1: ", i)

i = 0
while True:
    string = "%s%d" % (input, i)
    hash = hashlib.md5(str.encode(string)).hexdigest()
    if hash.startswith('000000'):
        break
    i += 1

print("Part 2: ", i)