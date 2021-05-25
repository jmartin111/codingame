#! venv/bin/python
import sys

# building dimensions
width, height = [int(i) for i in input().split()]

# maximum number of turns before game over.
turns_allowed = int(input())

# the Detective's starting point
bx, by = [int(i) for i in input().split()]

# directional modifiers
vectors = {
    "U": (0, -1),
    "UR": (1, -1),
    "R": (1, 0),
    "DR": (1, 1),
    "D": (0, 1),
    "DL": (-1, 1),
    "L": (-1, 0),
    "UL": (-1, -1)
}

# game loop
while True:
    # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    bomb_dir = input()
    print(f"{bomb_dir}", file=sys.stderr, flush=True)

    jump_x = bx + vectors[bomb_dir][0]
    jump_y = by + vectors[bomb_dir][1]
    print(f"Start: {bx} {by} End: {jump_x} {jump_y}", file=sys.stderr, flush=True)
    bx = jump_x
    by = jump_y

    # the location of the next window Batman should jump to.
    print(f"{jump_x} {jump_y}")
