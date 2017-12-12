### IMPORTS ###

import os
import collections

os.chdir(r'C:\Users\kyle.rasmussen\Dropbox\Programming\AdventOfCode2017')

### INPUTS ###

with open('day6.txt') as f:
    file = f.read()

data = list(map(int, file.split()))

indices = []
temp = collections.deque(range(len(data)))
for _ in range(len(data)):
    temp.rotate()
    indices.append(list(temp))
del temp

tupData = tuple(data)

### FUNCTIONS ###

def largestBlock(arr):
    ind, val = 0, 0
    for i, j in enumerate(arr):
        if j > val:
            ind, val = i, j
    return ind, val


def incrementer(arr, val):
    return [i + 1 for i in arr], val - len(arr)

# Part 1


def memoryAllocation(arr):
    # a hash list of previous arrays
    previous = set()
    previous.add(tupData)
    while True:
        index, value = largestBlock(arr)
        # set the value given the index to zero
        arr[index] = 0
        # This allows us to initially increment by the length of the array
        while len(arr) <= value:
            arr, value = incrementer(arr, value)
        # we need to increment by value % len(data). We also need an extra rotation
        rotater = []
        for i, j in enumerate(indices):
            if j[0] == index:
                rotater = indices[i - 1]
        for i in rotater:
            if value != 0:
                arr[i] += 1
                value -= 1
            else:
                break
        # We need to add a hashable type
        tup = tuple(arr)
        if tup not in previous:
            previous.add(tup)
        else:
            break
    return len(previous)


# Part 2
def cycleLength(arr):
    count = 0
    # a hash list of previous arrays
    previous = collections.defaultdict(list)
    previous[tupData].append(count)

    while True:
        index, value = largestBlock(arr)
        # set the value given the index to zero
        arr[index] = 0
        # This allows us to initially increment by the length of the array
        while len(arr) <= value:
            arr, value = incrementer(arr, value)
        # we need to increment by value % len(data). We also need an extra rotation
        rotater = []
        for i, j in enumerate(indices):
            if j[0] == index:
                rotater = indices[i - 1]
        for i in rotater:
            if value != 0:
                arr[i] += 1
                value -= 1
            else:
                break
        # We need to add a hashable type
        tup = tuple(arr)
        if tup not in previous:
            previous[tup].append(count)
            count += 1
        else:
            previous[tup].append(count)
            count += 1
            break
    maxi = max(previous.items(), key=lambda k: len(k[1]))
    return maxi[1][1] - maxi[1][0]

### OUTPUT ###

# Part 1
print(memoryAllocation(data))

# Part 2
print(cycleLength(data))
