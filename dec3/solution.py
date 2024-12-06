
def toCmd(line):
    cmd = line.replace("mul(", " mul(").replace(")", ") ").replace("do()", " do() ").replace("don't()", " don't() ").split()
    return cmd

def run(program, enabled=True, force_enable=True):
    result = 0

    for cmd in program:
        if cmd[:3] == "mul":
            try:
                a, b = list(map(int, cmd[4:-1].split(",")))

                if f"mul({a},{b})" != cmd:
                    raise ValueError()

                if enabled or force_enable:
                    result += a*b
            except Exception as e:
                continue

        elif cmd == "do()":
            enabled = True
        elif cmd == "don't()":
            enabled = False

    return result, enabled

part1 = 0
part2 = 0
enabled = True

with open("input.txt", "r") as f:
    for line in f:
        program = toCmd(line)
        result, _ = run(program)
        part1 += result

        result, enabled = run(program, enabled, False)
        part2 += result


print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
