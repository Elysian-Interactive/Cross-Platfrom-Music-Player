# Represents a node of the list
class Node:
    # Constructor
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
    # Hash Function
    def __hash__(self):
        return hash(self.key)
    # Comparision Function
    def __eq__(self, other):
        if isinstance(other, Node):
            return self.key == other.key
        return False

# Represents the list
class List:
    # Constructor
    def __init__(self):
        self.head = None
    
    def append(self, key, value):
        new_node = Node(key, value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def prepend(self, key, value):
        new_node = Node(key, value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def search(self, key):
        current = self.head
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None