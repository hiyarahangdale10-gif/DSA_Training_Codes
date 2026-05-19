# Given two string s and t. Return the minimum number of operations required to convert
# s = "ycce"
# t = "ycsce"
# output = 0
# count = 0
# if len(s)>len(t):
#     output = len(t)-len(s)
# elif len(t)<len(s):
#     output = len(s)-len(t)
# elif len(s)==len(t):
#     for i in range (len(s)):
#         if s[i]!=t[i]:
#             count +=1
#     output = count
# print(output)



# #Doubly linked list
# import sys
# class GetNode:
#     def __init__(self):
#         self.data = None
#         self.left = None
#         self.right = None
# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None
#     def append(self):
#         data = int(input("Enter the data : "))
#         newNode = GetNode()
#         newNode.data = data
#         if self.head is  None:
#             self.head = newNode
#         else:
#             ptr = self.head
#             while ptr.right != None:
#                 ptr = ptr.right
#             ptr.right = newNode
#         print(data, "is added")
#     def traverse(self):
#         if self.head is None:
#             print("List not present")
#         else:
#             ptr = self.head
#             while ptr != None:
#                 print(ptr.data, "->", end=" ")
#                 ptr = ptr.right
#             print("None")
#     def AddAtBegin(self):

# if __name__ == '__main__':
#     obj = DoublyLinkedList()
#     while True:
#         print("\n1. Append")
#         print("2. Traverse")
#         print("0. Exit")
#         n = int(input("Select any choice : "))
#         if n == 1:
#             obj.append()
#         elif n == 2:
#             obj.traverse()
#         elif n == 0:
#             sys.exit()
#         else:
#             print("Invalid Choice")



# Doubly linked list
import sys
class GetNode:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def append(self):
        data = int(input("Enter the data : "))
        newNode = GetNode()
        newNode.data = data
        if self.head is None:
            self.head = newNode
        else:
            ptr = self.head
            while ptr.right is not None:
                ptr = ptr.right
            ptr.right = newNode
            newNode.left = ptr
        print(data, "is added")
    def traverse(self):
        if self.head is None:
            print("List not present")
        else:
            ptr = self.head
            while ptr is not None:
                print(ptr.data, "->", end=" ")
                ptr = ptr.right
            print("None")
    def AddAtBegin(self):
        data = int(input("Enter the data : "))
        newNode = GetNode()
        newNode.data = data
        if self.head is None:
            self.head = newNode
        else:
            newNode.right = self.head
            self.head.left = newNode
            self.head = newNode
        print(data, "added at beginning")
if __name__ == '__main__':
    obj = DoublyLinkedList()
    while True:
        print("\n1. Append")
        print("2. Traverse")
        print("3. Add At Begin")
        print("0. Exit")
        n = int(input("Select any choice : "))
        if n == 1:
            obj.append()
        elif n == 2:
            obj.traverse()
        elif n == 3:
            obj.AddAtBegin()
        elif n == 0:
            sys.exit()
        else:
            print("Invalid Choice")