# str = "Hello Python"
# print("Length is",len(str))
# str1 = str.upper()
# print(str1)
# str2 = str.swapcase()
# print(str2)
# str3 = str.lower()
# print(str3)
# name = input("Enter your name: ")
# str4 = str.replace("Python",name)
# print(str4)

# ---> Bubble sort <---
li = list()
n = int(input("Enter List size: "))
for i in range(n):
    a = int(input())
    li.append(a)
print("Unsotred list:",li)

for i in range(len(li)-1):
    for j in range(len(li)-1-i):
        if(li[j]>li[j+1]):
            li[j],li[j+1]= li[j+1],li[j]

print(f"Sorted list = {li}")
