from Day4_input import actual_input


input = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

total_overlap = 0
partial_overlap = 0
for pair in actual_input.splitlines():
    elf1, elf2 = pair.split(",")
    r1 = list(range(int(elf1.split("-")[0]), int(elf1.split("-")[1])+1))
    r2 = list(range(int(elf2.split("-")[0]), int(elf2.split("-")[1])+1))
    total_overlap += 1 if (all(x in r1 for x in r2) or all(x in r2 for x in r1)) else 0
    partial_overlap += 1 if (any(x in r1 for x in r2) or any(x in r2 for x in r1)) else 0
print(f"Part 1: {total_overlap}")
print(f"Part 1: {partial_overlap}")
