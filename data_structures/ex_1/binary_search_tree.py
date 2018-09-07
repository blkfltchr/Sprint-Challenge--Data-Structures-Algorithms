class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

# According to http://mishadoff.com/blog/dfs-on-binary-tree-array/:

# DFS checks all nodes from leftmost path from the root to the leaf, 
# then jumps up and check right node and so on.

  def depth_first_for_each(self, cb):
    # create a callback function passing in the search value 
    cb(self.value)
    # start by traverse the tree to the left for as long as possible
    if self.left: # more concise than if self.left is not None:
      # search to the left for the value using the callback
      self.left.depth_first_for_each(cb)
    # next, traverse the tree to the right for as long as possible
    if self.right:
      # search to the right for the value using the callback
      self.right.depth_first_for_each(cb)   

# According to https://medium.com/basecs/breaking-down-breadth-first-search-cebe696709d9:
# BFS traverses through one level of children nodes,
# then traverses through the level of grandchildren nodes (and so on...)

  def breadth_first_for_each(self, cb):
    # create a queue and turn the tree into a queue
    queue = [self]
    # Search the queue as long as it isn't empty 
    while len(queue) > 0:
      # remove the current node
      current = queue.pop(0)
      # create a callback function passing in the current value 
      cb(current.value)
      # add children to the left to the queue
      if current.left:
        queue.append(current.left)
      # add children to the right to the queue
      if current.right:
        queue.append(current.right)
    return

  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
