
def getWords(x, y, data):
    words = [
        data[y][x:x+4],     # forwards
        [data[y][x - i] for i in range(0, 4)],  # backwards
        [data[y + i][x] for i in range(0, 4)],  # downwards
        [data[y - i][x] for i in range(0, 4)],  # upwards
        [data[y + i][x + i] for i in range(0, 4)], # diagonal downright
        [data[y - i][x + i] for i in range(0, 4)], # diagonal upright
        [data[y + i][x - i] for i in range(0, 4)], # diagonal downleft
        [data[y - i][x - i] for i in range(0, 4)], # diagonal upleft
    ]

    return list(map(lambda s: "".join(s), words))

def getCross(x, y, data):
    words = [
        [data[y + i][x + i] for i in range(-1, 2)], # lower left -> upper right
        [data[y + i][x - i] for i in range(-1, 2)]  # upper right -> lower left
    ]

    return list(map(lambda s: "".join(s), words))

game = []
padding = list("...")

with open("input.txt", "r") as f:
    for line in f:
        game.append(padding + list(line.strip()) + padding)

game.append(["." for x in game[0]])
game.append(["." for x in game[0]])
game.append(["." for x in game[0]])
game.insert(0, ["." for x in game[0]])
game.insert(0, ["." for x in game[0]])
game.insert(0, ["." for x in game[0]])


xmas = 0
mas_cross = 0
for y in range(len(game)):
    for x in range(len(game[y])):
        if game[y][x] == "X":
            words = getWords(x, y, game)
            for word in words:
                if "".join(word) == "XMAS":
                    xmas += 1
        if game[y][x] == "A":
            words = getCross(x, y, game)

            if (words[0] == "MAS" or words[0] == "SAM") and (words[1] == "MAS" or words[1] == "SAM"):
                mas_cross += 1


print(f"Part 1: {xmas}")
print(f"Part 2: {mas_cross}")
