# name='jennifer'
# print(name[2:9-4+2])
# #print niqu letter in string
# vow="aeiou"
# stri=""
# for i in name:
#     if i not in vow:
#         print(i)
# for i in range(len(name)):
#     if name[i] not in vow:
#         stri +=name[i]
#     else:
#         stri+=name[i]*(i+1)
# print(stri)

# name ="jenniiffeeren"
# vow = "aeiou"
# emp = ""
# w = ""
# for i in name:
#     if i in vow:
#         emp+=i
#         num = emp.count(i)
#         if(num==1):
#             w+='#'
#         elif(num==2):
#             w+='*'
#         elif(num==3):
#             w+='@'
#         else:
#             w+=i
#     else:
#         w+=i

# print(w)
# #--------------------------------------------------------------------
# st ='HpasKtY'
# print(st.swapcase())

# print(st.replace('p','*',1)) # 1 means only 1st occurence

# print(st.find('z'))
# print(st.index('p'))
# print(st.startswith('Hpa')) #returns true or false if string is present
# st ="980"
# print(st.isdigit())
# print(st.isnumeric())


# #-----------------------------------------------------------------------
# n=""
# while(not (n.isdigit() or n.isalpha() or n.isalnum())):
#     n = input('enter string')

# num1=int(input())
# num2=int(input())
# if(num1==1 or num1==0 or num1==2):
#     print(2)
#     num1=3
# for i in range(num1,num2):
#     j=2
#     while(j<i):
#         if i % j ==0:
#             break
#         j +=1
#     else:
#         print(i)

# n=input()
# lowcount=upcount=0
# low =[]
# up =[]
# for i,value in enumerate(n):
#     if value.islower():
#         lowcount+=1
#         low.append(i)
#     elif value.isupper():
#         upcount+=1
#         up.append(i)
# print(f'{lowcount} lower letters are present at {low}\n {upcount} capital letters are present at {up}')


#find first non repeating character
# def checkFirstOcuurence(n):
#     dict_values ={}
    
#     for char in n:
#         dict_values[char]=dict_values.get(char,0)+1
#     for char in n:
#         if dict_values[char] == 1:
#             return char
#     return None

# inp =input()
# result = checkFirstOcuurence(inp)
# print("No unique element" if result == None else result)

#map() function
# numbers = [1, 2, 3, 4, 5]
# doubled_numbers = list(map(lambda x: x * 2, numbers))
# print(doubled_numbers)

# #filter() function
# numbers = [1, 2, 3, 4, 5]
# odds = list(filter(lambda x: x % 2 != 0, numbers))
# print(odds)

# #reduce() function
# from functools import reduce
# numbers = [1, 2, 3, 4, 5]
# total = reduce(lambda x, y: x + y, numbers)
# print(total)

# from functools import reduce
# numbers = [1, 7, 3, 9, 5]
# max_number = reduce(lambda x, y: x if x > y else y, numbers)
# print(max_number)

# import numpy as np
# import pandas as pd
# list1 =[1,'string',np.arange(10),pd.Series(),1]
# print(np.arange(10))
# list1.remove(1)
# print(list1)

# def rotate(list1,n):
#     for i in range(n):
#         last = list1[len(list1)-1]
#         for j in range(len(list1)-1,0,-1):
#             list1[j] = list1[j-1]
#         list1[0]=last
#     return list1
# sam_list= list(map(int,input("enter list").split(' ')))
# n=int(input('enter rotation'))

# def rotate1(list1,n):
#     effective_rot = n % len(list1)
#     for i in range(effective_rot):
#         poped = list1.pop()
#         list1 = [poped] + list1
#     return list1

# result = rotate1(sam_list,n)
# print(result)

# def checkPalindrome(n):
#     left =0
#     for right in range(len(n)-1,-1,-1):
#         if(left == right):
#             return True
#         elif(n[left]== n[right]):
#             left+=1
#             right -=1
#         else:
#             return False
        

# print("yes" if checkPalindrome(input()) else "No")

# def checkBracket(s):
#     stack = []  # Using a list as a stack
#     top = -1  # Custom pointer to track the top of the stack

#     for char in s:
#         if char in "({[":
#             top += 1  # Move top pointer
#             if top < len(stack):
#                 stack[top] = char  # Reuse space
#             else:
#                 stack.append(char)  # Push to stack
#         else:
#             if top == -1:  # No matching opening bracket
#                 return False
            
#             # Manually check top of the stack
#             top_char = stack[top]
#             if (char == ')' and top_char != '(') or \
#                (char == '}' and top_char != '{') or \
#                (char == ']' and top_char != '['):
#                 return False  # Mismatch
            
#             top -= 1  # Remove top element (manual pop)

#     return top == -1
# result = checkBracket(input())
# print(result)

# def merge(l1,l2):
#     sample= []
#     left =0
#     l1 =l1+l2
#     for x in l2:

#print for albhabets from numbers
# def get_letter_combinations(s, index, current, result):
#     if index == len(s):  # Base case: Reached end of string
#         result.append("".join(current))
#         return

#     # Consider 1-digit number (s[index])
#     num1 = int(s[index])
#     if 1 <= num1 <= 26:  # Ensure valid mapping
#         current.append(chr(num1 + ord('A') - 1))
#         get_letter_combinations(s, index + 1, current, result)
#         current.pop()  # Backtrack

#     # Consider 2-digit number (s[index:index+2]) if possible
#     if index + 1 < len(s):
#         num2 = int(s[index:index+2])
#         if 1 <= num2 <= 26:
#             current.append(chr(num2 + ord('A') - 1))
#             get_letter_combinations(s, index + 2, current, result)
#             current.pop()  # Backtrack

# def get_all_combinations(s):
#     result = []
#     get_letter_combinations(s, 0, [], result)
#     return result

# # Example usage
# s = "123256"
# combinations = get_all_combinations(s)
# print(combinations)



            


