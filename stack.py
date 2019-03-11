class Stack:
    class Node:
        def __init__(self, prevNode, value, nextNode = None):
            self.prev = prevNode
            self.data = value
            self.next = nextNode

    #
    # def isEmpty(self, stack):
    #     if stack is None:
    #         return True
    #     else:
    #         return False


    def push(self, top, data):
        newNode = Stack.Node(data)
        if top is None:
            return newNode
        else:
            tmp = top
            tmp.next = newNode
            newNode.prev = tmp
            top = newNode
            return top

    def pop(self, top):
        if top or top.next is None:
            return None
        else:
            top = top.prev
            top.next = None
            return top



    def printStack(self, top):
        if top is None:
            return
        while top is not None:
            print(top.data)
            top.prev


    if __name__ == '__main__':
        top = push(None, 10) #initially head and top will be same node
        top = push(top, 20)
        top = push(top, 30)
        printStack(top)
