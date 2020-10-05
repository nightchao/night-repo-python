class node_db:
  def __init__(self, point_l, point_r, value):
    self.point_l = point_l
    self.point_r = point_r
    self.value = value

class node_temp:
  def __init__(self, name, value):
    self.name = name
    self.value = value

class input_model:
  def __init__(self, begin_node, des_node):
    self.begin_node = begin_node
    self.des_node = des_node
