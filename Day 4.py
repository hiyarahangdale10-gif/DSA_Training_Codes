# Arranging the given numbers in ascending or descending order is called sorting

# Bubble Sort (ascending order) 
# def bubble_sort(arr):
#     for i in range(len(arr)):  
#         for j in range(len(arr) - 1 - i):
#             if arr[j] > arr[j + 1]:  
#                 arr[j], arr[j + 1] = arr[j + 1], arr [j]

# if __name__ == "__main__":
#     arr = [5, 2, 9, 1, 5, 6]
#     bubble_sort(arr)
#     print(*arr)



# Bubble Sort (ascending order) 
# def bubble_sort(arr):
#     for i in range(len(arr)):  
#         for j in range(len(arr) - 1 - i):
#             if arr[j] < arr[j + 1]:  
#                 arr[j], arr[j + 1] = arr[j + 1], arr [j]

# if __name__ == "__main__":
#     arr = [5, 2, 9, 1, 5, 6]
#     bubble_sort(arr)
#     print(*arr)



# Selection Sort 
# def selectionSort(arr):
#     n = len(arr)
#     for i in range(n):
#         loc = i
#         for j in range(i + 1, n):
#             if arr[j] < arr[loc]:
#                 loc = j
#         arr[i], arr[loc] = arr[loc], arr [i]

# if __name__ == '__main__':
#     arr = [5, 2, 9, 1, 5, 6]
#     selectionSort(arr)
#     print(*arr)
#     print(arr)


# Selection Sort (descending order)
# def selectionSort(arr):
#     min = 0
#     loc = 0
#     for i in range(len(arr)-1):
#         min = arr[i]
#         loc = i
#         for j in range(i + 1, len(arr)):
#             if arr[j] > min:
#                 min = arr[j]
#                 loc = j
#         arr[i], arr[loc] = arr[loc], arr [i]

# if __name__ == '__main__':
#     arr = [5, 2, 9, 1, 5, 6]
#     selectionSort(arr)
#     print(*arr)
#     print(arr)


# Insertion sort (ascending order)
# arr =  [5, 2, 9, 1, 5, 6]
# def insertion_sort(arr):
#     for i in range (1, len(arr)):
#         current = arr[i]
#         pos = i
#         while current < arr[pos - 1] and pos > 0:
#             arr[pos] = arr[pos - 1]
#             pos -= 1
#         arr[pos] = current

# if __name__ == "__main__":
#     insertion_sort(arr)
#     print(*arr)


# *********************************Class************************************

# class Student:
#     def show (self):
#         print("This is a student class")
# s = Student()
# s.show() 

# class Student:
#     def __init__(self):
#         print("This is a class")

#     def show(self):
#         print("This is a student class")

# s = Student()
# s.show()



# Stack implementation using class
# import sys
# class stack:
#     def push(self):
#         pass
#     def pop(self):
#         pass
#     def traverse(self):
#         pass
#     def peek(self):
#         pass

# if __name__ == "__main__":
#     obj = stack()
#     while True:
#         print("1. Push")
#         print("2. Pop")
#         print("3. Traverse")
#         print("4. Peek")
#         print("5. Exit")
#         ch = int(input("Enter your choice: "))
#         if ch == 1:
#             obj.push()
#         elif ch == 2:
#             obj.pop()
#         elif ch == 3:
#             obj.traverse()
#         elif ch == 4:
#             obj.peek()
#         elif ch == 5:
#             sys.exit() 



# Push, Pop, Traverse, Peek operations of stack using class
# import sys
# class Stack:
#     def __init__(self):
#         self.stack = []
#         self.top = -1
#         self.capacity = 5
#     def isFull(self):
#         if self.top == self.capacity - 1:
#             return True
#         else:
#             return False
#     def isEmpty(self):
#         if self.top == -1:
#             return True
#         else:
#             return False
#     def push(self, ele):
#         if self.isFull():
#             print("Stack is full")
#         else:
#             self.top += 1
#             self.stack.append(ele)
#             print(ele, "is pushed")
#     def pop(self):
#         if self.isEmpty():
#             print("Stack is empty")
#         else:
#             ele = self.stack.pop()
#             self.top -= 1
#             print(ele, "is popped")
#     def peek(self):
#         if self.isEmpty():
#             print("Stack is empty")
#         else:
#             print("Top element is:", self.stack[self.top])
#     def traverse(self):
#         if self.isEmpty():
#             print("Stack is empty")
#         else:
#             print("Stack elements are:")
#             for i in range(self.top, -1, -1):
#                 print(self.stack[i])

# if __name__ == "__main__":
#     obj = Stack()
#     while True:
#         print("\n1. Push")
#         print("2. Pop")
#         print("3. Traverse")
#         print("4. Peek")
#         print("5. Exit")
#         ch = int(input("Enter your choice: "))
#         if ch == 1:
#             ele = int(input("Enter the element to push: "))
#             obj.push(ele)
#         elif ch == 2:
#             obj.pop()
#         elif ch == 3:
#             obj.traverse()
#         elif ch == 4:
#             obj.peek()
#         elif ch == 5:
#             sys.exit()
#         else:
#             print("Invalid choice")



# without size limit of stack
# import sys
# class Stack:
#     def __init__(self):
#         self.stack = []
#     def isEmpty(self):
#         return len(self.stack) == 0
#     def push(self, ele):
#         self.stack.append(ele)
#         print(ele, "is pushed")
#     def pop(self):
#         if self.isEmpty():
#             print("Stack is empty")
#         else:
#             ele = self.stack.pop()
#             print(ele, "is popped")
#     def peek(self):
#         if self.isEmpty():
#             print("Stack is empty")
#         else:
#             print("Top element is:", self.stack[-1])
#     def traverse(self):
#         if self.isEmpty():
#             print("Stack is empty")
#         else:
#             print("Stack elements are:")
#             for i in range(len(self.stack) - 1, -1, -1):
#                 print(self.stack[i])

# if __name__ == "__main__":
#     obj = Stack()
#     while True:
#         print("\n1. Push")
#         print("2. Pop")
#         print("3. Traverse")
#         print("4. Peek")
#         print("5. Exit")

#         ch = int(input("Enter your choice: "))
#         if ch == 1:
#             ele = int(input("Enter element to push: "))
#             obj.push(ele)
#         elif ch == 2:
#             obj.pop()
#         elif ch == 3:
#             obj.traverse()
#         elif ch == 4:
#             obj.peek()
#         elif ch == 5:
#             sys.exit()
#         else:
#             print("Invalid choice")


# reverse the stack
# import sys
# class Stack:
#     def __init__(self):
#         self.stack = []
#         self.top = -1
#         self.capacity = 5
#     def isFull(self):
#         if self.top == self.capacity - 1:
#             return True
#         else:
#             return False
#     def isEmpty(self):
#         if self.top == -1:
#             return True
#         else:
#             return False
#     def push(self, ele):
#         if self.isFull():
#             print("Stack is full")
#         else:
#             self.top += 1
#             self.stack.append(ele)
#             print(ele, "is pushed")
#     def pop(self):
#         if self.isEmpty():
#             print("Stack is empty")
#         else:
#             ele = self.stack.pop()
#             self.top -= 1
#             print(ele, "is popped")
#     def peek(self):
#         if self.isEmpty():
#             print("Stack is empty")
#         else:
#             print("Top element is:", self.stack[self.top])
#     def traverse(self):
#         if self.isEmpty():
#             print("Stack is empty")
#         else:
#             print("Stack elements are:")
#             for i in range(self.top, -1, -1):
#                 print(self.stack[i])

# if __name__ == "__main__":
#     obj = Stack()
#     arr = [1234, 153, 370, 371, 407]
#     for i in range(len(arr)):
#         obj.push(arr[i])
#     for i in range(len(arr)):
#             print(obj.pop())



