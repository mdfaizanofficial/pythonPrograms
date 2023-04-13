#Your code goes here

#input number from user
number = int(input())

# convert number into list
digits = list(map(int, str(number)))

sume=0
sumo=0
for i in digits:
    if(i%2==0): #add even number
        sume+=i
    else:
        sumo+=i #add odd number

print(sume,sumo) #print result