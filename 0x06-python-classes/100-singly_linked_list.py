#!/usr/bin/python3

"""class Node"""


class Node:
    """class Node"""
    def __init__(self, data, next_node=None):
        """
        Initialize a Node instance.

        Args:
            data (int): The data value for the node.
            next_node (Node, optional): The next node in the linked list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Get the data value of the node.

        Returns:
            int: The data value of the node.
        """
        return self.__data

    @property
    def next_node(self):
        """
        Get the next node in the linked list.

        Returns:
            Node: The next node in the linked list.
        """
        return self.__next_node

    @data.setter
    def data(self, value):
        """
        Set the data value of the node.

        Args:
            value (int): The data value to be set.

        Raises:
            TypeError: If the value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        """
        Set the next node in the linked list.

        Args:
            value (Node or None): The next node to be set.

        Raises:
            TypeError: If the value is not a Node object or None.
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """SinglyLinkedList"""
    def __init__(self):
        """
        Initialize a SinglyLinkedList instance.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Insert a new node with the given value into the linked list.

        Args:
            value (int): The value to be inserted.
        """
        new_node = Node(value)
        if self.head is None or self.head.data > value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            crnt = self.head
            while crnt.next_node is not None and crnt.next_node.data < value:
                crnt = crnt.next_node
            new_node.next_node = crnt.next_node
            crnt.next_node = new_node

    def __str__(self):
        """
        Generate a string representation of the linked list.

        Returns:
            str: The string representation of the linked list.
        """
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next_node
        return "\n".join(nodes)
