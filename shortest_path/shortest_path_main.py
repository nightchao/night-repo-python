from shortest_path_model import node_db
from shortest_path_model import node_temp
from shortest_path_model import input_model
from shortest_path_fc import search_node_begin
from shortest_path_fc import search_node_action
from shortest_path_fc import find_shortest_list
from shortest_path_fc import print_value

# read file .csv
file_csv = open('graph.csv', 'r') 
lines = file_csv.readlines()
list_node_db = []
for line in lines:
    arr_data = line.split(',')
    node = node_db(arr_data[0].strip(), arr_data[1].strip(), arr_data[2].strip())
    list_node_db.append(node)

file_csv.close()

# if data from file csv empty exit program
if len(list_node_db) == 0:
    print("Invalid file graph")
    exit()

start_input = input("What is start node?: ")
goal_input = input("What is goal node?: ")

if ((not start_input.isalpha()) or (not goal_input.isalpha())):
    print("Input is empty")
    exit()

start_input = start_input.upper() # force to Upper
goal_input = goal_input.upper() # force to Upper
input_param = input_model(start_input, goal_input)

list_search = search_node_begin(input_param.begin_node, list_node_db)
if len(list_search) == 0:
    print("Node: " + input_param.begin_node + " cannot go to node: " + input_param.des_node)
    exit()

list_possible = search_node_action(list_node_db, list_search, input_param)
list_shortest = find_shortest_list(list_possible)
print_value(input_param, list_shortest)