class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self) -> None:
        self.head=None
    def add(self,data):
        nn=Node(data)
        if self.head is None:
            self.head=nn
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=nn
 
    def reverse(self):
        current=self.head
        prev=None
        while current:
            nn=current.next
            current.next=prev
            prev=current
            current=nn

        self.head=prev

    def insert_at_begining(self,data):
        nn=Node(data)
        nn.next=self.head
        self.head=nn
    
    def insert_at_end(self,data):
        nn=Node(data)
        current=self.head
        while current.next:
            current=current.next
        current.next=nn

    def insert_at_specific_pos(self,data,pos):
        nn=Node(data)
        current=self.head
        if pos==0:
            self.insert_at_begining(data)
        if pos<0:
            print("Invalid position")
        for i in range(pos):
            if current is None:
                print("Invalid position")
                return
            
            if pos==i+1:
                nn.next=current.next
                current.next=nn
                return
            current=current.next

    def delete_at_begining(self):
        current=self.head
        self.head=current.next

    def delete_at_end(self):
        current=self.head
        prev=None
        while current.next:
            prev=current
            current=current.next
        prev.next=None

    def delete_at_specific_pos(self,pos):
        if(pos<0):
            print("Invalid pos")
        if(pos==0):
            self.delete_at_begining()
        current=self.head
        for i in range(pos):
            if(i+1==pos):
                nn=current.next
                current.next=None
                current.next=nn.next
                return
            current=current.next

    def check_if_ement_is_preset(self,ele):
        current=self.head
        while current:
            if current.data==ele:
                return True
            current=current.next
        return False
    
    def concatLinkedList(self,secondLinkedList):
        current=self.head
        while current.next:
            current=current.next
        current.next=secondLinkedList.head


    def bubble_sort(self):
        if not self.head and not self.head.next:
            return
        swapped=True
        while swapped:
            swapped=False
            prev=None
            current=self.head
            while current and current.next:
                if current.data>current.next.data:
                    if prev:
                        prev.next,current.next.next,current.next=current.next,prev.next,current.next.next
                    else:
                        self.head,current.next.next,current.next=current.next,self.head,current.next.next
                    swapped=True
                current,prev=current.next,current
    
    
    def display(self,current=None):
        # current=self.head
        # while current:
        if current==None:
            current=self.head
        print(current.data)
        current=current.next
        if current:
            self.display(current)
ll=LinkedList()
# ll2=LinkedList()
ll.add(1)
ll.add(5)
ll.add(3)
ll.add(4)
# print("first list")
# ll.display()
# ll2.add(5)
# ll2.add(6)
# ll2.add(7)
# ll2.add(8)
# print("second list")
# ll2.display()

# print("combining 1st list with second")
# ll.concatLinkedList(ll2)
# ll.display()
# print("after rev")
# ll.reverse()
# ll.display()

# print("inserting 0 at begining of the ll")
# ll.insert_at_begining(0)
# ll.display()

# print("inserting 5 at the end of the ll")
# ll.insert_at_end(5)
# ll.display()

# print("inserting 6 at pos 2")
# ll.insert_at_specific_pos(6,5)
# ll.display()

# print("deleting element at begining")
# ll.delete_at_begining()
# ll.display()

# print("deleting element at end")
# ll.delete_at_end()
# ll.display()

# print("deleting element at 1")
# ll.delete_at_specific_pos(1)
# ll.display()


# a=ll.check_if_ement_is_preset(10)
# print("checking if number is preset",a)
# ll.display()
# ll.display()
ll.display()
print("after bubble sort")
ll.bubble_sort()
ll.display()

