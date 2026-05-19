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



# Implement a stack using singly linked list
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




# Implement queue using Linked list
# class GetNode:
#     def __init__(self):
#         self.data = None
#         self.next = None
# class Queue:
#     def __init__(self):
#         self.head = None
#         self.rear = None
#     def append(self):
#         data = int(input("Enter the data : "))
#         newNode = GetNode()
#         newNode.data = data
#         if self.head is None:
#             self.head = newNode
#             self.rear = newNode
#         else:
#             self.rear.next = newNode
#             self.rear = newNode
#         print(data, "inserted into queue")
#     def deleteAtBegin(self):
#         if self.head is None:
#             print("Queue is empty")
#         else:
#             ptr = self.head
#             self.head = ptr.next
#             if self.head is None:
#                 self.rear = None
#             print(ptr.data, "is deleted")
#     def traverse(self):
#         if self.head is None:
#             print("Queue is empty")
#         else:
#             ptr = self.head
#             while ptr is not None:
#                 print(ptr.data, end=" ")
#                 ptr = ptr.next
#             print()
# q = Queue()
# while True:
#     print("\n1.Insert")
#     print("2.Delete")
#     print("3.Traverse")
#     print("0.Exit")
#     choice = int(input("Enter choice : "))
#     if choice == 1:
#         q.append()
#     elif choice == 2:
#         q.deleteAtBegin()
#     elif choice == 3:
#         q.traverse()
#     elif choice == 0:
#         break
#     else:
#         print("Invalid Choice")



# import sys
# class GetNode:
# 	def __init__(self,data):
# 		self.data=data
# 		self.link=None
# class LinkedList:
# 	def __init__(self):
# 		self.head=None
# 		#ptr=GetNode()
# 	def append(self):
# 		data=int(input("Enter data: "))
# 		new_node=GetNode(data)
# 		#new_node.data=data
# 		if self.head is None:
# 			self.head=new_node
# 		else:
# 			ptr=self.head
# 			while ptr.link is not None:
# 				ptr=ptr.link
# 			ptr.link=new_node
# 		print(data,"is added..")
# 	def traverse(self):
# 		ptr=self.head
# 		while ptr is not None:
# 			print(" -> ",ptr.data,end="")
# 			ptr=ptr.link
# 	def addAtBegin(self):
# 		data=int(input("Enter data: "))
# 		new_node=GetNode(data)
# 		#new_node.data=data
# 		if self.head is None:
# 			self.head=new_node
# 		else:
# 			new_node.link=self.head
# 			self.head=new_node
# 		print(data,"is added at begin..")
# 	def addAtAfter(self):
# 		data=int(input("Enter data: "))
# 		new_node=GetNode(data)
# 		key=int(input("Enter data after which data will be added: "))
# 		if self.head is None:
# 			self.head=new_node
# 		else:
# 			ptr=self.head
# 			while ptr.link is not None:
# 				if key==ptr.data:
# 					break
# 				else:
# 					ptr=ptr.link
# 			if ptr.link is None:
# 				print(key," not found ")
# 			else:
# 				ptr1=ptr.link
# 				new_node.link=ptr1
# 				ptr.link=new_node
# 				print(data,"is added after ",key)
# 	def addAtBefore(self):
# 		data=int(input("Enter data: "))
# 		new_node=GetNode(data)
# 		key=int(input("Enter data before which data will be added: "))
# 		if self.head is None:
# 			self.head=new_node
# 		else:
# 			ptr=self.head
# 			while ptr.link is not None:
# 				if key==ptr.data:
# 					break
# 				else:
# 					ptr1=ptr
# 					ptr=ptr.link
# 			if ptr.link is None:
# 				print(key," not found ")
# 			else:
# 				new_node.link=ptr
# 				ptr1.link=new_node
# 				print(data,"is added after ",key)
# 	def addAtEnd(self):
# 		data=int(input("Enter data: "))
# 		new_node=GetNode(data)
# 		if self.head is None:
# 			self.head=new_node
# 		else:
# 			ptr=self.head
# 			while ptr.link is not None:
# 				ptr=ptr.link
# 			ptr.link=new_node
# 		print(data,"is added at the end..")
# 	def deleteAtBegin(self):
# 		if self.head is None:
# 			print("LinkedList is empty..")
# 		else:
# 			ptr=self.head
# 			ptr1=ptr.link
# 			ptr.link=None
# 			self.head=ptr1
# 		print(ptr.data,"is deleted from begin..")
# 	def deleteAtAfter(self):
# 		key=int(input("Enter data after which data will be added: "))
# 		if self.head is None:
# 			print("LinkedList is empty..")
# 		else:
# 			ptr=self.head
# 			while ptr.link is not None:
# 				if key==ptr.data:
# 					break
# 				else:
# 					ptr=ptr.link
# 			if ptr.link is None:
# 				print(key," not found ")
# 			else:
# 				ptr1=ptr.link
# 				ptr2=ptr1.link
# 				ptr.link=ptr2
# 				ptr1.link=None
# 				print(ptr1.data," is deleted after ",key)
# 	def deleteAtValue(self):
# 		key=int(input("Enter data which node will be deleted: "))
# 		if self.head is None:
# 			print("LinkedList is empty..")
# 		else:
# 			ptr=self.head
# 			while ptr.link is not None:
# 				if key==ptr.data:
# 					break
# 				else:
# 					ptr1=ptr
# 					ptr=ptr.link
# 					ptr2=ptr.link
# 			if ptr.link is None:
# 				print(key," not found ")
# 			else:				
# 				ptr1.link=ptr2
# 				ptr.link=None
# 				print(ptr.data,"is deleted ",key)
# 	def deleteAtEnd(self):
# 		if self.head is None:
# 			print("LinkedList is empty..")
# 		else:
# 			ptr=self.head
# 			while ptr.link is not None:
# 				ptr1=ptr
# 				ptr=ptr.link
# 			ptr1.link=None
# 			print(ptr.data,"is deleted from the end..")	
# 	def length(self):
# 		len=0
# 		if self.head is None:
# 			print("LinkedList is empty..")
# 		else:
# 			ptr=self.head
# 			while ptr is not None:
# 				len=len+1
# 				ptr=ptr.link
# 			print("Size of LinkedList is ",len)

# obj=LinkedList()
# if __name__ == '__main__':
# 	while True:
# 		print("\n\n1. Append\t\t2. Add At Begin  \t3. Add At After")
# 		print("4. Add At Before\t5. Add At End\t\t6. Delete At Begin")
# 		print("7. Delete At After\t8. Delete Ay Node\t9. Delete At End")
# 		print("10. Length\t\t11. Traverse\t\t0. Exit")
# 		n=int(input("Select your choice: "))
# 		if n==1:
# 			obj.append()
# 		elif n==2:
# 			obj.addAtBegin()
# 		elif n==3:
# 			obj.addAtAfter()
# 		elif n==4:
# 			obj.addAtBefore()
# 		elif n==5:
# 			obj.addAtEnd()
# 		elif n==6:
# 			obj.deleteAtBegin()
# 		elif n==7:
# 			obj.deleteAtAfter()
# 		elif n==8:
# 			obj.deleteAtValue()
# 		elif n==9:
# 			obj.deleteAtEnd()
# 		elif n==10:
# 			obj.length()
# 		elif n==11:
# 			obj.traverse()
# 		elif n==0:
# 			sys.exit()



# import sys
# class GetNode:
# 	def __init__(self,data):
# 		self.data=data
# 		self.left=None
# 		self.right=None
# class LinkedList:
# 	def __init__(self):
# 		self.head=None
# 		#ptr=GetNode()
# 	def append(self):
# 		data=int(input("Enter data: "))
# 		new_node=GetNode(data)
# 		#new_node.data=data
# 		if self.head is None:
# 			self.head=new_node
# 		else:
# 			ptr=self.head
# 			while ptr.right is not None:
# 				ptr=ptr.right
# 			ptr.right=new_node
# 			new_node.left=ptr
# 			print(data,"is added..")
# 	def traverseForward(self):
# 		ptr=self.head
# 		while ptr is not None:
# 			print(" ->",ptr.data,end="")
# 			ptr=ptr.right
# 	def traverseBackward(self):
# 		if self.head is None:
# 			print("LinkedList is empty..")
# 		else:
# 			ptr=self.head
# 			while ptr.right is not None:
# 				ptr=ptr.right
# 			while ptr is not None:
# 				print(" ->",ptr.data,end="")
# 				ptr=ptr.left
# 	def addAtBegin(self):
# 		data=int(input("Enter data: "))
# 		new_node=GetNode(data)
# 		#new_node.data=data
# 		if self.head is None:
# 			self.head=new_node
# 		else:
# 			new_node.right=self.head
# 			self.head.left=new_node
# 			self.head=new_node
# 			print(data,"is added at begin..")
# 	def addAtAfter(self):
# 		data=int(input("Enter data: "))
# 		new_node=GetNode(data)
# 		key=int(input("Enter data after which data will be added: "))
# 		if self.head is None:
# 			self.head=new_node
# 		else:
# 			ptr=self.head
# 			while ptr.right is not None:
# 				if key==ptr.data:
# 					break
# 				else:
# 					ptr=ptr.right
# 			if ptr.right is None:
# 				print(key," not found ")
# 			else:
# 				ptr1=ptr.right
# 				new_node.right=ptr1
# 				ptr1.left=new_node
# 				ptr.right=new_node
# 				new_node.left=ptr
# 				print(data,"is added after ",key)
# 	def addAtBefore(self):
# 		data=int(input("Enter data: "))
# 		new_node=GetNode(data)
# 		key=int(input("Enter data after which data will be added: "))
# 		if self.head is None:
# 			self.head=new_node
# 		else:
# 			ptr=self.head
# 			while ptr.right is not None:
# 				if key==ptr.data:
# 					break
# 				else:
# 					ptr=ptr.right
# 			if ptr.right is None:
# 				print(key," not found ")
# 			else:
# 				ptr1=ptr.left
# 				new_node.right=ptr
# 				ptr.left=new_node
# 				ptr1.right=new_node
# 				new_node.left=ptr1
# 				print(data,"is added before ",key)
# 	def addAtEnd(self):
# 		data=int(input("Enter data: "))
# 		new_node=GetNode(data)
# 		#new_node.data=data
# 		if self.head is None:
# 			self.head=new_node
# 		else:
# 			ptr=self.head
# 			while ptr.right is not None:
# 				ptr=ptr.right
# 			ptr.right=new_node
# 			new_node.left=ptr
# 			print(data,"is added at the end..")
# 	def deleteAtBegin(self):
# 		if self.head is None:
# 			print("LinkedList is empty..")
# 		else:
# 			ptr=self.head
# 			ptr1=ptr.right
# 			ptr.right=None
# 			self.head=ptr1
# 			print(ptr.data,"is deleted from begin..")
# 	def deleteAtAfter(self):
# 		key=int(input("Enter data after which data will be added: "))
# 		if self.head is None:
# 			print("LinkedList is empty..")
# 		else:
# 			ptr=self.head
# 			while ptr.right is not None:
# 				if key==ptr.data:
# 					break
# 				else:
# 					ptr=ptr.right
# 			if ptr.right is None:
# 				print(key," not found ")
# 			else:
# 				ptr1=ptr.right
# 				ptr2=ptr1.right
# 				ptr.right=ptr2
# 				ptr2.left=ptr
# 				ptr1.right=None
# 				print(ptr1.data," is deleted after ",key)
# 	def deleteAtValue(self):
# 		key=int(input("Enter data which node will be deleted: "))
# 		if self.head is None:
# 			print("LinkedList is empty..")
# 		else:
# 			ptr=self.head
# 			while ptr.right is not None:
# 				if key==ptr.data:
# 					break
# 				else:
# 					ptr=ptr.right
# 			if ptr.right is None:
# 				print(key," not found ")
# 			else:
# 				ptr1=ptr.left
# 				ptr2=ptr.right
# 				ptr1.right=ptr2
# 				ptr2.left=ptr1
# 				ptr.right=None
# 				print(ptr.data,"is deleted at ",key)
# 	def deleteAtEnd(self):
# 		if self.head is None:
# 			print("LinkedList is empty..")
# 		else:
# 			ptr=self.head
# 			while ptr.right is not None:
# 				ptr=ptr.right
# 			ptr1=ptr.left
# 			ptr1.right=None
# 			print(ptr.data,"is deleted from the end..")	
# 	def length(self):
# 		len=0
# 		if self.head is None:
# 			print("LinkedList is empty..")
# 		else:
# 			ptr=self.head
# 			while ptr is not None:
# 				len=len+1
# 				ptr=ptr.right
# 			print("Size of LinkedList is ",len)

# obj=LinkedList()
# if __name__ == '__main__':
# 	while True:
# 		print("\n\n1. Append\t\t2. Add At Begin  \t3. Add At After")
# 		print("4. Add At Before\t5. Add At End\t\t6. Delete At Begin")
# 		print("7. Delete At After\t8. Delete Ay Node\t9. Delete At End")
# 		print("10. Length\t\t11. TraverseForward\t12. TraverseBackward \n0. Exit")
# 		n=int(input("Select your choice: "))
# 		if n==1:
# 			obj.append()
# 		elif n==2:
# 			obj.addAtBegin()
# 		elif n==3:
# 			obj.addAtAfter()
# 		elif n==4:
# 			obj.addAtBefore()
# 		elif n==5:
# 			obj.addAtEnd()
# 		elif n==6:
# 			obj.deleteAtBegin()
# 		elif n==7:
# 			obj.deleteAtAfter()
# 		elif n==8:
# 			obj.deleteAtValue()
# 		elif n==9:
# 			obj.deleteAtEnd()
# 		elif n==10:
# 			obj.length()
# 		elif n==11:
# 			obj.traverseForward()
# 		elif n==12:
# 			obj.traverseBackward()
# 		elif n==0:
# 			sys.exit()