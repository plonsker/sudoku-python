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

    puzzle_boxes_temp = []

    puzzle_boxes_temp.append(temp_flat[0:3])
    puzzle_boxes_temp.append(temp_flat[9:12])
    puzzle_boxes_temp.append(temp_flat[18:21])
    puzzle_boxes_temp.append(temp_flat[3:6])
    puzzle_boxes_temp.append(temp_flat[12:15])
    puzzle_boxes_temp.append(temp_flat[21:24])
    puzzle_boxes_temp.append(temp_flat[6:9])
    puzzle_boxes_temp.append(temp_flat[15:18])
    puzzle_boxes_temp.append(temp_flat[24:27])

    print puzzle_boxes_temp

    temp_flat_2= []

    flattened_list = []

    #flatten the lis
    for x in puzzle_boxes_temp:
      for y in x:
        flattened_list.append(y)

    print "yo 2"

    print flattened_list

    print "yo 3"

    puzzle_boxes_final = []

    box_0 = flattened_list[0] + flattened_list[1] + flattened_list[2]
    box_1 = flattened_list[3] + flattened_list[4] + flattened_list[5]
    box_2 = flattened_list[6] + flattened_list[7] + flattened_list[8]
    box_3 = flattened_list[9] + flattened_list[10] + flattened_list[11]
    box_4 = flattened_list[12] + flattened_list[13] + flattened_list[14]
    box_5 = flattened_list[15] + flattened_list[16] + flattened_list[17]
    box_6 = flattened_list[18] + flattened_list[19] + flattened_list[20]
    box_7 = flattened_list[21] + flattened_list[22] + flattened_list[23]
    box_8 = flattened_list[24] + flattened_list[25] + flattened_list[26]

    puzzle_boxes_final.append(box_0)
    puzzle_boxes_final.append(box_1)
    puzzle_boxes_final.append(box_2)
    puzzle_boxes_final.append(box_3)
    puzzle_boxes_final.append(box_4)
    puzzle_boxes_final.append(box_5)
    puzzle_boxes_final.append(box_6)
    puzzle_boxes_final.append(box_7)
    puzzle_boxes_final.append(box_8)

    print puzzle_boxes_final




practice_puzzle = "1-58-2----9--764-52--4--819-19--73-6762-83-9-----61-5---76---3-43--2-5-16--3-89--"
# puzzle_dict(practice_puzzle)
# row_ref(practice_puzzle)
# column_ref(practice_puzzle)
box_ref(practice_puzzle)
