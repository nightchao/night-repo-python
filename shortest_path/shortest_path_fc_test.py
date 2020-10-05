import unittest

from shortest_path_model import node_db
from shortest_path_model import node_temp
from shortest_path_model import input_model
from shortest_path_fc import search_node_begin
from shortest_path_fc import search_node_action
from shortest_path_fc import find_shortest_list
from shortest_path_fc import print_value

file_csv = open('graph.csv', 'r') 
lines = file_csv.readlines()
list_node_db = []
for line in lines:
    arr_data = line.split(',')
    node = node_db(arr_data[0].strip(), arr_data[1].strip(), arr_data[2].strip())
    list_node_db.append(node)

file_csv.close()

class find_shortest_path_test(unittest.TestCase):

    def test_search_begin(self):
        list_search = search_node_begin('A', list_node_db)
        methodOutput = []
        for result in list_search:
            methodOutput.append(result.name)
        
        expectedOutput = ['B', 'D', 'E']
        self.assertSequenceEqual(expectedOutput, methodOutput)
    
    def find_AB(self):
        input_param = input_model('A', 'B')
        list_search = search_node_begin(input_param.begin_node, list_node_db)
        
        list_possible = search_node_action(list_node_db, list_search, input_param)
        self.assertEqual(1, len(list_possible))
        list_shortest = find_shortest_list(list_possible)
        cost = print_value(input_param, list_shortest)
        self.assertEqual(5, cost)
    
    def find_BA(self):
        input_param = input_model('B', 'A')
        list_search = search_node_begin(input_param.begin_node, list_node_db)
        
        list_possible = search_node_action(list_node_db, list_search, input_param)
        self.assertEqual(1, len(list_possible))
        list_shortest = find_shortest_list(list_possible)
        cost = print_value(input_param, list_shortest)
        self.assertEqual(5, cost)
    
    def find_CF(self):
        input_param = input_model('C', 'F')
        list_search = search_node_begin(input_param.begin_node, list_node_db)
        
        list_possible = search_node_action(list_node_db, list_search, input_param)
        self.assertEqual(1, len(list_possible))
        list_shortest = find_shortest_list(list_possible)
        cost = print_value(input_param, list_shortest)
        self.assertEqual(10, cost)
    
    def find_FG(self):
        input_param = input_model('F', 'G')
        list_search = search_node_begin(input_param.begin_node, list_node_db)
        
        list_possible = search_node_action(list_node_db, list_search, input_param)
        self.assertEqual(1, len(list_possible))
        list_shortest = find_shortest_list(list_possible)
        cost = print_value(input_param, list_shortest)
        self.assertEqual(8, cost)
    
    def find_FC(self):
        input_param = input_model('F', 'C')
        list_search = search_node_begin(input_param.begin_node, list_node_db)
        
        list_possible = search_node_action(list_node_db, list_search, input_param)
        self.assertEqual(1, len(list_possible))
        list_shortest = find_shortest_list(list_possible)
        cost = print_value(input_param, list_shortest)
        self.assertEqual(10, cost)
    
    def find_FJ(self):
        input_param = input_model('F', 'J')
        list_search = search_node_begin(input_param.begin_node, list_node_db)
        
        list_possible = search_node_action(list_node_db, list_search, input_param)
        self.assertEqual(1, len(list_possible))
        list_shortest = find_shortest_list(list_possible)
        cost = print_value(input_param, list_shortest)
        self.assertEqual(18, cost)

    def find_FI(self):
        input_param = input_model('F', 'I')
        list_search = search_node_begin(input_param.begin_node, list_node_db)
        
        list_possible = search_node_action(list_node_db, list_search, input_param)
        self.assertEqual(1, len(list_possible))
        list_shortest = find_shortest_list(list_possible)
        cost = print_value(input_param, list_shortest)
        self.assertEqual(0, cost)


if __name__ == '__main__':
    unittest.main()
