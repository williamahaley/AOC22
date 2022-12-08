from anytree import Node
import re
from Day7_input import actual_input


input = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""
current: str
parent: str
nodes = {}
cleaned_input = input.replace("/", "0")
lines = cleaned_input.splitlines()
for idx in range(len(lines)):
    command = lines[idx]
    if lines[idx].startswith("$ cd"):
        _, command, dir = lines[idx].split(" ")
        if dir == "..":
            current = nodes[current].parent.name
            print(f"move back: {command} {dir} to ")
            continue
        elif dir not in nodes.keys():
            print(f"creating Node: {command} {dir}")
            nodes[dir] = Node(dir)
        current = dir
    elif lines[idx].startswith("$ ls"):
        print(f"Listing items: {command}")
        continue
    elif re.match(r"^\D", lines[idx]):
        print(f"Found Directory: {command}")
        nodes[lines[idx].split(" ")[1]] = Node(lines[idx].split(" ")[1], parent=nodes[current])
    elif re.match(r"^\d", lines[idx]):
        print(f"Found File: {command}")
        nodes[lines[idx]] = Node(lines[idx], parent=nodes[current])

folders = [x for x in nodes.keys() if re.match(r"^\D", x)]
sizes = {}
for folder in folders:
    sizes[folder] = sum([int(str(x.name).split(" ")[0]) for x in nodes[folder].descendants if re.match(r"^\d", x.name)])
    pass
total = sum([x for x in sizes.values() if x <= 100000])
print(f"Part One: {total}")
# small       1,414,917
# large     184,750,813
# All       186,165,730