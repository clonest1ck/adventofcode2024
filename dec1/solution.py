
left = []
right = []

with open("input.txt", "r") as f:
    for line in f: 
        l, r = line.split()
        left.append(int(l))
        right.append(int(r))

left.sort()
right.sort()

distance = 0

for i in range(len(left)):
    distance += abs(left[i] - right[i])

print(f"Part 1: {distance}")

similarity = 0

for value in left:
    similarity += right.count(value) * value

print(f"Part 2: {similarity}")
