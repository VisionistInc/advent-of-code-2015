with open('input', 'r') as file:
    input = file.read()

lines = input.split ('\n')

class Step:
    # Constructor method
    def __init__(self, op, in1, in2):
        self.op = op
        self.value = None
        self.input1 = in1
        self.input2 = in2
    
    def eval(self):
        try:
            in1 = int(self.input1)
            if self.op == 'INIT':
                self.value = in1
            
            if self.op == 'NOT':
                self.value = (~in1)&0xFFFF

            in2 = int(self.input2)
            if self.op == 'AND':
                self.value = in1 & in2
            
            if self.op == 'OR':
                self.value = in1 | in2
            
            if self.op == 'LSHIFT':
                self.value = (in1 << in2) & 0xFFFF

            if self.op == 'RSHIFT':
                self.value = (in1 >> in2) & 0xFFFF
        except:
            pass

steps = dict()

for line in lines:
    parts = line.split()
    if len(parts) == 3:
        steps[parts[2]] = Step('INIT', parts[0], None)
    elif len(parts) == 4:
        steps[parts[3]] = Step('NOT', parts[1], None)
    else:
        steps[parts[4]] = Step(parts[1], parts[0], parts[2])

import copy
saved_steps = copy.deepcopy(steps)

while True:
    # evaluate as much as we can
    updated = []
    for k,v in steps.items():
        v.eval()
        if v.value != None:
            updated.append(k)
    
    # if we have a's value, we are good
    if 'a' in updated:
        break

    # update inputs
    for k,v in steps.items():
        if v.input1 in updated:
            v.input1 = steps[v.input1].value
        if v.input2 in updated:
            v.input2 = steps[v.input2].value

    # remove evaluated
    for i in updated:
        del steps[i]

val = steps['a'].value

print("Part 1: ", val)

steps = saved_steps

del steps['b']

steps['b'] = Step('INIT', val, None)

while True:
    # evaluate as much as we can
    updated = []
    for k,v in steps.items():
        v.eval()
        if v.value != None:
            updated.append(k)
    
    # if we have a's value, we are good
    if 'a' in updated:
        break

    # update inputs
    for k,v in steps.items():
        if v.input1 in updated:
            v.input1 = steps[v.input1].value
        if v.input2 in updated:
            v.input2 = steps[v.input2].value

    # remove evaluated
    for i in updated:
        del steps[i]

val = steps['a'].value

print("Part 2: ", val)