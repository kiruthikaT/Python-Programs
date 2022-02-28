print("We have 10 programs please go a head and test with you inputs")
def Even_or_Odd(num):
  if num%2==0:
    print("The given number is Even")
  else:
    print("The given number is Odd")

def Temperature_convertor(degree):
  Farenheit=degree*(9/5) + 32
  print("Farenheit of",degree,"is",Farenheit)

def Product_real_num():
  X=int(input("\n Enter the number of real numbers \t"))
  for i in range(X):
    Y=float(input("\nEnter a real number \t"))
    product=X*Y
    print("The product of number is:",product)

def factorial(n):
    if (n==1 or n==0):
        return 1
    else:
        return (n * factorial(n - 1))

def Linear_Search(arr,x):
  for i in range(len(arr)):
    if arr[i] == x:
      return i
  return 0
    
def Binary_Search(ind,x):
  ind=ind//2
  if int(arr[ind]) == x:
    return ind
  elif int(arr[ind])>x:
    return Binary_Search(ind,x)
  elif int(arr[ind])<x:
    return Binary_Search(ind+l,x)

def Large_num(l):
  max=0
  for i in range(l):
    if max<int(num_list[i]):
      max=int(num_list[i])
  return max

#1) 
print("i) Program to check whether the given number is even or not")
number=int(input("\n Enter a number to check \t"))
Even_or_Odd(number)
print("\n")

#2)
print("ii) Program to convert the temperature in degree centigrade to Fahrenheit.")
Celcius=float(input("\nEnter the degree centegrate value to convert \t"))
Temperature_convertor(Celcius)
print("\n")

#3)
print("iii) Progran to find the product of a set of real numbers.")
Product_real_num()
print("\n")

#4)
print("iv) Program to find the factorial of a number using recursion.")
num=int(input("\nEnter a number \t"))
print("Factorial of the number:",num,"is",factorial(num))
print("\n")

#5)
print("v) Program to implement linear search")
numbers=input("Enter list of integers with space in between\t").split()
check=input("Enter a number to search\t")
result=Linear_Search(numbers,check)
if result == 0:
  print("Element is not present in the list",result)
else:
  print("The element present at the index",result)
print("\n")

#6)
print("vi) Python program to implement binary search.")
arr=input("Enter a list of numbers\t").split(' ')
l=len(arr)
arr=list(map(int,arr))
arr.sort()
print("list of numbers in sorted order",arr)
x=int(input("Enter number to search\t"))
#find middle=low+high/2
if x not in arr:
  print("The element is not present")
else:
  result=Binary_Search(l,x)
  print("The element present at the index",result)
print("\n")

#7)
print("vii) Program to find the largest number in a list")
num_list=input("Enter a list of numbers with space in between\t").split(' ')
l=len(num_list)
result=Large_num(l)
print("The largest number in the list is",result)
print("\n")

#8)
print("viii) Program to delete an element from a list by index.")
gvn_list=input("Enter a list of elements with space in between\t").split(' ')
gvn_element=input("Enter element to delete\t")
ind=gvn_list.index(gvn_element)
gvn_list.pop(ind)
result=' '.join([str(elem) for elem in gvn_list])
print("The final list after deletion of an element",result)
print("\n") 

#9)
print("ix) Program to print all the items in a dictionary.")
strs=int(input("Enter the number of keys & values\t"))
class_list = {}
for i in range(strs):
    key=input("Enter Key\t")
    value=input("Enter Value\t")
    class_list[key]=value
print("(Key,Values) in dictionary")
for i in class_list.items():
    print(i)
print("\n") 

#10)
print("x) Proogram to find the average of 10 numbers using while loop.")
numbers=input("Enter 10 numbers with space in between\t").split(' ')
l=list(map(int,numbers))
length=len(l)
i,sum=0,0
while i!=(length):
    sum+=l[i]
    i+=1
avg=sum/length
print("The average of the given 10 numbers is",avg)

print("THANK YOU !!!")
