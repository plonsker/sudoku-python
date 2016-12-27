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

    puzzle_boxes = map(list, zip(*([puzzle_box_rows[x:x+3] for x in range(0, len(puzzle_box_rows),3)])))

    # print puzzle_boxes

    temp_flat = []
    for sublist in puzzle_boxes:
      for val in sublist:
        temp_flat.append(val)

    print temp_flat

    print "yo"

    puzzle_boxes_final = []

    puzzle_boxes_final.append(temp_flat[0:3])
    puzzle_boxes_final.append(temp_flat[9:12])
    puzzle_boxes_final.append(temp_flat[18:21])
    puzzle_boxes_final.append(temp_flat[3:6])
    puzzle_boxes_final.append(temp_flat[12:15])
    puzzle_boxes_final.append(temp_flat[21:24])
    puzzle_boxes_final.append(temp_flat[6:9])
    puzzle_boxes_final.append(temp_flat[15:18])
    puzzle_boxes_final.append(temp_flat[24:27])

    print puzzle_boxes_final





practice_puzzle = "1-58-2----9--764-52--4--819-19--73-6762-83-9-----61-5---76---3-43--2-5-16--3-89--"
# puzzle_dict(practice_puzzle)
# row_ref(practice_puzzle)
# column_ref(practice_puzzle)
box_ref(practice_puzzle)
