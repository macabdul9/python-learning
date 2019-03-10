class Node:
    def __init__(self, data, nextNode = None):
        self.data = data
        self.next = nextNode


def printlist(current):
    while current is not None:
        print(current.data)
        current = current.next

#
# def insertnode(head, data):
#     newnode = Node(data)
#     tmp = head
#     #if linked list is empty
#     if tmp is None:
#         return newnode
#     #reach to the end of the ll to insert the node
#     while tmp.next is not None:
#         tmp = tmp.next
#     tmp.next = newnode
#     return head


#insertion is also possible in constant time just maintain the both end of the ll

def insertnode(end, data):
    newnode = Node(data)
    if end is None:
        return newnode
    else:
        end.next = newnode
        end = newnode
        return end

def pop_front(head):
    if head is None:
        return None
    return head.next


def pop_back(head):
    if head.next is None:
        return None
    tmp = head
    while tmp.next.next is not None:
        tmp = tmp.next
    return tmp


if __name__ == "__main__":
    end = head = insertnode(None, 10)
    end = insertnode(end, 20)
    end = insertnode(end, 30)
    end = insertnode(end, 40)
    printlist(head)
    print()
    head = pop_front(head)
    head = pop_front(head)
    printlist(head)
