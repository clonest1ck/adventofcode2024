import copy
from math import floor

def findFirstPrint(pages, rules):
    for first in sorted(rules.keys()):
        is_first = True
        for key, after in filter(lambda p: p[0] in pages, rules.items()):
            if first in after:
                is_first = False
                break

        if is_first:
            return first

    raise ValueError("impossible")


def generatePrintOrder(pages, _rules):
    rules = copy.deepcopy(_rules)
    order = []

    while len(rules.keys()) > 0:
        first = findFirstPrint(pages, rules)
        order.append(first)

        after = rules.pop(first)
        for page in after:
            if sum(map(lambda rule: page in rule, rules.values())) == 0 and page not in rules:
                order.append(page)
                continue

    return order

rules = dict()
prints = []
rules_done = False

with open("input.txt", "r") as f:
    for line in f:
        if line.strip() == "":
            rules_done = True
            continue

        if not rules_done:
            l, r = list(map(int, line.split("|")))
            if not l in rules:
                rules[l] = []

            rules[l].append(r)

        else:
            prints.append(list(map(int, line.split(","))))

part1 = 0
part2 = 0
for p in prints:
    print_order = generatePrintOrder(p, rules)
    middle = p[floor(len(p) / 2)]

    last_index = -1
    is_correct = True

    for page in p:
        if page not in print_order:
            continue

        index = print_order.index(page)
        if index <= last_index:
            is_correct = False
            break

        last_index = index

    if is_correct:
        part1 += middle
    else:
        correct_print = []
        for page in print_order:
            if page in p:
                correct_print.append(page)

        middle = correct_print[floor(len(p) / 2)]
        part2 += middle


print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
