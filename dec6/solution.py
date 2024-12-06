from enum import Enum

class direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

class Guard():
    def __init__(self, pos, world, direction=direction.UP, obsticle_added=False):
        self.direction = direction
        self.start = pos
        self.position = pos
        self.world = world
        self.trace = set()
        self.trace.add((self.position, self.direction))
        self.possible_loops = set()
        self.obsticle_added = obsticle_added
        self.is_looping = False

    def add_trace(self):
        new_state = (self.position, self.direction)
        if new_state in self.trace:
            self.is_looping = True
            return True

        self.trace.add(new_state)
        return False

    def turn(self):
        if direction.UP == self.direction:
            self.direction = direction.RIGHT
        elif direction.DOWN == self.direction:
            self.direction = direction.LEFT
        elif direction.RIGHT == self.direction:
            self.direction = direction.DOWN
        elif direction.LEFT == self.direction:
            self.direction = direction.UP

        return not self.add_trace()

    def step(self):
        move = (0, 0)
        if direction.UP == self.direction:
            move = (-1, 0)
        elif direction.DOWN == self.direction:
            move = (1, 0)
        elif direction.RIGHT == self.direction:
            move = (0, 1)
        elif direction.LEFT == self.direction:
            move = (0, -1)

        new_position = (self.position[0] + move[0], self.position[1] + move[1])
        out_of_bounds = new_position[0] < 0 or new_position[1] < 0 or \
            new_position[0] >= len(self.world) or new_position[1] >= len(self.world[0])

        if not out_of_bounds:
            facing = world[new_position[0]][new_position[1]]
            if facing == "#":
                return self.turn() and self.step()

            # Initial strategy for solving part 2, but resulted in too many possibilites
            if not self.obsticle_added and new_position != self.start:
                self.world[new_position[0]][new_position[1]] = "#"
                alternative_guard = Guard(self.start, self.world, self.direction, True)
                alternative_guard.trace.update(self.trace)
                alternative_guard.position = self.position
                if alternative_guard.turn():
                    while alternative_guard.step():
                        continue

                self.world[new_position[0]][new_position[1]] = "."

                if alternative_guard.is_looping:
                    self.possible_loops.add(new_position)

            self.position = new_position
            return not self.add_trace()

        return not out_of_bounds


world = []
guard_pos = None

with open("input.txt", "r") as f:
    for line in f:
        if "^" in line:
            guard_pos = (len(world), line.index("^"))

        world.append(list(line.strip()))

guard = Guard(guard_pos, world, obsticle_added=True)

while guard.step():
    continue

part1 = len(set(map(lambda t: t[0], guard.trace)))

# Final strategy for solving part 2: Brute force
possible_loops = set()
for y in range(len(world)):
    print(f"Processing line {y}/{len(world)}")
    for x in range(len(world[y])):
        if world[y][x] != ".":
            continue

        world[y][x] = "#"
        guard = Guard(guard_pos, world, obsticle_added=True)

        while guard.step():
            continue

        if guard.is_looping:
            possible_loops.add((y, x))

        world[y][x] = "."

part2 = len(possible_loops)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
