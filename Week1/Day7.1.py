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
folders = {"/": 0}
pwd = "/"
for line in actual_input.splitlines():
    if line.startswith("$ ls"):
        continue
    elif line.startswith("$ cd .."):
        pwd = "/".join(pwd.split("/")[0:-2]) + "/"
    elif line.startswith("$ cd /"):
        pwd = "/"
    elif line.startswith("$ cd"):
        _, command, change_to = line.split(" ")
        pwd = f"{pwd}{change_to}/"
    elif line.startswith("dir"):
        folders[f"{pwd}{line.split(' ')[-1]}/"] = 0
    else:
        folders[pwd] += int(line.split(" ")[0])
folder_names = list(folders.keys())
for idx in range(len(folder_names)):
    folders[folder_names[idx]] = sum([int(folders[x]) for x in folder_names if str(x).startswith(folder_names[idx])])
print(f"Part 1: {sum([x for x in folders.values() if x <=1e5])}")

# Part 2
max_size = 7e7
used = folders["/"]
delta = 3e7 - (max_size - used)
print(f"Part 2: { min([x for x in folders.values() if x >= delta])}")

