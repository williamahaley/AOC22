import string
from Day3_input import actual_input


input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""
total = 0
for sack in str(actual_input).splitlines():
    dups = set([x for x in sack[len(sack)//2:] if x in sack[:len(sack)//2]])
    total += sum([string.ascii_letters.index(x)+1 for x in dups])
print(f"Part 1: {total}")
n = 0
total = 0
while n < len(str(actual_input).splitlines()):
    contents = set([x for x in "".join(str(actual_input).splitlines()[n:n+3])])
    for letter in contents:
        if letter in str(actual_input).splitlines()[n] and letter in str(actual_input).splitlines()[n+1] and letter in str(actual_input).splitlines()[n+2]:
            total += string.ascii_letters.index(letter) + 1
    n += 3
print(f"Part 2: {total}")
