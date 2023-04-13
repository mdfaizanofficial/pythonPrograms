li = list()
n = int(input("Enter list length: "))
for i in range(n):
    li.append(int(input()))
print(f"Unsorted list: {li}")

for i in range(len(li)-1):
    for j in range(len(li)-1-i):
        if(li[j]>li[j+1]):
            li[j],li[j+1] = li[j+1],li[j]
print("Sorted List:",li)