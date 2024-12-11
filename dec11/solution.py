
def step(value, steps, visited):
    if steps == 0:
        return 1

    if (value, steps) in visited:
        return visited[(value, steps)]

    new_value = value
    split_stones = 0
    if value == 0:
        new_value = 1
    else:
        s = list(str(value))
        if len(s) % 2 == 0:
            mid = round(len(s) / 2)
            new_value = int("".join(s[:mid]))
            split = int("".join(s[-mid:]))

            split_stones = step(split, steps - 1, visited)
        else:
            new_value = value * 2024

    stones = step(new_value, steps - 1, visited)
    visited[(value, steps)] = stones + split_stones

    return stones + split_stones

visited = dict()
stones = []
with open("input.txt", "r") as f:
    stones = list(map(int, f.readline().strip().split()))

part1 = 0
for stone in stones:
    part1 += step(stone, 25, visited)

part2 = 0
for stone in stones:
    part2 += step(stone, 75, visited)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

