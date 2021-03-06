from LinkedList import LinkedList

class HashTable:

  def __init__(self, size):
    self.size = size
    self.arr = self.create_arr(size)


  # 1️⃣ TODO: Complete the create_arr method.

  # Each element of the hash table (arr) is a linked list.
  # This method creates an array (list) of a given size and populates each of its elements with a LinkedList object.

  def create_arr(self, size):
      #instantiation of array
    arr = []
    #uses the size parameter to append one Linked List function call to each index within range
    for i in range(size):
      new_ll = LinkedList()
      arr.append(new_ll)

    return arr




  # 2️⃣ TODO: Create your own hash function.

  # Hash functions are a function that turns each of these keys into an index value that we can use to decide where in our list each key:value pair should be stored. 

  def hash_func(self, key):
    return (ord(key[0]) - ord('s')) % self.size




  # 3️⃣ TODO: Complete the insert method.

  # Should insert a key value pair into the hash table, where the key is the word and the value is a counter for the number of times the word appeared. When inserting a new word in the hash table, be sure to check if there is a Node with the same key in the table already.

  def insert(self, key, value):
    #Find the index where the key value should be placed
    key_index = self.hash_func(key)

    # range of index value to tell if key is found within array
    found = self.arr[key_index].find(key)

    # if key is within array, take the value associated with it and increment it according to frequency of occurance
    if found == -1:
        toople = (key, value)
        self.arr[key_index].append(toople)


    # inserting the associated tuple into the Linked List 
       








  # 4️⃣ TODO: Complete the print_key_values method.

  # Traverse through the every Linked List in the table and print the key value pairs.

  # For example: 
  # a: 1
  # again: 1
  # and: 1
  # blooms: 1
  # erase: 2

  def print_key_values(self):
    if self.size == None:
      print("empty")
      return -1
    else:
      for i in self.arr:
        i.print_nodes()




