#!/usr/bin/python3

"""This module defines a node of a singly linked list.
"""


class Node:
    """Node class of a linked list"""
    def __init__(self, data, next_node=None):
        """Initializing a node with data and pointing to the next node.

        args:
            data: an integer representing data field of a node.
            new_node: pointing to the next node or None if there no more nodes.
        """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data
        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node

    @property
    def data(self):
        """Return an integer or data from the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the integer to data attribute

        args:
            value: must be integer or raise an exception if not.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Return a next node pointed to by the current node or Node
        if there no more nodes or if there is no next node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets a pointer to the next node and can be
        refered to as next node."""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Create a singly linked list"""
    def __init__(self):
        """Initializing a linked list with no node"""
        self.__head = None

    def sorted_insert(self, value):
        """Adds a new_node in a sorted manner.
        Checks if the current node in not none and also
        if contains an integer greater or less the value.

        args:
            value: an integer for the new node to add.
        """
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and\
                    current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """string represention of the linked list."""
        result = []
        current = self.__head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return ("\n".join(result))
