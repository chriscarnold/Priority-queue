class CinemaPriorityQueue:
    """A linked list implementation of an unbounded min-priority queue."""

    class Node:
        """A node in a linked list."""

        def __init__(self, item: object, priority_value: int) -> None:
            """Initialise the node with the given item and priority value."""
            self.item = item
            self.priority = priority_value
            self.next = None

    def __init__(self) -> None:
        """Initialise the queue to be empty."""
        self.head = None

    def is_empty(self) -> bool:
        """
        Preconditions: true
        Postconditions: the output is true if the queue is empty, false otherwise
        """
        return self.head == None

    def print(self) -> None:
        """Print out the queue"""
        if self.head == None:
            print('The queue is empty')
        else:
            current = self.head
            while current != None:
                print(current.item, current.priority)
                current = current.next

    def insert(self, item: object, priority_value: int) -> None:
        """Insert item according to priority.
        Preconditions: true
        Postconditions: post-self is the sequence
        pre-self with item inserted after
        the last item in self with the same priority
        """
        # we are creating a new instance with item and prority_value
        new_node = CinemaPriorityQueue.Node(item, priority_value)
        
        # using a dummy variable to walk through the priority values in the queue
        walk = self.head
        
        # inserting the item if the list is empty
        if self.head == None:
            new_node.next = self.head
            self.head = new_node 
            
        # inserting the item to be on top of the queue
        elif self.head.priority > new_node.priority:
            new_node.next = self.head
            self.head = new_node
            
        # otherwise inserting the item into the appropriate position in the queue using our dummy variables
        else:
            while walk.next: #looping until we find the node that is in the correct priority range
                if new_node.priority < walk.next.priority:
                    break
                    
                walk = walk.next
                
            new_node.next = walk.next
            # hangs the rest of the queue to the new item
            
            walk.next = new_node
            # hangs the new node at the end of the appropriate priority range
            # if there no items of that priority range in the queue it hangs the new node
            # at the end of the next lower priority range
