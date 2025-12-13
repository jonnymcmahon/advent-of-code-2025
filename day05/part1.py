from workshop import read_input


def main():

    input = read_input(5)

    ranges, ingredients = process_input(input)

    ranges = create_range_objects(ranges)

    fresh_ids = set()

    # loop through all ingredients
    for id in ingredients:

        # check each range
        for _range in ranges:

            # if in range, add to fresh
            if int(id) in _range:

                fresh_ids.add(int(id))

    print(len(fresh_ids))


def process_input(input):

    # split the two inputs
    ranges, ingredients = input.split("\n\n")

    # return arrays
    return ranges.split("\n"), ingredients.split("\n")


def create_range_objects(ranges):

    # loop through and create range objects for each range
    for i, _range in enumerate(ranges):

        start, end = _range.split("-")

        ranges[i] = range(int(start), int(end) + 1)

    return ranges


if __name__ == "__main__":
    main()
