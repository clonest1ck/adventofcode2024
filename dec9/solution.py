part1 = 0
part2 = 0

free_chunks = []
data = []

class Chunk:
    def __init__(self, start, length, value=None):
        self.start = start
        self.length = length
        self.value = value

    def checksum(self):
        if self.value is None:
            return 0

        csm = 0
        for pos in range(self.start, selfstart + self.length):
            csm += pos * self.value

        return csm

    def __repr__(self):
        s = "."
        if self.value is not None:
            s = str(self.value)
        return "".join([s for x in range(self.length)])

    def __get_start__(self):
        return self.start

def get_last_chunk(memory):
    return list(filter(lambda x: x.value is not None, memory))[-1]

def fit(chunk, memory, free_chunks):
    free_chunks_to_fill = []
    free_chunks_to_fill_size = 0
    i = 0

    while free_chunks_to_fill_size < chunk.length:
        free_chunk = free_chunks.pop(0)
        if free_chunks_to_fill_size + free_chunk.length > chunk.length:
            space_left = free_chunks_to_fill_size + free_chunk.length - chunk.length
            new_chunk = Chunk(free_chunk.start + chunk.length, space_left)
            free_chunk.length -= space_left
            free_chunks.insert(0, new_chunk)
            memory.append(new_chunk)
            memory.sort(key=Chunk.__get_start__)

        free_chunks_to_fill.append(free_chunk)
        free_chunks_to_fill_size += free_chunk.length

    for free_chunk in free_chunks_to_fill:
        free_chunk.value = chunk.value
    chunk.value = None
    free_chunks.append(chunk)
    free_chunks.sort(key=Chunk.__get_start__)

def fragment(memory, free_chunks):
    next_free_block = free_chunks[0].start
    last_used_chunk = get_last_chunk(memory)
    last_used_block = last_used_chunk.start + last_used_chunk.length

    while next_free_block < last_used_block:
        fit(last_used_chunk, memory, free_chunks)

        next_free_block = free_chunks[0].start
        last_used_chunk = get_last_chunk(memory)
        last_used_block = last_used_chunk.start + last_used_chunk.length


def defragment(memory, free_chunks):
    for chunk in list(reversed(memory)):
        if chunk.value is None:
            continue

        free_chunks_large_enough = list(filter(lambda c: c.length >= chunk.length, free_chunks))

        if len(free_chunks_large_enough) == 0:
            continue

        free_chunk = free_chunks_large_enough[0]
        if free_chunk.start < chunk.start:
            free_chunks.remove(free_chunk)

            if free_chunk.length > chunk.length:
                space_left = free_chunk.length - chunk.length
                new_chunk = Chunk(free_chunk.start + chunk.length, space_left)
                free_chunk.length -= space_left
                free_chunks.insert(0, new_chunk)
                memory.append(new_chunk)
                memory.sort(key=Chunk.__get_start__)
                free_chunks.sort(key=Chunk.__get_start__)

            free_chunk.value = chunk.value
            chunk.value = None


def print_memory(memory):
    mem_str = "".join(map(repr, sorted(memory, key=Chunk.__get_start__)))
    print(mem_str)
    return mem_str

def checksum(memory):
    checksum = 0
    index = 0
    for chunk in memory:
        if chunk.value is not None:
            for i in range(chunk.length):
                checksum += chunk.value * index
                index += 1
        else:
            index += chunk.length

    return checksum

def decompress(compressed):
    memory = []
    free_chunks = []

    index = 0
    value = 0
    contains_data = True

    for c in compressed:
        length = int(c)
        data = None
        if contains_data:
            data = value
            value += 1

        entry = Chunk(index, length, data)
        index += length

        memory.append(entry)

        if not contains_data:
            free_chunks.append(entry)

        contains_data = not contains_data

    return memory, free_chunks

with open("input.txt", "r") as f:
    data = list(f.readline().strip())

memory, free_chunks = decompress(data)
fragment(memory, free_chunks)
part1 = checksum(memory)

memory, free_chunks = decompress(data)
defragment(memory, free_chunks)
part2 = checksum(memory)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

