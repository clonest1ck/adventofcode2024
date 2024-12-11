
class Stone():
    def __init__(self, value, index, head=None, tail=None):
        self.value = value
        self.index = index

        self.head = head
        if head is None and index > 0:
            self.head = index - 1

        self.tail = tail

    def step(self, stones):
        if self.value == 0:
            self.value = 1
        else:
            s = list(str(self.value))
            if len(s) % 2 == 0:
                mid = round(len(s) / 2)
                a = int("".join(s[:mid]))
                b = int("".join(s[-mid:]))

                split = Stone(b, len(stones), self.index, self.tail)
                self.tail = len(stones)
                self.value = a
                stones.append(split)

            else:
                self.value *= 2024

    def __repr__(self):
        return repr(self.value)

def step(stones):
    stones_len = len(stones)
    for i in range(stones_len):
        stone = stones[i]
        stone.step(stones)

stones = []
with open("input.txt", "r") as f:
    for i, s in enumerate(list(map(int, f.readline().strip().split()))):
        stones.append(Stone(s, i, tail=i+1))

stones[-1].tail = None

for i in range(25):
    step(stones)

part1 = len(stones)

for i in range(75 - 25):
    step(stones)
    print(f"{i+25}: {len(stones)}")

part2 = len(stones)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

