# class Node:
#     def __init__(self,x):
#         self.data = x
#         self.next = None

# def mergeTwo(head1,head2):
#     dummy = Node(-1)
#     curr = dummy

#     while head1 is not None and head2 is not None:
        
#         if head1.data <= head2.data:
#             curr.next = head1
#             head1 = head1.next
#         else:
#             curr.next = head2
#             head2 = head2.next

#         curr = curr.next
    
#     if head1 is not None:
#         curr.next = head1
#     else:
#         curr.next = head2
    
#     return dummy.next

# def printList(node):
#     while node is not None:
#         print(f"{node.data}", end="")
#         if node.next is not None:
#             print(" -> ",end="")
#         node = node.next
    
#     print()
    
# def mergeList(arr):
#     res = None

#     for node in arr:
#         res = mergeTwo(res,node)
    
#     return res

# if __name__ == '__main__':
#     arr = []
#     node1 = Node(1)
#     node1.next = Node(3)
#     node1.next.next = Node(5)
#     node1.next.next.next = Node(7)
#     arr.append(node1)

#     node2 = Node(2)
#     node2.next = Node(4)
#     node2.next.next = Node(6)
#     node2.next.next.next = Node(8)
#     arr.append(node2)

#     node3 = Node(0)
#     node3.next = Node(9)
#     node3.next.next = Node(10)
#     node3.next.next.next = Node(11)
#     arr.append(node3)
  
#     head = mergeList(arr)
#     printList(head)

# class Node:
#     def __init__(self,val):
#         self.val = val
#         self.next = None

# def getMinNode(arr):
#     index = -1
#     mini = None

#     for i in range(len(arr)):
#         if arr[i] is None:
#             continue
#         if mini is None or arr[i].val < mini.val:
#             index = i
#             mini = arr[i]
    
#     if index != -1:
#         arr[index] = arr[index].next
    
#     return mini

# def mergeKList(arr):
#     dummy = Node(-1)
#     tail = dummy

#     mini = getMinNode(arr)

#     while mini:
#         tail.next = mini
#         tail = tail.next

#         mini = getMinNode(arr)

#     return dummy.next

# def printList(head):

#     while head is not None:
#         print(f"{head.val}",end="")
#         print(" -> ",end="")
#         head = head.next

# if __name__ == "__main__":
#     arr = []
#     node1 = Node(1)
#     node1.next = Node(3)
#     node1.next.next = Node(5)
#     node1.next.next.next = Node(7)
#     arr.append(node1)

#     node2 = Node(2)
#     node2.next = Node(4)
#     node2.next.next = Node(6)
#     node2.next.next.next = Node(8)
#     arr.append(node2)

#     node3 = Node(0)
#     node3.next = Node(9)
#     node3.next.next = Node(10)
#     node3.next.next.next = Node(11)
#     arr.append(node3)

#     head = mergeKList(arr)
#     printList(head)
import heapq
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def mergeKLists(arr):
    pq = []
    for i in range(len(arr)):
        head = arr[i]
        heapq.heappush(pq,(head.val,i,head))
    
    dummy = Node(-1)
    tail = dummy

    while pq:
        _, index, top = heapq.heappop(pq)

        tail.next = top
        tail = top

        if top.next is not None:
            heapq.heappush(pq,(top.next.val,index,top.next))
    
    return dummy.next

def printList(node):
    while node is not None:
        print(node.val, end="")
        if node.next is not None:
            print("->", end="")
        node = node.next
    print()

if __name__ == "__main__":
    k = 3

    arr = [None] * k

    arr[0] = Node(1)
    arr[0].next = Node(3)
    arr[0].next.next = Node(5)
    arr[0].next.next.next = Node(7)

    arr[1] = Node(2)
    arr[1].next = Node(4)
    arr[1].next.next = Node(6)
    arr[1].next.next.next = Node(8)

    arr[2] = Node(0)
    arr[2].next = Node(9)
    arr[2].next.next = Node(10)
    arr[2].next.next.next = Node(11)

    head = mergeKLists(arr)

    printList(head)