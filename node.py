class Node:
    '''A class to house Single Linked Lists for data permanence'''
    def __init__(self, obj, pointer):
        self.__obj = obj
        self.pointer = pointer

    # return node object that is stored
    def get_data(self):
        print(self.__obj)
        return self.__obj

    # save the node object
    def set_data(self, obj):
        self.__obj = obj

    #get link to the next node
    def get_next(self):
        print(self.pointer)
        return self.pointer

    # set the link to next node
    def set_next(self, node_next):
        self.pointer = node_next