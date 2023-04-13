def fact(num):
    factorial = 1
    for i in range(1,num+1):
        factorial = factorial*i
    return factorial 

n = int(input("Enter your Number to check factorial:"))
print(fact(n))