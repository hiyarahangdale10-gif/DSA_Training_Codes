# function is a self contained block of code that performs a specific task
# function is reusable and can be called multiple times in a program

# if__name__ == "__main__":  **main function hota hai jisme hum apne program ka main logic likhte hai aur jab hum program run karte hai to ye function call hota hai


# def add():
#     a = int(input("Enter the first number: "))
#     b = int(input("Enter the second number: "))
#     sum = a + b
#     print("The sum is: ", sum)

# if  __name__ == "__main__":
#     add()


#funtion with parameters
# def add(a,b):
#     a = int(input("Enter the first number: "))
#     b = int(input("Enter the second number: "))
#     sum = a + b
#     print("The sum is: ", sum)

# if  __name__ == "__main__":
#     a = int(input("Enter the first number: "))
#     b = int(input("Enter the second number: "))
#     add(a,b)


# function with return type
# def add(a,b):    
#     sum = a+b
#     return sum

# if  __name__ == "__main__":
#     a = int(input("Enter the first number: "))
#     b = int(input("Enter the second number: "))
#     result = add(a,b)
#     print("The sum is: ", result)


#function with multiple return type
# def add(a,b):    
#     add = a+b
#     sub = a-b
#     mul = a*b
#     return add, sub, mul

# if  __name__ == "__main__":
#     a = int(input("Enter the first number: "))
#     b = int(input("Enter the second number: "))
#     add, sub, mul = add(a,b)
#     print("The sum is: ", add)
#     print("The difference is: ", sub)
#     print("The product is: ", mul)


#linear search
# def liner_search(n, arr, target):
#     flag = False
#     for i in range(n):
#         if arr[i] == target:
#             flag = True
#             print("Element found at index: ", i)
#             break
#     if flag == False:
#         print("Element not found in the array")

# if __name__ == "__main__":
#     n=int(input("Enter  size of array: "))
#     arr=[]
#     for i in range(n):
#         arr.append(int(input("Enter element: ")))
#     target = int(input("Enter no to search: ")) 
#     liner_search(n, arr, target)


#Binary search
# def binary_search(n, arr, target):
#     flag = False
#     low = 0
#     high = n - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] == target:
#             flag = True
#             loc = mid
#             break;
#             print("Element found at index: ", mid)
#             loc = mid
#             while loc > 0 and arr[loc - 1] == target:
#                 loc -= 1
#             print("Element found at index: ", loc)
#             break
#         elif target < arr[mid]:
#             high = mid - 1
#         elif target > arr[mid]:
#             low = mid + 1

#     if flag==True:
#         print("Search successful :", loc)
#     else:
#         print("Search unsuccessful")

# if __name__ == "__main__":
#     n=int(input("Enter  size of array: "))
#     arr=[]
#     for i in range(n):
#         arr.append(int(input("Enter element: ")))
#     target = int(input("Enter no to search: ")) 
#     binary_search(n, arr, target)