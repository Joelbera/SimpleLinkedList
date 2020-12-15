class Node: 
    def __init__(self, value):
        self.value = value 
        self.next = None

class LinkedList: 
    # Head Pointer
    def __init__ (self): 
        self.head = None

    def Push(self, node ): 
        node.next = self.head
        self.head = node
    
    def Pop(self): 
        self.head = self.head.next

    def DeleteList(self):
        self.head = None

    def Search(self, value): 
        Pointer = self.head
        while True: 
            if Pointer.value == value: 
                print(f"Item {Pointer.value} in list at location: 0x{id(Pointer)}")
                break
            elif Pointer == None: 
                print("List Empty")
                break
            else: 
                Pointer = Pointer.next
                
    def PrintAll(self): 
        Pointer = self.head
        while True: 
            if Pointer == None: 
                break  
            else: 
                print(f"{Pointer.value} at 0x{id(Pointer)},")
                Pointer = Pointer.next