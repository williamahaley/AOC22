import re
import pandas as pd
from Day5_input import actual_input

input = """   
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""
stacks, directions = actual_input.split("\n\n")

cleaned_directions = [re.sub("\D+", ",", x) for x in directions.splitlines()]

cleaned_stacks = []
for n in range(len(stacks.splitlines())):
    cleaned_stacks.append([stacks.splitlines()[n][i:i+4] for i in range(0, len(stacks.splitlines()[n]), 4)])
rows = [[y if y.strip() != "" else None for y in x] for x in cleaned_stacks]
data = pd.DataFrame(rows)[1:-1]
data = data.iloc[::-1].reset_index(drop=True)

y_count = sum(list(data.count()))
data = data.reindex(index=range(y_count))
for command in cleaned_directions:
    _, number, start, end = command.split(",")
    source_index = data[int(start) - 1].last_valid_index() - (int(number) - 1)
    source_values = data[int(start) - 1][source_index:source_index + int(number)].to_list()
    end_index = 0 if data[int(end) - 1][0] is None else data[int(end) - 1].last_valid_index() + 1
    #  If you want the Part 1 answer uncomment the reverse...  too lazy to even copy/paste this shit
    #  source_values.reverse()
    data[int(end) - 1][end_index:end_index + int(number)] = source_values
    data[int(start) - 1][source_index:source_index + int(number)] = None

for n in range(len(data.columns)):
    print(data[n][data[n].last_valid_index()])

