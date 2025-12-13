from workshop import read_input


def main():

    rows = read_input(4).split("\n")

    # get grid max width and height indexes
    max_width = len(rows[0]) - 1
    max_height = len(rows) - 1

    accessible_rolls = 0

    for x, row in enumerate(rows):

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
                accessible_rolls += 1

    print(accessible_rolls)


def has_paper_roll(x, y, direction, max_width, max_height, rows):

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

    if y < 0 or y > max_width or x < 0 or x > max_height:
        return 0

    if rows[x][y] == "@":
        return 1
    else:
        return 0


if __name__ == "__main__":
    main()
