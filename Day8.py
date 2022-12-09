import numpy as np

from Day8_input import actual_input
import numpy as np

input = """30373
25512
65332
33549
35390"""

'''
input = \
"""12345
67890
12345
67890
12345"""
'''
column_hs = []

height_grid = np.array([[int(y) for y in x] for x in actual_input.splitlines()])
vis_grid = np.array([[-1 for y in x] for x in actual_input.splitlines()])
r_len, c_len = height_grid.shape
vis_count = 0
for y in range(0, height_grid.shape[0]):
    for x in range(0, height_grid.shape[1]):
        if not y or not x or x == height_grid.shape[1]-1 or y == height_grid.shape[0]-1:
            vis_grid[x, y] = 1
        elif vis_grid[x][y] > -1:
            continue
        elif height_grid[x][y] > max(height_grid[x][:y]):
            vis_grid[x, y] = 1
        elif height_grid[x][y] > max(height_grid[x][y+1:]):
            vis_grid[x, y] = 1
        elif height_grid[x, y] > max(height_grid[:, y][:x]):
            vis_grid[x, y] = 1
        elif height_grid[x, y] > max(height_grid[:, y][x+1:]):
            vis_grid[x, y] = 1
        else:
            vis_grid[x, y] = 0
        vis_count += vis_grid[x, y]
    pass

print(f"Part 1: {vis_count}")
# 1702 is not the answer


def count_trees(base, trees):
    moves = 0
    for cell in trees:
        if cell >= base:
            moves += 1
            return moves
        else:
            moves += 1
    return moves


scenic_grid = np.array([[0 for y in x] for x in actual_input.splitlines()])
for y in range(0, height_grid.shape[0]):
    for x in range(0, height_grid.shape[1]):
        score = []
        if not x or not y:
            score.append(0)
        elif x == height_grid.shape[1]-1 or y == height_grid.shape[0]-1:
            score.append(0)
        else:
            score.append(count_trees(height_grid[x][y], np.flip(height_grid[:, y][:x])))  # up
            score.append(count_trees(height_grid[x][y], np.flip(height_grid[x][:y])))  # left
            score.append(count_trees(height_grid[x][y], height_grid[:, y][x + 1:]))  # down
            score.append(count_trees(height_grid[x][y], height_grid[x][y + 1:]))  # right
            scenic_grid[x][y] = np.prod(score)

print(f"Part 2: {np.amax(scenic_grid)}")