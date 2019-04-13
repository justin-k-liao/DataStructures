class Node:

    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class MatthewLL:

    def __init__(self):
        self.head = None

    def add(self, value):
        if self.head is None:
            self.head = Node(value, None)
            return
        #print(self.head.next)
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(value, None)
        # TODO

    def index(self, pos):
        # TODO
        if pos < 0:
            raise ValueError("pos cannot be negative")
        current = self.head
        for i in range(0, pos):
            if current.next is not None:
                current = current.next
            else:
                raise ValueError("outside range")
        return current.value

    def pop(self, pos):
        if pos < 0:
            raise ValueError("pos cannot be negative")
        current = self.head
        if pos == 0:
            self.head = current.next

        for i in range(0, pos - 1):
            if current.next is not None:
                current = current.next
            else:
                raise ValueError("outside range")
        if current.next.next is None:
            current.next = None
        else:
            current.next = current.next.next


