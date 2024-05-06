class Node:
    '''A class to house Single Linked Lists for data permanence'''
    def __init__(self, obj, ptr_next):
        self.__obj = obj
        self.__ptr_next = ptr_next

    # return node object that is stored
    def get_data(self):
        return self.__obj

    # save the node object
    def set_data(self, obj):
        self.__obj = obj

    #get link to the next node
    def get_next(self):
        return self.__ptr_next

    # set the link to next node
    def set_next(self, node_next):
        self.__ptr_next = node_next