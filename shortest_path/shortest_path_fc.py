from shortest_path_model import node_db
from shortest_path_model import node_temp
from shortest_path_model import input_model

def search_node_begin(search, list_node_db):
  list_way = []
  for node in list_node_db:
    if node.point_l == search:
        node_temp_model = node_temp(node.point_r, node.value)
        list_way.append(node_temp_model)
    elif node.point_r == search:
        node_temp_model = node_temp(node.point_l, node.value)
        list_way.append(node_temp_model)

  return list_way
    
def search_node_action(list_node_db, list_search, input_param):
    list_possible = []
    for node_temp_model in list_search:
        list_main = []
        init_model = node_temp(input_param.begin_node, 0)
        list_main.append(init_model)

        # if first node to find equal goal then add to list and exit loop
        if node_temp_model.name == input_param.des_node:
            init_model = node_temp(node_temp_model.name, node_temp_model.value)
            list_main.append(init_model)
            list_possible.append(list_main)
            break

        search_node(list_node_db, node_temp_model, input_param, list_main, list_possible, [])
    
    return list_possible

def search_node(list_node_db, node_next, input_param, list_main, list_possible, list_save_point):  
    start = list_main[len(list_main) - 1].name # Index latest of list_main
    goal = node_next.name # Next node to find
    list_searching = search_deep(list_node_db, goal, start)

    if goal == input_param.begin_node or goal == input_param.des_node or isLostWay(goal, list_main):  

        # if finish goal save list to list_possible
        if goal == input_param.des_node:
            save_node(list_main, node_next)
            list_possible.append(list_main)

        return load_another_save(list_node_db, input_param, list_possible, list_save_point)

    save_node(list_main, node_next)
    if len(list_searching) == 0:
        return load_another_save(list_node_db, input_param, list_possible, list_save_point)
    else:
        if len(list_searching) > 1:
            list_another_save = []
            list_another_save.extend(list_searching)
            del list_another_save[0]

            for another_save in list_another_save:
                save_point(list_save_point, list_main, another_save)
            
        node_next = list_searching[0]
        return search_node(list_node_db, node_next, input_param, list_main, list_possible, list_save_point)

def load_another_save(list_node_db, input_param, list_possible, list_save_point):
    if len(list_save_point) == 0: # if list_save_point emtpy exit end loop
        return list_possible
    else: # load another_save from list_save_point
        list_another_save = []
        list_another_save.extend(list_save_point[0]) # load latest save
        del list_save_point[0] # delete when load finish
        node_next = list_another_save[len(list_another_save) - 1]

        list_main = []
        list_main.extend(list_another_save) # load another_save to list_main
        del list_main[len(list_main) - 1] # back 1 step to find next node
        return search_node(list_node_db, node_next, input_param, list_main, list_possible, list_save_point)

def isLostWay(goal, list_main):
    for node_temp in list_main:
        if node_temp.name == goal:
            return True
    
    return False

def save_node(list_main, node_next):
    for hist in list_main:
        if hist.name == node_next.name:
            return

    list_main.append(node_next)

def search_deep(list_node_db, search, back_step):
    list_no = []
    for node in list_node_db:
        if node.point_l == search and (not node.point_r == back_step): 
            search_next = node.point_r
            model = node_temp(search_next, node.value)
            list_no.append(model)
        elif node.point_r == search and (not node.point_l == back_step):
            search_next = node.point_l
            model = node_temp(search_next, node.value)
            list_no.append(model)
        
    return list_no

def save_point(list_save_point, list_main, node_temp_model):
    list_temp = []
    list_temp.extend(list_main)

    if is_duplicate(list_temp, node_temp_model):
        list_temp.append(node_temp_model)
        list_save_point.append(list_temp)

    return list_save_point

def is_duplicate(list_temp, node_temp_model):
    for hist in list_temp:
        if hist.name == node_temp_model.name:
            return False

    return True

def find_shortest_list(list_possible):
    if len(list_possible) == 0:
        return []
    
    list_shortest = []
    check_first_total = True
    total:int = 0
    shortest_cost = 0

    for list_no in list_possible:
        for result in list_no:
          total = total + int(result.value)

        if check_first_total:
            shortest_cost = total
            check_first_total = False
            list_shortest.extend(list_no)
        else:
            if shortest_cost > total:
                shortest_cost = total
                list_shortest = []
                list_shortest.extend(list_no)

        total = 0

    return list_shortest

def print_value(input_param, list_shortest):
    path = ""
    first = True
    total = 0

    for result in list_shortest:
        if first:
            path = result.name + "(" + str(result.value) + ")"
            first = False
        else:
            path = path + " -> " + result.name + "(" + str(result.value) + ")"

        total = total + int(result.value)
    
    print("Path from " + input_param.begin_node + " to " + input_param.des_node + " is " + path + ", and have cost " + str(total) + ".")
    return total
