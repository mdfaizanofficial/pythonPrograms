n = int(input("Enter your Number: "))

print("1st way to print fibonacci sequence...")

a = 0
b = 1
print(a,b,sep="\n")
for i in range(3,n+1):
    c=a+b
    print(c,end=",")
    a=b
    b=c

#2nd way
print("\n2nd way to print fibonacci sequence...")

i =0
j=1
for x in range(1,n+1):
    k = i+j
    print(i,end=",")
    i=j
    j=k
    
