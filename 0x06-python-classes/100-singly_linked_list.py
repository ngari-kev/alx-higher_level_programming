#!/usr/bin/python3
'''
This Module is a blue print of the creation of a Singly linked list.
Serves both the Node class and the SinglyLinkedList class
'''


class Node:
    '''
    This class defines a node.
    Args:
        data - actual data to be stored in the node
        next_node - pointer to the next node
    '''
    def __init__(self, data, next_node=None):
        '''Initialize the data and next_node attributes'''
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        '''Getter method for the data attribute'''
        return self.__data

    @data.setter
    def data(self, value):
        '''setter method for the data attribute'''
        self.__data = value

    @property
    def next_node(self):
        '''Getter method for the next_node attribute'''
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        '''Setter method for the next_node attribute'''
        if not isinstance(value, Node) or if value is not None:
            '''Ensure that next_node is a Node item or None'''
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    '''
    This class defines the actual singly linked list
    Args:
        head - set to None
    '''
    def __init__(self):
        self.head = None
