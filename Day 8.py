# Binary Search Tree
# import sys
# class BST:
#     def __init__(self, key):
#         self.leftChild = None
#         self.data = key
#         self.rightChild = None
#     def insert(self, key):
#         if self.data is None:
#             self.data = key
#             return
#         elif self.data == key:
#             return
#         else:
#             if key < self.data:
#                 if self.leftChild:
#                     self.leftChild.insert(key)
#                 else:
#                     self.leftChild = BST(key)
#             elif key > self.data:
#                 if self.rightChild:
#                     self.rightChild.insert(key)
#                 else:
#                     self.rightChild = BST(key)
#     def preorder(self):
#         if self.data is None:
#             print("Tree is Empty")
#             return
#         print(self.data, end=" -> ")
#         if self.leftChild:
#             self.leftChild.preorder()
#         if self.rightChild:
#             self.rightChild.preorder()
#     def postorder(self):
#         if self.data is None:
#             print("Tree is Empty")
#             return
#         if self.leftChild:
#             self.leftChild.postorder()
#         if self.rightChild:
#             self.rightChild.postorder()
#         print(self.data, end=" -> ")
#     def inorder(self):
#         if self.data is None:
#             print("Tree is Empty")
#             return
#         if self.leftChild:
#             self.leftChild.inorder()
#         print(self.data, end=" -> ")
#         if self.rightChild:
#             self.rightChild.inorder()

# if __name__ == "__main__":
#     root = BST(None)
#     while True:
#         print("\n1.Insert")
#         print("2.Preorder")
#         print("3.Postorder")
#         print("4.Inorder")
#         print("0.Exit")
#         n = int(input("Select your choice : "))
#         if n == 1:
#             arr = [36, 26, 46, 21, 31, 11, 24, 41, 56, 51, 66]
#             for i in range(len(arr)):
#                 root.insert(arr[i])
#             print("Nodes Inserted")
#         elif n == 2:
#             root.preorder()
#             print()
#         elif n == 3:
#             root.postorder()
#             print()
#         elif n == 4:
#             root.inorder()
#             print()
#         elif n == 0:
#             sys.exit(0)



# Binary Search Tree with Search function
# import sys
# class BST:
#     def __init__(self, key):
#         self.leftChild = None
#         self.data = key
#         self.rightChild = None
#     def insert(self, key):
#         if self.data is None:
#             self.data = key
#             return
#         elif self.data == key:
#             return
#         else:
#             if key < self.data:
#                 if self.leftChild:
#                     self.leftChild.insert(key)
#                 else:
#                     self.leftChild = BST(key)
#             elif key > self.data:
#                 if self.rightChild:
#                     self.rightChild.insert(key)
#                 else:
#                     self.rightChild = BST(key)
#     def search(self, key):
#         if self.data == key:
#             print(key, "Found")
#             return
#         if key < self.data:
#             if self.leftChild:
#                 self.leftChild.search(key)
#             else:
#                 print(key, "Not Found")
#         else:
#             if self.rightChild:
#                 self.rightChild.search(key)
#             else:
#                 print(key, "Not Found")
#     def preorder(self):
#         if self.data is None:
#             print("Tree is Empty")
#             return
#         print(self.data, end=" -> ")
#         if self.leftChild:
#             self.leftChild.preorder()
#         if self.rightChild:
#             self.rightChild.preorder()
#     def postorder(self):
#         if self.data is None:
#             print("Tree is Empty")
#             return
#         if self.leftChild:
#             self.leftChild.postorder()
#         if self.rightChild:
#             self.rightChild.postorder()
#         print(self.data, end=" -> ")
#     def inorder(self):
#         if self.data is None:
#             print("Tree is Empty")
#             return
#         if self.leftChild:
#             self.leftChild.inorder()
#         print(self.data, end=" -> ")
#         if self.rightChild:
#             self.rightChild.inorder()

# if __name__ == "__main__":
#     root = BST(None)
#     while True:
#         print("\n1.Insert")
#         print("2.Preorder")
#         print("3.Postorder")
#         print("4.Inorder")
#         print("5.Search")
#         print("0.Exit")
#         n = int(input("Select your choice : "))
#         if n == 1:
#             arr = [36, 26, 46, 21, 31, 11, 24, 41, 56, 51, 66]
#             for i in range(len(arr)):
#                 root.insert(arr[i])
#             print("Nodes Inserted")
#         elif n == 2:
#             root.preorder()
#             print()
#         elif n == 3:
#             root.postorder()
#             print()
#         elif n == 4:
#             root.inorder()
#         elif n == 5:
#             key = int(input("Enter element to search : "))
#             root.search(key)
#             print()
#         elif n == 0:
#             sys.exit(0)



# Find factorial using recursion
# def fact(n=1):
#     if n == 0 or n == 1:
#         return 1
#     else : 
#         return n * fact(n - 1)
# if __name__ == '__main__':
#     n = 5 
#     res = fact(n)
#     print(res)



# Multiply two number
# def multiply(x, y):
#     if y == 1:
#         return x
#     elif x == 1:
#         return y
#     elif x == 0 or y == 0:
#         return 0
#     else:
#         return x + multiply(x, y - 1)
# print(multiply(5, 4))



# Find power using recursion
# def power(base, exp):
#     if exp == 0:
#         return 1
#     return base * power(base, exp - 1)
# print(power(2,6))



# Find the sum of N numbers using recursion
# def sumN(n):
#     if n == 0:
#         return 0 
#     return n + sumN(n - 1)
# print(sumN(10))



# Fibonacci series
# def fibo(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else :
#         return fibo(n-1)+fibo(n-2)
# n=10
# for x in range(n):
#     print(fibo(x),end=" ")



# Compute the nearest larger number by interchanging digits (TCS)
# Compute the nearest larger number by interchaning its digits updated. Given 2 number a and b findthe samllest number greater the b by interchanging the digits of a and if not possible print -1.
from itertools import permutations
def generate_permutation(a, b):
    number_str = str(a)
    perm = permutations(number_str)
    ans = []
    for i in perm:
        num = int("".join(i))
        if num > b:
            ans.append(num)
    if len(ans) == 0:
        return -1
    return min(ans)
a = int(input("Enter a : "))
b = int(input("Enter b : "))
print(generate_permutation(a, b))