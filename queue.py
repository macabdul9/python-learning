from Node import Node

def createNode(data):
    node = Node(data)
    return node

def printqueue(front):
    if front is None:
        return
    while front is not None:
        print(front.data)
        front = front.next


def push(back, data):
    newnode = createNode(data)
    if back is None:
        return newnode
    back.next = newnode
    back = newnode
    return back


def pop(front):
    if front is None:
        return
    tmp = front.next
    del front
    front = tmp
    return front

if __name__ == '__main__':
    front = back = push(None, 10)
    back = push(back, 20)
    back = push(back, 30)
    back = push(back, 40)
    printqueue(front)
    print()
    front = pop(front)
    printqueue(front)