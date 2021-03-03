from Node import Node

class LinkedList:

  def __init__(self):
    self.head = None


  def append(self, new_data):
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node


  def find(self,item):

    current = self.head

    found = False
    counter = 0

    while current != None and not found:

      if current.data[0] == item:
        found = True
      else:
        current = current.next
        counter += 1

    if found:
      new_data = (current.data[0],(current.data[1]+1))
      current.data = new_data
    else:
      return -1



  def length(self):
    if self.head == None:
      return 0
    else:
      counter = 1
      current = self.head
      while(current.next):
        current = current.next
        counter +=1
      return counter

  # def delete(self, key):
  #   '''Helper function for deleting nodes'''
  #   current_node = self.head
  #   previous = None
    
  #   while current_node != None:
  #     if current_node.get_key() != key:
  #       previous = current_node
  #       current_node = current_node.next


  #     if current_node.get_key() == key:
  #       if previous == None:
  #         value1 = current_node.get_value()
  #         self.head = current_node.next
  #         return value1


  #       if current_node.next == None:
  #         #Remove last node
  #         value1 = current_node.get_value()
  #         previous.set_next(None)
  #         return value1

  #       value1 = current_node.get_value()
  #       previous.set_next(current_node.next)
  #       return value1
  #     return
          

  def print_nodes(self):
    current = self.head
    
    if current == None:
      pass
    else:
      for i in range(self.length()):
        print(f'{current.data[0]}:{current.data[1]}')
        current = current.next