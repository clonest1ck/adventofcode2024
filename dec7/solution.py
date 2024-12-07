import itertools

def compute(a, b, op):
    if op == "*":
        return a * b
    elif op == "+":
        return a + b
    elif op == "||":
        return int(str(a) + str(b))

    raise ValueError(f"Unknown operator: {op}")

def solve(expected_result, data, removed_operators):
    combinations = itertools.product(removed_operators, repeat=len(data) - 1)
    for operators in combinations:
        result = data[0]
        for i, operator in enumerate(operators):
            result = compute(result, data[i+1], operator)
            if result > expected_result:
                break

        if result == expected_result:
            return True

    return False

part1 = 0
part2 = 0

with open("input.txt", "r") as f:
    for line in f:
        _result, data = line.split(":")
        data = list(map(int, data.split()))
        result = int(_result)

        if solve(result, data, ["*", "+"]):
            part1 += result
        if solve(result, data, ["*", "+", "||"]):
            part2 += result


print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

