li = list()
# insert value in list 
size = int(input("Enter list size: "))
for i in range(size):
    li.append(int(input()))
print("Simple list = ",li)
l2 = li.copy()
# sorting
for i in range(len(li)-1):
    for j in range(len(li)-1-i):
        if(li[j]>li[j+1]):
            li[j],li[j+1] = li[j+1],li[j]

print("After sort = ",li)
s = int(input("Enter element who you want to search: "))
# searching
for i in range(len(l2)):
    if(l2[i]==s):
        print("The element position is:",i+1)
        break