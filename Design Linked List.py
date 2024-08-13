class Node():

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.left = Node(0)
        self.right = Node(0)
        self.left.next = self.right
        self.right.prev = self.left     

    def get(self, index: int) -> int:
        current = self.left.next
        while current and index > 0:
            current = current.next
            index -= 1
        if current and current != self.right and index == 0:
            return current.value
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        cur_head = self.left.next
        new_head = Node(val)
        new_head.next = self.left.next
        new_head.prev = self.left
        cur_head.prev = new_head
        self.left.next = new_head

    def addAtTail(self, val: int) -> None:
        cur_tail = self.right.prev
        new_tail = Node(val)
        new_tail.next = self.right
        new_tail.prev = cur_tail
        cur_tail.next = new_tail
        self.right.prev = new_tail

    def addAtIndex(self, index: int, val: int) -> None:
        current = self.left.next
        new_node = Node(val)
        while current and index > 0:
            current = current.next
            index -= 1
        if current and index == 0:
            prev_node = current.prev
            prev_node.next = new_node
            new_node.next = current
            current.prev = new_node
            new_node.prev = prev_node


    def deleteAtIndex(self, index: int) -> None:
        current = self.left.next
        while current and index > 0:
            current = current.next
            index -= 1
        if current and current != self.right and index == 0:
            prev_node, next_node = current.prev, current.next
            next_node.prev = prev_node
            prev_node.next = next_node
            



        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
