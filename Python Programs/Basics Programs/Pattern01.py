# printing star '*' in pyramid shape
n = int(input("Enter your Number: "))
for i in range(n):
    for j in range(n-i-1):
        print(end=" ")
    for j in range(i+1):
        print(" *",end="")  
    print()