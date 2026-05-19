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
#         if self.head is None:
#             self.head = newNode
#         else:
#             ptr = self.head
#             while ptr.right is not None:
#                 ptr = ptr.right
#             ptr.right = newNode
#             newNode.left = ptr
#         print(data, "is added")
#     def traverse(self):
#         if self.head is None:
#             print("List not present")
#         else:
#             ptr = self.head
#             while ptr is not None:
#                 print(ptr.data, "->", end=" ")
#                 ptr = ptr.right
#             print("None")
#     def AddAtBegin(self):
#         data = int(input("Enter the data : "))
#         newNode = GetNode()
#         newNode.data = data
#         if self.head is None:
#             self.head = newNode
#         else:
#             newNode.right = self.head
#             self.head.left = newNode
#             self.head = newNode
#         print(data, "added at beginning")
#     def AddAtBetween(self):
#         pos = int(input("Enter the position : "))
#         data = int(input("Enter the data : "))
#         newNode = GetNode()
#         newNode.data = data
#         ptr = self.head
#         count = 1
#         while count < pos - 1 and ptr is not None:
#             ptr = ptr.right
#             count += 1
#         if ptr is None:
#             print("Position not found")
#         else:
#             newNode.right = ptr.right
#             newNode.left = ptr
#             if ptr.right is not None:
#                 ptr.right.left = newNode
#             ptr.right = newNode
#             print(data, "added at position", pos)

# if __name__ == '__main__':
#     obj = DoublyLinkedList()
#     while True:
#         print("\n1. Append")
#         print("2. Traverse")
#         print("3. Add At Begin")
#         print("4. Add At Between")
#         print("0. Exit")
#         n = int(input("Select any choice : "))
#         if n == 1:
#             obj.append()
#         elif n == 2:
#             obj.traverse()
#         elif n == 3:
#             obj.AddAtBegin()
#         elif n == 4:
#             obj.AddAtBetween()
#         elif n == 0:
#             sys.exit()
#         else:
#             print("Invalid Choice")



# Implement astack using singly linked list
# import sys
# class GetNode:
#     def __init__(self):
#         self.data = None
#         self.next = None
# class Stack:
#     def __init__(self):
#         self.top = None
#     def push(self):
#         data = int(input("Enter the data : "))
#         newNode = GetNode()
#         newNode.data = data
#         if self.top is None:
#             self.top = newNode
#         else:
#             newNode.next = self.top
#             self.top = newNode
#         print(data, "is pushed")
#     def pop(self):
#         if self.top is None:
#             print("Stack is empty")
#         else:
#             temp = self.top
#             self.top = self.top.next
#             print(temp.data, "is popped")
#     def peek(self):
#         if self.top is None:
#             print("Stack is empty")
#         else:
#             print("Top element :", self.top.data)
#     def traverse(self):
#         if self.top is None:
#             print("Stack is empty")
#         else:
#             ptr = self.top
#             while ptr is not None:
#                 print(ptr.data, "->", end=" ")
#                 ptr = ptr.next
#             print("None")

# if __name__ == '__main__':
#     obj = Stack()
#     while True:
#         print("\n1. Push")
#         print("2. Pop")
#         print("3. Peek")
#         print("4. Traverse")
#         print("0. Exit")
#         n = int(input("Select any choice : "))
#         if n == 1:
#             obj.push()
#         elif n == 2:
#             obj.pop()
#         elif n == 3:
#             obj.peek()
#         elif n == 4:
#             obj.traverse()
#         elif n == 0:
#             sys.exit()
#         else:
#             print("Invalid Choice")



# Stock span problem
# input : N = 7 , price= [100,80,60,70,60,75,85]
# output : 1 1 1 8 1 8 8
# explanation : traversing the given input span for 100 will be 1,
# 80 is smaller then 100 so the span is 1, 
# 60 is smaller then 80 so the span is 1, 
# 70 is smaller then 60 so the span is 2, 
# 60 is smaller then 70 so the span is 1, 
# 75 is smaller then 60 so the span is 2, 
# 85 is smaller then 75 so the span is 2, 
# Hence the output will be 1 1 1 2 1 2 2

# N = 7
# price = [100, 80, 60, 70, 60, 75, 85]
# ans = [1]
# for i in range(1, N):
#     if price[i] < price[i - 1]:
#         ans.append(1)
#     else:
#         ans.append(2)
# for i in range(N):
#     print(ans[i] ** 3, end=" ")
