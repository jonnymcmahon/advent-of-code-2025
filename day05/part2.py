from workshop import read_input
from collections import deque


def main():

    input = read_input(5)

    input_ranges = process_input(input)

    raw_ranges = read_and_sort_ranges(input_ranges)

    # create two queues for raw ranges and merged ranges
    q_ranges = deque(raw_ranges)
    q_merged = deque()

    while len(q_ranges) > 1:

        # get two ranges from queue
        a_min, a_max = q_ranges.popleft()
        b_min, b_max = q_ranges.popleft()

        # test for overlap between ranges
        if b_min > a_max:

            # no overlap!

            # add first range to merged queue
            q_merged.append((a_min, a_max))

            # add second range back to raw queue
            q_ranges.appendleft((b_min, b_max))
        else:

            # overlap!!

            # find max end of two ranges
            max_end = max(a_max, b_max)

            # merge ranges and add to raw queue
            q_ranges.appendleft((a_min, max_end))

    # add last from raw queue to merged queue
    q_merged.append(q_ranges.popleft())

    # count all ids in ranges
    total_ids = 0

    while q_merged:
        _min, _max = q_merged.popleft()

        # add IDs in range to total
        total_ids += _max - _min + 1

    print(total_ids)


def process_input(input):

    # split the two inputs
    ranges, _ = input.split("\n\n")

    # return arrays
    return ranges.split("\n")


def read_and_sort_ranges(ranges):

    raw_ranges = []

    # read in all ranges as tuples
    for _range in ranges:

        start, end = _range.split("-")

        raw_ranges.append((int(start), int(end)))

    # sort them (sorts by first value in tuple)
    raw_ranges.sort()

    return raw_ranges


if __name__ == "__main__":
    main()
