#no classes for now. this is an experiment with just methods.
from random import randint
from collections import OrderedDict
import copy
import random

def puzzle_dict(puzzle_str):
    global puzzle_master
    puzzle_str_arr = list(puzzle_str)
    puzzle_master = dict(enumerate(puzzle_str_arr))

    puzzle_master = {k:int(v) if v.isdigit() else v for k,v in puzzle_master.items()}


    print "Here is the dictionary"
    print puzzle_master


def row_ref(puzzle_str):
    global puzzle_rows
    #try and get this to be integers here
    puzzle_str = [ int(x) for x in puzzle_str ]
    puzzle_rows = [puzzle_str[x:x+9] for x in range(0, len(puzzle_str),9)]
    puzzle_rows = [list(cell) for cell in puzzle_rows]
    print "Here are the rows"
    print puzzle_rows

def column_ref(puzzle_str):
    global puzzle_columns
    puzzle_str = [ int(x) for x in puzzle_str ]
    puzzle_columns = map(list, zip(*([puzzle_str[x:x+9] for x in range(0, len(puzzle_str),9)])))
    print "here are the colums"
    print puzzle_columns

def box_ref(puzzle_str):
    global puzzle_boxes_final
    puzzle_str = [ int(x) for x in puzzle_str ]
    puzzle_box_rows = [puzzle_str[x:x+3] for x in range(0, len(puzzle_str),3)]
    puzzle_box_rows = [list(cell) for cell in puzzle_box_rows]

    puzzle_boxes = map(list, zip(*([puzzle_box_rows[x:x+3] for x in range(0, len(puzzle_box_rows),3)])))

    # print puzzle_boxes

    temp_flat = []
    for sublist in puzzle_boxes:
      for val in sublist:
        temp_flat.append(val)

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

    temp_flat_2= []

    flattened_list = []

    for x in puzzle_boxes_temp:
      for y in x:
        flattened_list.append(y)

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

    print "here are the boxes"
    print puzzle_boxes_final

#NEXT STEP: make reference table so that you know the row, column, and box for a given cell

def cell_reference(dict, row, column, box):
  global live_puzzle_dict
  live_puzzle_dict = {}

  for key, value in puzzle_master.iteritems():
    live_puzzle_dict[key] = []
    # print "start rows"
    if key in range(0,9):
        cell_row = row[0]
        live_puzzle_dict[key].append(row[0])
    elif key in range(9,18):
        cell_row = row[1]
        live_puzzle_dict[key].append(row[1])
    elif key in range(18,27):
        cell_row = row[2]
        live_puzzle_dict[key].append(row[2])
    elif key in range(27,36):
        cell_row = row[3]
        live_puzzle_dict[key].append(row[3])
    elif key in range(36,45):
        cell_row = row[4]
        live_puzzle_dict[key].append(row[4])
    elif key in range(45,54):
        cell_row = row[5]
        live_puzzle_dict[key].append(row[5])
    elif key in range(54,63):
        cell_row = row[6]
        live_puzzle_dict[key].append(row[6])
    elif key in range(63,72):
        cell_row = row[7]
        live_puzzle_dict[key].append(row[7])
    elif key in range(72,82):
        cell_row = row[8]
        live_puzzle_dict[key].append(row[8])
    else:
        print "error. row is out of range"

    #columns
    if key in range(0,80,9):
        cell_column = puzzle_columns[0]
        live_puzzle_dict[key].append(column[0])
    elif key in range(1,80,9):
        cell_column = puzzle_columns[1]
        live_puzzle_dict[key].append(column[1])
    elif key in range(2,80,9):
        cell_column = puzzle_columns[2]
        live_puzzle_dict[key].append(column[2])
    elif key in range(3,80,9):
        cell_column = puzzle_columns[3]
        live_puzzle_dict[key].append(column[3])
    elif key in range(4,80,9):
        cell_column = puzzle_columns[4]
        live_puzzle_dict[key].append(column[4])
    elif key in range(5,80,9):
        cell_column = puzzle_columns[5]
        live_puzzle_dict[key].append(column[5])
    elif key in range(6,80,9):
        cell_column = puzzle_columns[6]
        live_puzzle_dict[key].append(column[6])
    elif key in range(7,80,9):
        cell_column = puzzle_columns[7]
        live_puzzle_dict[key].append(column[7])
    elif key in range(8,81,9):
        cell_column = puzzle_columns[8]
        live_puzzle_dict[key].append(column[8])
    else:
        print "error. column out of range"

    #boxes
    if key in range(0,3) or key in range(9,12) or key in range (18,21):
        box = puzzle_boxes_final[0]
        live_puzzle_dict[key].append(puzzle_boxes_final[0])
    elif key in range(3,6) or key in range(12,15) or key in range (21,24):
        box = puzzle_boxes_final[1]
        live_puzzle_dict[key].append(puzzle_boxes_final[1])
    elif key in range(6,9) or key in range(15,18) or key in range (24,27):
        box = puzzle_boxes_final[2]
        live_puzzle_dict[key].append(puzzle_boxes_final[2])
    elif key in range(27,30) or key in range(36,39) or key in range (45,48):
        box = puzzle_boxes_final[3]
        live_puzzle_dict[key].append(puzzle_boxes_final[3])
    elif key in range(30,33) or key in range(39,42) or key in range (48,51):
        box = puzzle_boxes_final[4]
        live_puzzle_dict[key].append(puzzle_boxes_final[4])
    elif key in range(33,36) or key in range(42,45) or key in range (51,53):
        box = puzzle_boxes_final[5]
        live_puzzle_dict[key].append(puzzle_boxes_final[5])
    elif key in range(54,57) or key in range(63,66) or key in range (72,75):
        box = puzzle_boxes_final[6]
        live_puzzle_dict[key].append(puzzle_boxes_final[6])
    elif key in range(57,60) or key in range(66,69) or key in range (75,78):
        box = puzzle_boxes_final[7]
        live_puzzle_dict[key].append(puzzle_boxes_final[7])
    elif key in range(60,63) or key in range(69,71) or key in range (78,81):
        box = puzzle_boxes_final[8]
        live_puzzle_dict[key].append(puzzle_boxes_final[8])
    else:
        "error. box out of range"
    # finish this

  print live_puzzle_dict
  print "next is solution collector"

def solution_collector(live_puzzle_dict):
  global possible_solutions
  possible_solutions = copy.deepcopy(live_puzzle_dict)
  possible_nums = [1,2,3,4,5,6,7,8,9]
  possible_solutions_subset = []

  for key,value in possible_solutions.iteritems():
    for area in value:
        for num,item in enumerate(area):
          if item != 0:
            item = item
          else:
            if item not in possible_nums:
              # this is if num == 0
              possible_solutions_subset = filter(lambda x: x not in area, possible_nums)
              value.append(possible_solutions_subset)



  for key,value in possible_solutions.iteritems():
    del value[:3]

  for key,value in possible_solutions.iteritems():
    unique_solutions = []
    for elem in value:
      if elem not in unique_solutions:
        unique_solutions.append(elem)
    del value[:]
    for elem in unique_solutions:
      value.append(elem)

  # print live_puzzle_dict
  print possible_solutions



#at this point, we have two dictionaries.
#one that references cells (live_puzzle_dict)
#one that references possible entries in that cell (possible solution)

def solutions_filter(live_puzzle_dict,possible_solutions):
    for key,value in possible_solutions.iteritems():
      if len(value) == 3:
        filtered_list = [x for x in value[0] if x in value[1] and x in value[2]]
        # print filtered_list
        del value[:]
        value.append(filtered_list)

      if len(value) == 2:
          filtered_list = [x for x in value[0] if x in value[1]]
          # print filtered_list
          del value[:]
          value.append(filtered_list)

    print possible_solutions

    # print live_puzzle_dict

    for key,value in puzzle_master.iteritems():
      if value != 0:
        del possible_solutions[key]

    # print possible_solutions

  # print possible_solutions[key][value]
      #if the value is zero, i want you to pick a number from the corresponding index in possible_solutions and put it in the puzzle. keep doing this until puzzle is solved

def solver(puzzle_master,live_puzzle_dict,possible_solutions):
  print puzzle_master
  for key,value in puzzle_master.iteritems():
    if value == 0:
      for key,value in possible_solutions.iteritems():
        i = 0
        while i <= key:
          # the following iteration is broken
          insertions = [x for x in key[i] if x not in live_puzzle_dict[0][0] and x not in live_puzzle_dict[0][1] and x not in live_puzzle_dict[0][2]]
          i+=1
          puzzle_master[key] = insertions

  print puzzle_master
  # print live_puzzle_dict
  # print live_puzzle_dict[key][0][0]




#for each possible solution for a cell,
#if it can go in a row, column, and box, that's the correct solution


practice_puzzle = "105802000090076405200400819019007306762083090000061050007600030430020501600308900"
puzzle_dict(practice_puzzle)
row_ref(practice_puzzle)
column_ref(practice_puzzle)
box_ref(practice_puzzle)
cell_reference(puzzle_master, puzzle_rows, puzzle_columns, puzzle_boxes_final)
solution_collector(live_puzzle_dict)
solutions_filter(live_puzzle_dict, possible_solutions)
solver(puzzle_master,live_puzzle_dict,possible_solutions)
