'''
print(bin(10))
print(0b1010)
'''
'''
n= 10
bi = format(n,'b')
print(bi)
'''

def countBits(n):
    bi = format(n,'b')
    count = 0
    for i in bi:
        if i==1:
            count = count+1
    return count

        
n = int(input())
print(countBits(n))

bi = 1010
for i in bi:
    for i in bi:
        if i==1:
            print(i)
    
