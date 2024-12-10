#storing all even numbers using lambda function
even_numbers = list(filter(lambda x:x % 2 == 0, range(1, 101)))
print(even_numbers)

#num=int(input("Enter a number : "))
#result=lambda even:(num%2==0)
#for num in range(0,101,-1):
    #print(num)