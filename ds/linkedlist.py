
class Node:
    def __init__(self, data=None):
        self.data=data;
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.current=None
    
    def insert(self, data):
        node = Node(data)
        if not self.head:
            self.head=node
            self.current=node
        else:
            self.current.next=node
    
    def showList(self):
        temp = self.head
        cnt = 0
        while temp:
            cnt +=1 
            print(f'{temp.data}-->', end='')
            temp = temp.next
        
        print(cnt)

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert(10)
    ll.insert(14)
    ll.insert(17)
    ll.insert(23)
    ll.insert(30)
    ll.showList()


    