#Question 1 - if else ladder
# per = 75
# if per>=40 and per>=60:
#     print ("Take admission in ABC college")
# elif per>=61 and per>=80:
#     print ("Take admission in XYZ college")
# elif per>=81 and per>=100:
#     print ("Take admission in PQR college")



#Question 2 - for finding the ,Cost price ,discount
# cp = int (input("Enter the Cost Price: "))
# s = input("Are you a student? (yes/no): ")
# if s=="yes" :
#     if cp>=500:
#         print ("You get a 10% discount. The final price is: ", cp*0.10)
#     else:
#         print ("You get a 10% discount. The final price is: ", cp*0.05)
# else :
#     if s=="no" and cp>=500:
#         print ("You get a 8% discount. The final price is: ", cp*0.08)
#     else :
#         print ("You get a 2% discount. The final price is: ", cp*0.02)
# print ("cost price is: ", cp)
# print ("Total discount is: ", cp*0.10 + cp*0.08)
# print ("Net price is: ", cp - (cp*0.10 + cp*0.08))
# arr = [10, 20, 30, 40, 50]
# for  x in arr:
#     print (x)



#Question 3 for print this pattern 
# 1  10
# 2  9
# 4  7
# 5  6 

# i = 1
# j = 10
# while i < j:
#     if i == 3:
#         i += 1
#         j -= 1
#         continue
#     print(i, j)
#     i += 1
#     j -= 1
# Is = []
# print (type(Is))



# arr = [11, 22, 33, 44, 55]
# print (arr)
# for i in range (len(arr)):
#     print (arr[i], end=" ")
# print()
# for x in arr:
#     print (x, end=" ")



# Accesing the list 
# arr = [11, 22, 33, 44, 55]
# print (arr[-1])



#slicing the list
# arr = [11, 22, 33, 44, 55]
# print (arr[1:5])
# print (arr[4:6])
# print (arr[:6])
# print (arr[4:])
# print (arr[:])
# print (arr[::1])
# print (arr[::2])
# print (arr[::-1])  



#Question 1 - find max and min number
# arr = [5,3,9,2,8]
# max = arr[0]
# for i in range (1,len(arr)):
#     if arr[i] > max:
#         max = arr[i]    
# print ("The maximum number is: ", max)
# min = arr[0]
# for i in range (1, len(arr)):
#     if arr[i] < min:
#         min = arr[i]    
# print ("The minimum number is: ", min)



#Question 2 - Remove the duplicate number from the list
# arr = [3,2,3,1,2,4]
# ans = []
# for i in arr:
#     if i not in ans:
#         ans.append(i) 
# print (ans)



#Find the nuumber is palindrome or not(without user input) **for loop**
# for i in range(1, 1001):
#     num = i
#     sum = 0
#     save = num
#     count = 0
#     while num > 0:
#         num = num // 10
#         count = count + 1
#     num = save
#     while num > 0:
#         rem = num % 10
#         sum = sum + (rem ** count)
#         num = num // 10        
#     if sum == save:
#         print("The number is a palindrome : ", save)



#Find the nuumber is palindrome or not(with user input)
# num = int(input("Enter a number: "))
# sum = 0
# save = num
# count = 0

# while num > 0:
#     num = num // 10
#     count = count + 1
# num = save

# while num > 0:
#     rem = num % 10
#     sum = sum + (rem ** count)
#     num = num // 10
            
#     if sum == save:
#         print("The number is a palindrome : ", save)
#     else:        
#         print("The number is not a palindrome")



#Find the number is a Peterson number or not
# num = int(input("Enter a number: "))
# sum = 0
# save = num

# while num > 0:
#     rem = num % 10
#     fact = 1
#     while rem > 0:
#         fact = fact * rem
#         rem = rem - 1

#     sum = sum + fact
#     num = num // 10

# if save == sum:
#     print("The number is a Peterson number:", save)
# else:
#     print("The number is not a Peterson number")