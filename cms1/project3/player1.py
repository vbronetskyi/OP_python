#_____________________________________________
# ruby ./filler_vm -f ./map01 -p1 "python ./player1.py" -p2 "python ./player2.py" | python visualizer.py
#_____________________________________________
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    This is an example of a bot for the 3rd project.
    ...a pretty bad bot to be honest -_-
"""

from logging import DEBUG, debug, getLogger
from math import sqrt

# We use the debugger to print messages to stderr
# You cannot use print as you usually do, the vm would intercept it
# You can hovever do the following:
#
# import sys
# print("HEHEY", file=sys.stderr)

getLogger().setLevel(DEBUG)


def parse_field_info():
    """
    Parse the info about the field.

    However, the function doesn't do anything with it. Since the height of the field is
    hard-coded later, this bot won't work with maps of different height.

    The input may look like this:

    Plateau 15 17:
    """
    line = input().split(" ")
    debug(f"Description of the field: {line}")
    return (line[1], line[2].replace(':', ''))


def parse_field(rows):
    """
    Parse the field.

    First of all, this function is also responsible for determining the next
    move. Actually, this function should rather only parse the field, and return
    it to another function, where the logic for choosing the move will be.

    Also, the algorithm for choosing the right move is wrong. This function
    finds the first position of _our_ character, and outputs it. However, it
    doesn't guarantee that the figure will be connected to only one cell of our
    territory. It can not be connected at all (for example, when the figure has
    empty cells), or it can be connected with multiple cells of our territory.
    That's definitely what you should address.

    Also, it might be useful to distinguish between lowecase (the most recent piece)
    and uppercase letters to determine where the enemy is moving etc.

    The input may look like this:

        01234567890123456
    000 .................
    001 .................
    002 .................
    003 .................
    004 .................
    005 .................
    006 .................
    007 ..O..............
    008 ..OOO............
    009 .................
    010 .................
    011 .................
    012 ..............X..
    013 .................
    014 .................

    :param player int: Represents whether we're the first or second player
    """
    field = []
    input()
    for _ in range(int(rows)):
        line = input().strip()[4:]
        field.append([i for i in line])
        debug(f"Field: {line}")

    return field


def parse_figure():
    """
    Parse the figure.

    The function parses the height of the figure (maybe the width would be
    useful as well), and then reads it.
    It would be nice to save it and return for further usage.

    The input may look like this:

    Piece 2 2:
    **
    ..
    """
    sign = []
    line = input()
    debug(f"Piece: {line}")
    height = int(line.split()[1])
    for _ in range(height):
        line = input().strip()
        sign.append([i for i in line])
        debug(f"Piece: {line}")
    return sign

def intersections(pole, coordinates, player, move_to):
    """
    The function gives priority to a move if it envelops
    the opponent and limits his further moves
    """
    priority, way = 0, None
    # for index in range(-1, 1):
    #     for index1 in range(-1, 1):
    #         if coordinates[0] + index < len(pole)\
    #             and coordinates[1] + index1 < len(pole[0]):
    #             if pole[coordinates[0] + index][coordinates[1]\
    #                 + index1] not in (player, "."):
    #                 priority += 1000
    # if not priority:
    #     if coordinates:
    #         way = sqrt(pow(move_to[0]-coordinates[0], 2)+pow(move_to[1]-coordinates[1], 2))
    #         priority += 999 - way*10

    return priority

def check(coordianates, pole, sign, mark, move_to):
    """
    Checks the move for correctness, and with the
    help of additional functions calculates the
    priority of the move
    """
    priority = 0
    coordianates_y = coordianates[0]
    coordianates_x = coordianates[1]
    if  coordianates_y < 0 or coordianates_x < 0:
        return "error", 0
    flag = False
    for i1, v1 in enumerate(sign):
        for i3, v3  in enumerate(v1):
            try:
                if sign[i1][i3] != ".":
                    if pole[coordianates_y + i1][coordianates_x + i3].upper() == mark:
                        if flag:
                            return "error", 0
                        flag = True
                    if pole[coordianates_y + i1][coordianates_x + i3].upper() not in (mark, "."):
                        return "error", 0
                    priority += intersections(pole,(coordianates_y + i1, coordianates_x + i3), mark, move_to)
            except (IndexError, TypeError):
                if v3 != ".":
                    return "error", 0
    return (coordianates, priority)


def move_func(pole, sign, mark, move_to):
    """
    Checks all possible moves, and then
    returns the most optimal of them
    """
    all_moves = []
    for i1, v1 in enumerate(sign):
        for i3, v3  in enumerate(v1):
            if v3 != ".":
                for i5, v5 in enumerate(pole):
                    for i7, v7 in enumerate(v5):
                        if v7 == mark:
                            move1, points = check((i5 - i1, i7 - i3),pole, sign, mark, move_to)
                            if move1 != "error":
                                all_moves.append((move1, points))

    debug(all_moves)
    if all_moves == []:
        return (-1, -1)
    best_move = all_moves[0]
    for move2, points_for_move in all_moves:
        if points_for_move > best_move[1]:
            best_move = (move2, points_for_move)
    return best_move[0]

def cord_to_move(pole, mark):
    """Find first cordinate of your player"""
    for y_cord in range(len(pole)):
        for x_cord in range(len(pole[y_cord])):
            if pole[y_cord][x_cord] not in (mark, '.'):
                return (x_cord, y_cord)



def step(player: int):
    """
    Perform one step of the game.

    :param player int: Represents whether we're the first or second player
    """
    if player == 1:
        mark = "O"
    else:
        mark = "X"
    rows, cols= parse_field_info()
    pole = parse_field(rows)
    debug(f"Cols__________________________________\n: {cols}")
    move_to = cord_to_move(pole, mark)
    debug(f"Cord__________________________________\n: {move_to}")
    sign = parse_figure()
    solut = move_func(pole, sign, mark, move_to)
    return solut


def play(player: int):
    """
    Main game loop.

    :param player int: Represents whether we're the first or second player
    """
    while True:
        move = step(player)
        print(*move)


def parse_info_about_player():
    """
    This function parses the info about the player

    It can look like this:

    $$$ exec p2 : [./player1.py]
    """
    i = input()
    debug(f"Info about the player: {i}")
    return 1 if "p1 :" in i else 2


def main():
    player = parse_info_about_player()
    try:
        play(player)
    except EOFError:
        debug("Cannot get input. Seems that we've lost ):")


if __name__ == "__main__":
    main()
