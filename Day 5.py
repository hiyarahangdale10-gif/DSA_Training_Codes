# Queue implementation using list
# import sys
# class Queue:
#     def __init__(self):
#         self.queue=[]
#         self.rear=-1
#         self.front=0
#         self.CAPACITY=5

#     def isFull(self):
#         if self.rear==self.CAPACITY-1:
#             return True
#         else:
#             return False

#     def insert(self,ele):
#         pass

#     def traverse(self):
#         pass

#     def isEmpty(self):
#         if self.rear==-1:
#             return True
#         else:
#             return False

#     def delete(self):
#         pass
        
    
#     def peek(self):
#         pass

# if __name__ == '__main__':
#     obj=Queue()
#     while True:
#         print("1. Insert")
#         print("2. Delete")
#         print("3. Peek")
#         print("4. Traverse")
#         print("0. Exit")
#         ch=int(input("Select any choice :"))
#         if ch==1:
#             ele=int(input("Enter data: "))
#             obj.insert(ele)
#         elif ch==2:
#             obj.delete()
#         elif ch==3:
#             obj.peek()
#         elif ch==4:
#             obj.traverse()
#         elif ch==0:
#             sys.exit(0)



# import sys
# class Queue:
#     def __init__(self):
#         self.queue=[]
#         self.rear=-1
#         self.front=0
#         self.CAPACITY=5

#     def isFull(self):
#         if self.rear==self.CAPACITY-1:
#             return True
#         else:
#             return False

#     def insert(self,ele):
#         if self.isFull():
#             print("Queue is full")
#         else:
#             self.queue.append(ele)
#             self.rear+=1

#     def traverse(self):
#         if not self.isEmpty():
#             print("Queue elements:")
#             for i in range(self.front, self.rear+1):
#                 print(self.queue[i], end=" ")
#             print()
#         else:
#             print("Queue is empty")

#     def isEmpty(self):
#         if self.rear==-1:
#             return True
#         else:
#             return False

#     def delete(self):
#         if self.isEmpty():
#             print("Queue is empty")
#         else:
#             ele=self.queue[self.front]
#             for i in range(1 ,self.rear + 1):
#                 self.queue[i]=self.queue[i-1]
#             self.rear-=1
#             print(ele, "is deleted")
#     def peek(self):
#         if not self.isEmpty():
#             print("Front element:", self.queue[self.front])
#         else:
#             print("Queue is empty")

# if __name__ == '__main__':
#     obj=Queue()
#     while True:
#         print("1. Insert")
#         print("2. Delete")
#         print("3. Peek")
#         print("4. Traverse")
#         print("0. Exit")
#         ch=int(input("Select any choice :"))
#         if ch==1:
#             ele=int(input("Enter data: "))
#             obj.insert(ele)
#         elif ch==2:
#             obj.delete()
#         elif ch==3:
#             obj.peek()
#         elif ch==4:
#             obj.traverse()
#         elif ch==0:
#             sys.exit(0)



# import sys
# class Queue:
#     def __init__(self):
#         self.queue = []
#         self.rear = -1
#         self.front = 0
#         self.CAPACITY = 5
#     def isFull(self):
#         return self.rear == self.CAPACITY - 1
#     def isEmpty(self):
#         return self.rear == -1
#     def insert(self, ele):
#         if self.isFull():
#             print("Queue is full")
#         else:
#             self.queue.append(ele)
#             self.rear += 1
#             print(ele, "inserted into queue")
#     def delete(self):
#         if self.isEmpty():
#             print("Queue is empty")
#         else:
#             ele = self.queue.pop(0)
#             self.rear -= 1
#             return ele
#     def traverse(self):
#         if self.isEmpty():
#             print("Queue is empty")
#         else:
#             print("Queue elements:")
#             for i in range(self.front, self.rear + 1):
#                 print(self.queue[i], end=" ")
#             print()

# class Stack:
#     def __init__(self):
#         self.stack = []
#         self.top = -1
#         self.capacity = 5
#     def isFull(self):
#         return self.top == self.capacity - 1
#     def isEmpty(self):
#         return self.top == -1
#     def push(self, ele):
#         if self.isFull():
#             print("Stack is full")
#         else:
#             self.stack.append(ele)
#             self.top += 1
#             print(ele, "pushed into stack")
#     def pop(self):
#         if self.isEmpty():
#             print("Stack is empty")
#         else:
#             ele = self.stack.pop()
#             self.top -= 1
#             return ele

# if __name__ == '__main__':
#     q = Queue()
#     s = Stack()
#     n = int(input("Enter no of element :"))
#     for i in range (n):
#         ele = int (input ("Enter element : "))
#         q.insert(ele)
#     for x in range(n):
#         ele = q.delete()
#         s.push(ele)
#     for x in range(n):
#         ele = s.pop()
#         q.insert(ele)
#     q.traverse()


#  Insert element in the array
# arr = [1,2,3,4,5]
# key = 22
# loc = 3
# arr.append(0)
# print(arr)
# for i in range (len(arr)-1,loc,-1):
#     arr[i]=arr[i-1]
# arr[loc]=key
# print(arr)


# Delete key element from array
# arr = [1, 2, 3, 4, 5] 
# loc = 3 
# print(*arr)
# for i in range(loc+1,len(arr)):
#     arr[i-1] = arr[i]
# arr.pop()
# print(arr)



#Question : Rotate an array to the right by a given number of step  
# arr = [1, 2, 3, 4, 5]
# k=1
# for i in range (k):
#     temp = arr[-1]
#     for i in range (len(arr)-1,0,-1):
#         arr[i]=arr[i-1]
#     arr[0]=temp
# print(arr)



# Question : Find the intersection of two arrays and find the common element in the second array
# arr1 = [1, 2, 2, 1]
# arr2 = [2, 2]
# intersection = []
# for num in arr1:
#     if num in arr2:
#         intersection.append(num)
#         arr2.remove(num)
# print("Intersection:", intersection)



# Rearrange positive and negative numbers:
# Question :Given an array containing both positive and negetive numbers,rearrange then in an alternating fashion 
# arr = [-1, 2, -3, 4, 5, -6]
# neg = []
# pos = []
# for num in arr:
#     if num < 0:
#         neg.append(num)
#     else:
#         pos.append(num)
# ans = []
# for i in range(len(neg)):
#     ans.append(neg[i])
#     ans.append(pos[i])
# print(ans)



# Reverse the string without inbuild function & shortcut
# Expected logic 1 :
# s = "Hello Hiya" 
# rev = ""
# for x in s:
#     rev = x + rev
# print(rev)

# Expected logic 3 :
# arr = "Hello Hiya"
# reversed_arr = ""
# for i in range(len(arr) - 1, -1, -1):
#     reversed_arr += arr[i]
# print(reversed_arr)



# Question : Write a program to check id a give string is a valid palidromic string after ignoring non-alphanumeric characters and considering case.
#logic : use loops to compare characters while ignoring non-alphanumeric characters.

# s = "A man, a plan, a canal: Panama" 
# str = ""
# for x in s:
#     if x.isalpha():
#         str = str + x
# print(str)
# str = str.lower()
# print(str)
# rev = str [::-1]
# if rev == str:
#     print("String is a Palindrom")
# else:
#     print("String is not a Palindrom")



# Program to check if two string are anagrams of each other
# Check if the character conuts in both strings are the same 

# s1 = "listen"
# s2 = "silent"
# is_anagram = True
# if len(s1) != len(s2):
#     is_anagram = False
# else:
#     for char in s1:
#         count_s1 = 0
#         for i in s1:
#             if i == char:
#                 count_s1 += 1
#     for char in s1:
#         count_s1 = 0
#         for i in s1:
#             if i == char:
#                 count_s1 += 1
#         count_s2 = 0
#         for j in s2:
#             if j == char:
#                 count_s2 += 1
#         if count_s1 != count_s2:
#             is_anagram = False
#             break
# if is_anagram:
#     print(f"'{s1}' and '{s2}' are anagrams.")
# else:
#     print(f"'{s1}' and '{s2}' are NOT anagrams.")



# HOMEWORK 

# Check for Pangram
# str = "The quick brown fox jumps over the lazy dog.".lower()
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# flag = True
# for ch in alphabet:
#     if ch not in str:
#         flag = False
#         break
# if flag:
#     print("Pangram")
# else:
#     print("Not Pangram")



# Remove White Spaces
# str = "hello world"
# result = ""
# for ch in str:
#     if ch != " ":
#         result = result + ch
# print(result)



# Count Words in a String
# str = "This is a sentence."
# count = 1
# for ch in str:
#     if ch == " ":
#         count += 1
# print(count)



# Merge Two Sorted Lists
# list1 = [1, 3, 5]
# list2 = [2, 4, 6]
# result = list1 + list2
# result.sort()
# print(result)