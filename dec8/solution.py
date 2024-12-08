import itertools


def in_map(a, world):
    return a[0] >= 0 and a[1] >= 0 and a[0] < world[0] and a[1] < world[1]

def part1_antinodes(a, b, world_bound):
    antinodes = set()

    d_y = a[0] - b[0]
    d_x = a[1] - b[1]

    candidate_a = (a[0] - 2 * d_y, a[1] - 2 * d_x)
    candidate_b = (a[0] + d_y, a[1] + d_x)

    if in_map(candidate_a, world_bound):
        antinodes.add(candidate_a)

    if in_map(candidate_b, world_bound):
        antinodes.add(candidate_b)

    return antinodes

def part2_antinodes(a, b, world_bound):
    antinodes = set()

    d_y = a[0] - b[0]
    d_x = a[1] - b[1]

    i = 0
    while True:
        candidate = (a[0] + i * d_y, a[1] + i * d_x)
        if not in_map(candidate, world_bound):
            break

        antinodes.add(candidate)
        i += 1

    i = -1
    while True:
        candidate = (a[0] + i * d_y, a[1] + i * d_x)
        if not in_map(candidate, world_bound):
            break

        antinodes.add(candidate)
        i -= 1

    return antinodes

part1 = 0
part2 = 0

max_y = 0
max_x = 0

antennas = dict()
world = []

with open("input.txt", "r") as f:
    for y, line in enumerate(f):
        world.append(list(line.strip()))
        for x, antenna in enumerate(list(line.strip())):
            if antenna == ".":
                continue

            if antenna not in antennas:
                antennas[antenna] = []

            antennas[antenna].append((y, x))

antinodes = set()
antinodes_part2 = set()
world_bound = (len(world), len(world[0]))

for antenna, locations in antennas.items():
    for a, b in itertools.combinations(locations, 2):
        nodes = part1_antinodes(a, b, world_bound)
        antinodes.update(nodes)

        nodes = part2_antinodes(a, b, world_bound)
        antinodes_part2.update(nodes)

print(f"Part 1: {len(antinodes)}")
print(f"Part 2: {len(antinodes_part2)}")

