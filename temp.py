class Node:
    '''A class to house Single Linked Lists for data permanence'''
    def __init__(self, data= None):
        self.data = data
        self.next = None

class SLL:
    '''Class to house SLL functionality'''
    # declaring class variables and assigning initial values and creating an empty single linked list
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def append_node(self, data):
        node = Node(data)
        if self.__head:
            self.__head.next = node
            self.__head = node
        else:
            self.__tail = node
            self.__head = node
        self.__size += 1

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
            current = current.next
            yield value

    def search_sll(self, data):
        for node in self.iterate():
            if data == node:
                return True
        return False

    def patient_view(self):
        curr = self.__head
        print(curr)
        while curr != None:
            print(curr.data, curr)
            curr = curr.next

items = SLL()
items.append_node('PHP')
items.append_node('Python')
items.append_node('C#')
items.append_node('C++')
items.append_node('Java')

items.patient_view()

if items.search_sll('SQL'):
    print("True")
else:
    print("False")

if items.search_sll('C++'):
    print("True")
else:
    print("False")