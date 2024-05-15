# node creation with data and next pointer
class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self) -> None:
        self.head=None

    # adding elements to linked list
    def append(self,data):
        # creating new node
        new_node=Node(data)

        if not self.head:
            self.head=new_node
            return
        current=self.head

        # setting next pointer to the last node to the new node
        while current.next:
            current=current.next
        current.next=new_node

    # itterating through all the nodes from the head node
    def display(self):
        current=self.head
        while current:
            print(current.data,end=" ")
            current=current.next

    def remove(self,value):
        # comparing and updating the head node if the remove value equal to the head node value
        if self.head.data==value:
            self.head=self.head.next
            return
        current=self.head

        # comparing and updating if other nodes next equal to the remove value
        while current.next:
            if(current.next.data==value):
                current.next=current.next.next
                return 
            current=current.next
ll=LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.display()

ll.remove(4)
ll.display()
