# import random
# import string
#
#
# # def generate(length):
# characters = string.digits + string.ascii_letters + string.punctuation
# password = ""
# for x in range(8):
#         password += random.choice(characters)
#
# print(password)
#
# list = [1,6,3,8,5,9]
# # list.append(random.randint * 100 )
#
# avg = sum(list) / len(list)
#
# print(avg)
#
#
#
#
#
# year = int(input())
#
# if (year%4 == 0 and year%100 == 0) or (year%400 == 0):
#         print("Year is a leap year")
# else :
#         print("Year is not a leap year")

value =  int(input())
result = 1
for i in range(1,value+1):
        result *= i

print(result)
