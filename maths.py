#Check if a number is prime
'''def is_prime(n):
    if n<=1:
        return False #1 or less is not a prime number
    
    for i in range(2,num):
        if n%i==0:
            return False
    else:
        return True
    
#user input 
num=int(input("enter number you want to check: "))

#check and print result
if is_prime(num):
    print(num ,"is a prime number")
else:
    print(num , "is not a prime number")    
        
'''

#for the sum of all prime numbers upto n
"""def is_prime(num):
    if num<2:
        return False
    for i in range (2,int((num**0.5)+1)):
                    if num%i==0:
                            return False
    else:
           return True     

def sumprime(n):
        total=0
        for i in range(2,n+1):
               if is_prime(i):
                       total+=i
        else:
                return total
#user input and result print
n=int(input("enter number for sum (only sum of prime numbers): ")) 
print("sum of prime numbers upto",n,"is",sumprime(n))                    

               
                    
                        """
#DETERMINE THE NUMBER OF TRAILING ZEROS IN FACTORIAL OF NUMBER
"""def count_trailing_zero(n):
    counter=0
    while n>=5:
        n//=5
        counter+=5
    return counter
n=int(input("enter the number you want to check="))   
print("number of trailing zero in this number=", count_trailing_zero(n))



"""
#calculate sum of digits of number until it becomes a single digit number
"""def sum_until_single(n):
    while n>10:
        temp=0
        while n>0:
            digit=n%10
            temp+=digit
            n= n//10
        n=temp
    return n 
n=int(input("enter the number"))    
print("sum of digits until it becomes a single digit number ",sum_until_single(n))         """

#wap to check if a number is harshad number or not
"""def is_harshad(num):
    original_num= abs(num)
    if original_num == 0 :
        return False
    temp=original_num
    digit_sum=0
    while temp>0:
        digit=temp%10
        digit_sum+=digit
        temp=temp//10
    return original_num%digit_sum==0

num=int(input("enter the number you want to check:"))
if is_harshad(num) :
    print(f"{num}  is a harshad number")  
else:
    print(f"{num}  is not a harshad number") """

#find all prime factors of a number
"""def is_prime(num):
    factors=[]
    divisor=2
    while num>1:
        while num % divisor==0:
            factors.append(divisor)
            num=num//divisor
        divisor+=1
    return factors

num=int(input("enter number"))
print ("prime factors of ",num,"are: ",is_prime(num))"""

#check if number is an armstrong number
"""def is_armstrong(num):
    str_num=str(num)
    temp=len(str_num)
    sum_of_digits=0
    for digit in str_num:
        sum_of_digits+=int(digit)**len(str_num)
    return sum_of_digits==num

n=int(input("enter any number"))
if is_armstrong(n):
    print(f"{n} is a armstrong number")
else:
    print(f"{n} is not an armstrong number")"""
#count how many numbers between 1 and 1000 have exactly three digits and are divisble by their sum

"""def is_sum(n):
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    return total

count = 0
for num in range(100, 1000):  # includes 999
    digit = is_sum(num)
    if digit != 0 and num % digit == 0:
        count += 1

print("Total 3-digit Harshad numbers:", count)"""

#print the first n perfect numbers
#euclid theorem=(2**p)-1 * 2**(p-1)
"""def is_prime(num):
    if num<=1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

def is_perfect(n):
    count=0
    p=2 #first prime number
    while count<n:
        mersenne=(2**p )-1
        if is_prime(mersenne):
            perfect_num=(2**(p-1))*mersenne
            print(perfect_num,end=" ")
            count+=1
        p+=1
is_perfect(5)"""
#determine if number is palindrome
"""def is_palindrome(num):
    original=str(num)
    reverse=original[::-1] 
    if original==reverse:
        print(num,"is a palindrome")
    else:
        print(num,"is not palindrome")
is_palindrome(7667)"""
#compute the nth fibonnaci number iteratively
"""def is_fibonacci(n):
    if n<=0:
        return "invalid input"
    elif n==1:
        return 0
    elif n==2:
        return 1
    a,b=0,1
    for  i in range(3,n+1):
        a,b=b,a+b
    return b
print(is_fibonacci(10)) """
          

    