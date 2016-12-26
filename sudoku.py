#no classes for now. this is an experiment with just methods.

def puzzle_dict(puzzle_str):
    puzzle_str_arr = list(puzzle_str)
    puzzle_master = dict(enumerate(puzzle_str_arr))
    print puzzle_master

def row_ref(puzzle_str):
    puzzle_rows = [puzzle_str[x:x+9] for x in range(0, len(puzzle_str),9)]
    puzzle_rows = [list(cell) for cell in puzzle_rows]
    print(puzzle_rows)

def column_ref(puzzle_str):
    puzzle_columns = map(list, zip(*([puzzle_str[x:x+9] for x in range(0, len(puzzle_str),9)])))
    print puzzle_columns

def box_ref(puzzle_str):
    puzzle_box_rows = [puzzle_str[x:x+3] for x in range(0, len(puzzle_str),3)]
    puzzle_box_rows = [list(cell) for cell in puzzle_box_rows]
    # print puzzle_box_rows

    puzzle_boxes = []
    i = 27

    while i > 0:
        for box_row in puzzle_box_rows:
            puzzle_boxes.append(puzzle_box_rows[i-1])
            puzzle_boxes.append(puzzle_box_rows[i-4])
            puzzle_boxes.append(puzzle_box_rows[i-7])
            i = i-1

    # puzzle_boxes.reverse()
    print puzzle_boxes


practice_puzzle = "1-58-2----9--764-52--4--819-19--73-6762-83-9-----61-5---76---3-43--2-5-16--3-89--"
# puzzle_dict(practice_puzzle)
# row_ref(practice_puzzle)
# column_ref(practice_puzzle)
box_ref(practice_puzzle)
