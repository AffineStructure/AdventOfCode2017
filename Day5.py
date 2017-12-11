import os

os.chdir(r'C:\Users\kyle.rasmussen\Dropbox\Programming\AdventOfCode2017')

with open('day5.txt') as f:
    file = f.read()

data = list(map(int, file.split()))


def twistP1(arr):
    count = 0
    value, tmp = 0, 0
    while True:
        if value < 0 or len(arr) - 1 < value:
            return count
            break
        else:
            tmp = value
            value += arr[value]
            arr[tmp] += 1
            count += 1


def twistP2(arr):
    count = 0
    value, tmp = 0, 0
    while True:
        if value < 0 or len(arr) - 1 < value:
            return count
            break
        else:
            tmp = value
            value += arr[value]
            if arr[tmp] >= 3:
                arr[tmp] -= 1
            else:
                arr[tmp] += 1
            count += 1


print(twistP1(data))


data = list(map(int, file.split()))
print(twistP2(data))
