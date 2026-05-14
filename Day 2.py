# arr = [1,2,3],[4,5,6],[7,8,9]
# # print (arr)
# # for i in range (len(arr)):
# #   print (arr[i])

# for i in range (len(arr)):
#  for j in range (len(arr[i])):
#   print (arr[i][j],end=" ")
# print()

# s={1,2,5,6,4,3,2,4,6}
# print (s)

# arr= [1,2,5,6,4,3,2,4,6]
# s= set(arr)
# arr= list(s)
# print (arr) 

# n= int(input("Enter the size : "))
# arr=[]
# even =  0
# odd = 0
# even1 =  0
# odd1 = 0

# for i in range(n):
#  element=int(input("Enter number : "))
#  arr.append(element)
    
# for i in range(len(arr)):
#  if arr[i] % 2 == 0:
#   even += arr[i]
#   even1 += 1
#  else:
#   odd += arr[i]
#   odd1 += 1
# print("Sum of even numbers:", even)
# print("Sum of odd numbers:", odd)
# print("Count of even numbers:", even1)
# print("Count of odd numbers:", odd1)



# no=2025
# save=no
# count=0
# while no > 0:
#     no=no//10
#     count += 1
# no=save
# if count % 2 == 0:
#   mid=count//2
#   no1=no//10**mid
#   no2=no%10**mid
#   sum=no1+no2
#   sq=sum*sum
    


# if sq == no:
#  print ("True,This is a Tech number ")
# else:
#  print ("False,This is not a Tech number ")



#for this pattern 
#     j=1 j=2 j=3 j=4
# i=1 1   1   1   1
# i=2 2   2   2   2
# i=3 3   3   3   3
# i=4 4   4   4   4

# for i in range(1,5):
#     for j in range(1,5):
#         print(i,end=" ")
#     print()



# n=1
# for i in range(1,5):
#     for j in range(1,5):
#         print(n,end=" ")
#         n=n+1
#     print()



# n=65
# for i in range(1,5):
#     for j in range(1,5):
#         print(chr(n),end=" ")
#         n=n+1
#     print()



# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()



# for i in range(4,0,-1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()



# sp=0
# for i in range(4,0,-1):
#     for x in range(sp):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
#     sp += 1



# s = " Hiya is the most beautiful with there heart and looks too "
# print(s.find("with")) 
# print(s.find("h"))
# print(s.rfind("o"))



# s= "abcabcbabcbabcbabcbabcdd"
# print(s.count("a"))
# print(s.count("ab"))
# print(s.count("a",3,10))



# s = ("Hiya Rahangdale")
# print(s.replace("Rahangdale","Beautiful"))
# print(s)



# s = " Hiya is the most beautiful with there heart and looks too "
# ls= s.split()
# print(ls)



# l = ['Hiya', 'Rahangdale']
# s = '*'.join(l)
# print(s)



# s = "Hiya is the most beautiful with there heart and looks too"
# ls= s.split()
# for i in range(len(ls)):
#     print(ls[i][::-1],end=" ")



# s = "ABDCDAEDRFHJGCVACFDCASDC"
# ans = ""
# for i in s:
#     if i not in ans:
#         ans = ans + i
# print(ans)



# num = input("Enter mobile number: ")
# if len(num) == 10 and num.isdigit() and num[0] in ['6', '7', '8', '9']:
#     print("Valid Indian mobile number")
# else:
#     print("Invalid number")



# num = input("Enter mobile number: ")
# if num.isdigit():
#     if len(num)==10:
#         if num.startswith(('6', '7', '8', '9')):
#             print("Valid Indian mobile number")
#         else:
#             print("Invalid number")



# d={}
# d[100]= "Hiya"
# d[200]= "Rahangdale"
# print (d)


# rec={}
# n = int(input("Enter the number of students: "))
# for i in range(n):
#     name = input("Enter the name of student: ")
#     marks = int(input("Enter the marks of student: "))
#     rec[name] = marks
# print(rec)

# print (rec)
# for x in rec:
#     print (x,"\t",rec[x])



