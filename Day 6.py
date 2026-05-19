# Merge sort with sorted list
# class MergeSort:
#     def mergesort(self,arr1,arr2):
#         arr3 = []
#         i = 0
#         j = 0
#         k = 0 
#         while i<len(arr1) and j<len(arr2):
#             if arr1[i]<arr2[j]:
#                 arr3.append(arr1[i])
#                 i+=1
#                 k+=1
#             else:
#                 arr3.append(arr2[j])
#                 j+=1
#                 k+=1
#         while len(arr1)>i:
#             arr3.append(arr1[i])
#             i+=1
#             k+=1
#         while len(arr2)>j:
#             arr3.append(arr2[j])
#             j+=1
#             k+=1
#         return arr3

# if __name__ == '__main__':
#     obj=MergeSort()
#     arr1 = [1,3,5]
#     arr2 = [2,4,6]
#     ans = obj.mergesort(arr1,arr2)
#     print(ans)



# Merge sort with unsorted list

# HINTS
#The idea of merge sort
#Divide the list into smaller parts
#Sort each smaller parts
#Merge them back together

# class MergeSort:
#     def mergesort(self,arr):
#         if len(arr) <= 1:
#             return arr
#         mid = len(arr)//2
#         arr1 = self.mergesort(arr[:mid])
#         arr2 = self.mergesort(arr[mid:])
#         i = 0
#         j = 0
#         k = 0
#         while i < len(arr1) and j < len(arr2):
#             if arr1[i] < arr2[j]:
#                 arr[k] = arr1[i]
#                 i += 1
#                 k += 1
#             else:
#                 arr[k] = arr2[j] 
#                 j += 1
#                 k += 1
#         while len(arr1) > i:
#             arr[k] = arr1[i]
#             i += 1
#             k += 1
#         while len(arr2) > j:
#             arr[k] = arr2[j]
#             j += 1
#             k += 1
#         return arr
    
# if __name__ == '__main__':
#     obj = MergeSort()
#     arr1 = [5, 2, 8, 1, 3]
#     arr1 = obj.mergesort(arr1)
#     print(arr1)



# Linked list
# import sys
# class GetNode:
#     def __init__(self):
#         self.data = None
#         self.next = None
# class LinkedList:
#     def __init__(self):
#         self.head = None
#     def append(self):
#         data = int(input("Enter the data : "))
#         newNode = GetNode()
#         newNode.data = data
#         if self.head == None:
#             self.head = newNode
#         else:
#             ptr = self.head
#             while ptr.next != None:
#                 ptr = ptr.next
#             ptr.next = newNode
#         print(data, "is added")
#     def traverse(self):
#         if self.head == None:
#             print("Linked list not present")
#         else:
#             ptr = self.head

#             while ptr != None:
#                 print(ptr.data, "->", end=" ")
#                 ptr = ptr.next
#             print("None")
#     def addAtBegin(self):
#         data = int(input("Enter the data : "))
#         newNode = GetNode()
#         newNode.data = data
#         if self.head == None:
#            self.head=newNode
#         else :
#             ptr = self.head
#             newNode.next=ptr
#             self.head = newNode
#         print(data, "added at beginning") 

# if __name__ == '__main__':
#     obj = LinkedList()
#     while True:
#         print("\n1. Append")
#         print("2. Traverse")
#         print("3. Add at Begin")
#         print("0. Exit")
#         n = int(input("Select any choice : "))
#         if n == 1:
#             obj.append()
#         elif n == 2:
#             obj.traverse()
#         elif n == 3:
#             obj.addAtBegin()
#         elif n == 0:
#             sys.exit()



# import sys
# class GetNode:
#     def __init__(self):
#         self.data = None
#         self.next = None
# class LinkedList:
#     def __init__(self):
#         self.head = None
#     def append(self):
#         data = int(input("Enter the data : "))
#         newNode = GetNode()
#         newNode.data = data
#         if self.head == None:
#             self.head = newNode
#         else:
#             ptr = self.head
#             while ptr.next != None:
#                 ptr = ptr.next
#             ptr.next = newNode
#         print(data, "is added")
#     def traverse(self):
#         if self.head == None:
#             print("Linked list not present")
#         else:
#             ptr = self.head
#             while ptr != None:
#                 print(ptr.data, "->", end=" ")
#                 ptr = ptr.next
#             print("None")
#     def addAtBegin(self):
#         data = int(input("Enter the data : "))
#         newNode = GetNode()
#         newNode.data = data
#         newNode.next = self.head
#         self.head = newNode
#         print(data, "added at beginning")
#     def addAtBetween(self):
#         data = int(input("Enter the data : "))
#         key = int(input("Enter data after inserted : "))
#         newNode = GetNode()
#         newNode.data = data
#         if self.head == None:
#             print("List not present")
#         else:
#             ptr = self.head
#             while ptr != None:
#                 if ptr.data == key:
#                     break
#                 ptr = ptr.next
#             if ptr == None:
#                 print("Key not found")
#             else:
#                 newNode.next = ptr.next
#                 ptr.next = newNode
#                 print(data, "is added")
#     def deleteAtBegin(self):
#         if self.head == None:
#             print("List not present")
#         else:
#             ptr = self.head
#             self.head = ptr.next
#             ptr.next = None
#             print(ptr.data, "is deleted")
#     def deleteAtEnd(self):
#         if self.head == None:
#             print("List not present")
#         elif self.head.next == None:
#             print(self.head.data, "is deleted")
#             self.head = None
#         else:
#             ptr = self.head
#             while ptr.next.next != None:
#                 ptr = ptr.next
#             print(ptr.next.data, "is deleted")
#             ptr.next = None

# if __name__ == '__main__':
#     obj = LinkedList()
#     while True:
#         print("\n1. Append")
#         print("2. Traverse")
#         print("3. Add at Begin")
#         print("4. Add at Between")
#         print("5. Delete at Begin")
#         print("6. Delete at End")
#         print("0. Exit")
#         n = int(input("Select any choice : "))
#         if n == 1:
#             obj.append()
#         elif n == 2:
#             obj.traverse()
#         elif n == 3:
#             obj.addAtBegin()
#         elif n == 4:
#             obj.addAtBetween()
#         elif n == 5:
#             obj.deleteAtBegin()
#         elif n == 6:
#             obj.deleteAtEnd()
#         elif n == 0:
#             sys.exit()
#         else:
#             print("Invalid Choice")