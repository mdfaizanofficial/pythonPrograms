li = [54,45,32,89,65,4,5,4,2,1,345,32]
size = len(li)
# size = int(input("Enter your list size "))
# for i in range(size):
#     li.append(int(input()))

for i in range(size-1):
    min = i
    for j in range(size-1-i):
        if(li[min]>li[j+1]):
            min = j+1

print("Minimum element is:",li[min])
