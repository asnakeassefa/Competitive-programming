class MyLinkedList:

    def __init__(self):
        self.LinkedList = []

    def get(self, index: int) -> int:
        if index < len(self.LinkedList) and self.LinkedList[index] != None:
            return self.LinkedList[index]
        else:
            return -1
    def addAtHead(self, val: int) -> None:
        self.LinkedList.insert(0,val)

    def addAtTail(self, val: int) -> None:
        self.LinkedList.append(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if len(self.LinkedList) < index:
            self.LinkedList = [-1] * (index - len(self.LinkedList))
        self.LinkedList.insert(index,val)

    def deleteAtIndex(self, index: int) -> None:
        if index < len(self.LinkedList):
            self.LinkedList.pop(index)


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)