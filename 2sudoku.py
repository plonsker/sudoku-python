#no classes for now. this is an experiment with just methods.
from random import randint
from collections import OrderedDict
import copy
import random


#refactor using a list instead of a dictionary

def puzzle_parser(puzzle_str):
    # print list(puzzle_str)
    global orig_board_list
    orig_board_list = map(int, list(puzzle_str))
    print orig_board_list
    return orig_board_list

def row_ref(orig_board_list):
    orig_board_rows = [orig_board_list[i:i+9] for i in range(0, len(orig_board_list), 9)]
    print orig_board_rows
    return orig_board_rows


def column_ref(orig_board_list):
    orig_board_columns = map(list, zip(*([orig_board_list[x:x+9] for x in range(0, len(orig_board_list),9)])))
    print orig_board_columns
    return orig_board_columns

def box_ref(orig_board_list):
    # orig_board_boxes = [ int(x) for x in puzzle_str ]
    orig_board_boxes_temp = [orig_board_list[x:x+3] for x in range(0, len(orig_board_list),3)]
    orig_board_boxes_temp = [list(cell) for cell in orig_board_boxes_temp]

    print orig_board_boxes_temp

    orig_board_boxes = []

    #perhaps make this a while loop
    orig_board_boxes.append(orig_board_boxes_temp[0] + orig_board_boxes_temp[3] + orig_board_boxes_temp[6])
    orig_board_boxes.append(orig_board_boxes_temp[1] + orig_board_boxes_temp[4] + orig_board_boxes_temp[7])
    orig_board_boxes.append(orig_board_boxes_temp[2] + orig_board_boxes_temp[5] + orig_board_boxes_temp[8])
    orig_board_boxes.append(orig_board_boxes_temp[9] + orig_board_boxes_temp[12] + orig_board_boxes_temp[15])
    orig_board_boxes.append(orig_board_boxes_temp[10] + orig_board_boxes_temp[13] + orig_board_boxes_temp[16])
    orig_board_boxes.append(orig_board_boxes_temp[11] + orig_board_boxes_temp[14] + orig_board_boxes_temp[17])
    orig_board_boxes.append(orig_board_boxes_temp[18] + orig_board_boxes_temp[21] + orig_board_boxes_temp[24])
    orig_board_boxes.append(orig_board_boxes_temp[19] + orig_board_boxes_temp[22] + orig_board_boxes_temp[25])
    orig_board_boxes.append(orig_board_boxes_temp[20] + orig_board_boxes_temp[23] + orig_board_boxes_temp[26])

    print "here are the boxes"
    print orig_board_boxes
    return orig_board_boxes

#
def cell_row(cell):
    cell / 9

def cell_column(cell):
    cell % 9

def cell_box(cell):
    box_row = (cell / 9) / 3
    box_column = (cell % 9) / 3
    (box_row + 3) + box_column

def complete_area_checker(area):
    if set(map(len, area)) == set([9]):
    #maybe detect if there are any zeros
        return true

def complete_board_checker(board):
    for sublist in row_ref(board):
        if 0 not in sublist:
            return True

    for sublist in column_ref(board):
        if 0 not in sublist:
            return True

    for sublist in box_ref(board):
        if 0 not in sublist:
            return True


def solution_collector(orig_board_list):
  global possible_solutions
  print "here is that original"
  print orig_board_list
  possible_solutions = copy.deepcopy(orig_board_list)
  possible_nums = [1,2,3,4,5,6,7,8,9]
  possible_solutions_subset = []

  print "who"
  print possible_solutions
  print "what"

  for cell, num in enumerate(possible_solutions):
    if num != 0:
        print num
        # cell = cell
    #this breaks it
    else:
        print "yolo"
        # for possible_entry in possible_nums:
        #     if possible_entry not in row_ref(board):
        #       possible_solutions_subset.append(possible_entry)
        #       num = possible_solutions_subset

  print "here are some possible solutions"
  print possible_solutions
  #
  # for key,value in possible_solutions.iteritems():
  #   del value[:3]
  #
  # for key,value in possible_solutions.iteritems():
  #   unique_solutions = []
  #   for elem in value:
  #     if elem not in unique_solutions:
  #       unique_solutions.append(elem)
  #   del value[:]
  #   for elem in unique_solutions:
  #     value.append(elem)
  #
  # # print "possible solutions"
  # # print possible_solutions
  # for key,value in possible_solutions.iteritems():
  #     if len(value) == 3:
  #         filtered_list = [x for x in value[0] if x in value[1] and x in value[2]]
  #         del value[:]
  #         value.append(filtered_list)
  #
  # if len(value) == 2:
  #     filtered_list = [x for x in value[0] if x in value[1]]
  #     del value[:]
  #     value.append(filtered_list)
  #
  # for key,value in puzzle_master.iteritems():
  #     if value != 0:
  #         del possible_solutions[key]

# print puzzle_master
  # print "possible solutions"
  # print possible_solutions
  # print "puzzle_master"
  # print puzzle_master

# def solver1(puzzle_master,live_puzzle_dict,possible_solutions):
#   global puzzle_str_ref_end
#   i = 0
#   # print live_puzzle_dict
#   going = True
#   already_seen_puzzles = []
#
#   while going:
#       new_puzzle_master = copy.deepcopy(puzzle_master)
#       for key,value in new_puzzle_master.iteritems():
#           if new_puzzle_master[key] == 0:
#               for key,value in possible_solutions.iteritems():
#                   insertions = [x for x in possible_solutions[key] if x not in live_puzzle_dict[key]]
#                   new_puzzle_master[key] = [item for sublist in insertions for item in sublist]
#                   if len(new_puzzle_master[key]) == 1:
#                       new_puzzle_master[key] = map(str, new_puzzle_master[key])
#                       new_puzzle_master[key] = ''.join(new_puzzle_master[key])
#                       new_puzzle_master[key] = int(new_puzzle_master[key])
#
#       #once this logic is fixed, the solver should run much more efficiently
#       for key,value in new_puzzle_master.iteritems():
#         if value and isinstance(value, list) and value != []:
#             # print value
#             # new_puzzle_master[key] = value[randint(0,len(value)-1)]
#             new_puzzle_master[key] = random.choice(value)
#
#
#       puzzle_str_ref = ''.join(map(str, (new_puzzle_master.values())))
#
#       new_live_puzzle_dict = cell_reference(new_puzzle_master, row_ref(puzzle_str_ref), column_ref(puzzle_str_ref), box_ref(puzzle_str_ref))
#
#     #   print new_live_puzzle_dict
#
#     #   for key,value in new_live_puzzle_dict.iteritems():
#     #       print len(set(value[0]))
#     #       print len(set(value[1]))
#     #       print len(set(value[-1]))
#
#       if puzzle_str_ref not in already_seen_puzzles:
#               already_seen_puzzles.append(puzzle_str_ref)
#               row_set = map(set, row_ref(puzzle_str_ref))
#               column_set = map(set, column_ref(puzzle_str_ref))
#               box_set = map(set, column_ref(puzzle_str_ref))
#
#               print puzzle_str_ref
#               print "--------------------------"
#               print "%s total calculations" % i
#               print "--------------------------"
#
#
#
#
#             #   if len(set(new_live_puzzle_dict[key][len(value)-3])) == 9 and len(set(new_live_puzzle_dict[key][len(value)-2])) == 9 and len(set(new_live_puzzle_dict[key][len(value)-1])) == 9:
#               if set(map(len, row_set)) == set([9]) and set(map(len, column_set)) == set([9]) and set(map(len, box_set)) == set([9]):
#                       print "======================================="
#                       print "Solution:"
#                       print puzzle_str_ref
#                       print "======================================="
#                     #   print cell_reference(new_puzzle_master, row_ref(puzzle_str_ref), column_ref(puzzle_str_ref), box_ref(puzzle_str_ref))
#                       going = False
#                       break
#               i+=1


#puzzle one:
practice_puzzle = "105802000090076405200400819019007306762083090000061050007600030430020501600308900"

#nearly solved puzzle:
# practice_puzzle = "246857913180000000000001486418329507637480000950170048764532891321968754895710000"

#puzzle two:
# practice_puzzle = "005030081902850060600004050007402830349760005008300490150087002090000600026049503"

#easy kids puzzle
# practice_puzzle = "639000024002904067070268090005603780701025400360040209510080940200419005043700610"

# practice_puzzle = "000000000089410000006700193200000700340600010000900005000020050650040020730100000"
# practice_puzzle = "173269584589413672426758193291584736345672819867931245914826357658347921732195468"

puzzle_parser(practice_puzzle)
# row_ref_index(11)
# column_ref_index(23)
row_ref(orig_board_list)
column_ref(orig_board_list)
box_ref(orig_board_list)
cell_row(80)
cell_column(80)
cell_box(80)
solution_collector(orig_board_list)
