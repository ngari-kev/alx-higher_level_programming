#!/usr/bin/python3
'''This Module is a blue print of the creation of a Singly linked list'''


class Node:
    '''This class defines a node'''
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) or if value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    '''This class defines the actual singly linked list'''
    def __init__(self):
        self.head = None
