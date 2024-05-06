from node import Node

class SLL:
    '''Class to house SLL functionality'''
    # declaring class variables and assigning initial values and creating an empty single linked list
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def append_node(self, data, pointer):
        node = Node(data, pointer)
        if self.__head:
            self.__head.next = node
            self.__head = node
        else:
            self.__tail = node
            self.__head = node
        self.__size += 1
        print(node)

    # A node function to gets the node and returns the node in a certain place
    def get_node(self, pos):
        counter = 1
        tmp_node = None
        # loop through nodes until required position is reached
        while counter <= pos:
            if counter == 1:
                tmp_node = self.__head
            else:
                tmp_node = tmp_node.get_next()
            counter = counter + 1
        # looped to a required position and returning the node at position
        return tmp_node

    def iterate(self):
        current = self.__tail
        while current:
            value = current.data
            current = current.pointer
            yield value

    def search_sll(self, data):
        for node in self.iterate():
            print(node)
            if data == node:
                return True
        return False

    def patient_view(self):
        curr = self.__head
        while curr != None:
            curr = curr.get_data()
            curr = curr.get_next()
            print(curr)

        # method to insert a node/object at the start
    def insert_start(self, new_data, ptr):
        # creating an object
        new_node = Node(new_data, ptr)
        # giving the new objects pointer equal the old head object
        new_node.next = self.__head
        if self.__head == None:
            self.__head == new_node
        else:
        # making the new object the head or first object
            new_node.next= self.__head
            self.__head = new_node
        self.__size = self.__size + 1

    # method to insert object at the start of the linked list
    def insert_end(self, new_data, last_node):
        if last_node is None:
            print("List of patient not created yet")
            return
        new_node = Node(new_data, last_node)
        last = self.__head
        while (last.next):
            last = last.next
        last.next = new_node
        self.__size = self.__size + 1

    def insert_particular(self, data, position):
        count = 1
        curr = self.__head
        while count < position - 1 and curr != None:
            curr = curr.next
            count += 1
        temp = Node(data, position)
        temp.next = curr.next
        curr.next = temp
        self.__size = self.__size + 1

    def remove(self, pos):
        if pos == 1: # if in position 1
            tmp_node = self.get_node(1)
            self.__head = tmp_node.get_next()
        elif pos == self.__size and self.__size > 1: # last in SLL
            tmp_node = self.get_node(pos -1)
            tmp_node.set_next(None)
        else: # middle node
            current = self.get_node(pos)
            previous = self.get_node(pos-1)
            previous.set_next(current.get_next())
        self.__size = self.__size -1 #decrement the counter

    def size(self):
        return self.__size
