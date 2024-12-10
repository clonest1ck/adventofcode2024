
def traceUniqueEnds(x, y, world, visited):
    if (x, y) in visited:
        return 0

    visited[(x, y)] = True

    height = world[y][x]
    if height == 9:
        return 1

    left = world[y][x-1]
    right = world[y][x+1]
    down = world[y+1][x]
    up = world[y-1][x]

    score = 0
    if left == height + 1:
        score += traceUniqueEnds(x-1, y, world, visited)
    if right == height + 1:
        score += traceUniqueEnds(x+1, y, world, visited)
    if down == height + 1:
        score += traceUniqueEnds(x, y+1, world, visited)
    if up == height + 1:
        score += traceUniqueEnds(x, y-1, world, visited)

    return score

def traceDistinct(x, y, world, visited):
    if (x, y) in visited:
        return visited[(x, y)]

    height = world[y][x]
    if height == 9:
        return 1

    left = world[y][x-1]
    right = world[y][x+1]
    down = world[y+1][x]
    up = world[y-1][x]

    score = 0
    if left == height + 1:
        score += traceDistinct(x-1, y, world, visited)
    if right == height + 1:
        score += traceDistinct(x+1, y, world, visited)
    if down == height + 1:
        score += traceDistinct(x, y+1, world, visited)
    if up == height + 1:
        score += traceDistinct(x, y-1, world, visited)

    visited[(x, y)] = score

    return score


world = []
with open("example.txt", "r") as f:
    for line in f:
        world.append([-1] + list(map(int, list(line.strip()))) + [-1])

world.insert(0, [-1 for x in range(len(world[0]))])
world.append([-1 for x in range(len(world[0]))])

part1 = 0
for y, row in enumerate(world):
    for x, height in enumerate(row):
        if height == 0:
            visited = dict()
            score = traceUniqueEnds(x, y, world, visited)
            part1 += score

part2 = 0
visited = dict()
for y, row in enumerate(world):
    for x, height in enumerate(row):
        if height == 0:
            score = traceDistinct(x, y, world, visited)
            part2 += score

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

