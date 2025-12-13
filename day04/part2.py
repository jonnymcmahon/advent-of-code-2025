from workshop import read_input


def main():

    rows = read_input(4, False).split("\n")

    # convert rows from strings to array of strings
    for x, row in enumerate(rows):

        rows[x] = [i for i in row]

    # get grid max width and height indexes
    max_width = len(rows[0]) - 1
    max_height = len(rows) - 1

    has_changed = True
    total_removed = 0

    # loop until it no more can be removed
    while has_changed is True:

        rows, removed, has_changed = mark_for_removal(rows, max_width, max_height)

        total_removed += removed

    print(total_removed)


def mark_for_removal(rows, max_width, max_height):

    removed_rolls = []
    removed = 0

    # loop rows
    for x, row in enumerate(rows):

        # loop cols in row
        for y, col in enumerate(row):

            # if there is no roll of paper - skip
            if col == ".":
                continue

            adjacent = 0

            # check all directions
            adjacent += has_paper_roll(x, y, "up-left", max_width, max_height, rows)
            adjacent += has_paper_roll(x, y, "up", max_width, max_height, rows)
            adjacent += has_paper_roll(x, y, "up-right", max_width, max_height, rows)
            adjacent += has_paper_roll(x, y, "left", max_width, max_height, rows)
            adjacent += has_paper_roll(x, y, "right", max_width, max_height, rows)
            adjacent += has_paper_roll(x, y, "down-left", max_width, max_height, rows)
            adjacent += has_paper_roll(x, y, "down", max_width, max_height, rows)
            adjacent += has_paper_roll(x, y, "down-right", max_width, max_height, rows)

            if adjacent < 4:
                removed_rolls.append([int(x), int(y)])
                removed += 1

    # remove rolls from original grid
    for coords in removed_rolls:

        x = coords[0]
        y = coords[1]

        rows[x][y] = "."

    # return a bool for if the grid has changed this run so we know when to stop
    if removed == 0:
        has_changed = False
    else:
        has_changed = True

    return rows, removed, has_changed


def has_paper_roll(x, y, direction, max_width, max_height, rows):

    # match statement for each direction
    match direction:
        case "up":
            y = y + 1

        case "down":
            y = y - 1

        case "left":
            x = x - 1

        case "right":
            x = x + 1

        case "up-left":
            y = y + 1
            x = x - 1

        case "up-right":
            y = y + 1
            x = x + 1

        case "down-left":
            y = y - 1
            x = x - 1

        case "down-right":
            y = y - 1
            x = x + 1

    # if outside bounds - return 0 for no paper roll found
    if y < 0 or y > max_width or x < 0 or x > max_height:
        return 0

    # if roll found, return 1
    if rows[x][y] == "@":
        return 1
    else:
        return 0


if __name__ == "__main__":
    main()
