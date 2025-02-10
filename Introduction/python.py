# use of " " and ' ' 
#for development ->json format, also to include " and ' in string
#python iss type insensitive (not declaring datatype).so payment gateway never use python

#take name and birth year as input and print you are this years old
# name=input('name')
# year = int(input('year'))
# print(f'{name}, you are {2024-year} years old')

#BODMAS -> bracket, of(expo),div,mul,add,sub
#PEMDAS  -> parenthesis,exponen,multi, div,add,sub

#input no, print square root and cube root of it
# number =int(input())
# cube = number ** (1/3)
# print("perfect" if(round(number**(1/3))**3 ==number) else("not perfect"))
# if(round(cube)**3 == number):
#     print("perfect")
# else:
#     print("not perfect")
# print(number ** 0.5)
# print(number ** (1/3))
# print()

# n = int(input())
# sum=[]
# sum =[num for i in range(2) num=n%10 ]

# while n>0:
#     temp = n%10
#     sum +=temp
#     n //= 10
# print(sum)
# if(sum%2 ==0):
#     print((sum%10)**(1/3))
# else:

#take 3 digit number and check whether the numebr is divible by 3 or not

#print("divisible" if sum(list(map(int,input()))) %3 ==0 else "not divisible") 

#take 4 digit number ,substract sum of alternate digits from each other 3456 ->8-10=2
# a=int(input())
# num1 = a%10 + a//100%10
# num2 = a//10%10 +a //1000
# print(num1-num2)

# print(True and False or True) #and has higherpriority
# print(100 or False) #output 100
# print(True+True and False) #2 and false =false

#sphere radius =50cm can it hold 3 litre water
# vol = (4/3) *3.14*(50**3)
# if vol >= 3000:
#     print("yes ")
# else:
#     print('no')
# print(f'{(vol):.3f}') # :.3f gives 3 digits after decimal
# print(f'{(22/7):.10f}')

# while True:
#     print('hello')

# n=int(input())
# sum1=0
# while n:
#     sum1 +=n
#     n -=1
# print(sum1)

# n1=int(input())
# fact=1
# while n:
#     fact *=n
#     n -=1
# print(fact) 

#print number of digits and also sum of digits

# num =int(input())
# count=temp=sum1=0
# while num:
#     temp =num%10
#     sum1 +=temp
#     num //=10
#     count +=1
# print(f'sum is {sum1} and count is {count}')

# n1=int(input())
# while n1:
#     temp =n1 % 10
#     fact=1
#     while temp:
#         fact *=temp
#         temp -=1
#     print(fact)
#     n1 //=10

#check if a number is armstrong or not
# n=int(input())
# number=n
# num = n
# sum=count=0
# while num:
#     temp = n%10
#     count +=1
#     num //=10

# while n:
#     temp = n%10
#     sum +=temp**count
#     n //= 10
# print("armstrong" if sum == number else "not armstrong")


#check if a number is strong number
# n=int(input())
# number=n
# sum=0
# while n:
#     temp = n%10
#     fact =1
#     while temp:
#         fact *=temp
#         temp -=1
#     sum +=fact
#     n //=10
# print("strong" if sum == number else "not strong")

#prime number
# def checkPrime(e):
#     i=2
#     while(i<e):
#         if(e%i==0):
#             print('not prime')
#             break
#         i+=1
#     else:
#         print('it is prime')
# n = int(input())
# checkPrime(n)

#reverse a number using while loop
# n = int(input())
# rever=0
# while n:
#     temp = n%10
#     rever = rever*10 +temp
#     n //=10
# print(rever)
# print(input()[::-1]) #easily revrese in single line

#print('*'*i for i in range(5))

# n=int(input())
# i=1
# while(i<n*2):
#     if(i>n):
#         print((' '*(i-n) + '* '*(2*n -i)).rstrip())
#     else:
#         print((' '*(n-i) +'* '*i).rstrip())
#     i+=1

# #deimal to binary
# num =13
# a=''
# while num:
#     a=str(num%2) +a #continuosly dividing by 2 and attaching
#     num //=2
# print(a)

#binary to decimal
# num =1101
# count=0
# sum=0
# while num>0:
#     if(num %10 ==1):
#         sum = sum + 2**count # 1**3 + 1**2 + 0**1 + 1**0
#     num =num // 10
#     count+=1
# print(sum)

# n=None
# while n!='python':
#     n=input("enter the string")

#hcf
num1,num2 =24,36
a=2
gcd=0
while(a<num1):
    if num1 % a==0 and num2 % a==0 :
        gcd = a
    a +=1
print(gcd)

   





