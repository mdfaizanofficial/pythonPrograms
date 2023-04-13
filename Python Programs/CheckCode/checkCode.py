a = "faizan"
b = "faizon"
aList = list(a)
bList = list(b)
k =0
for i in bList:
     if i in aList:
        k+=1
if(k==len(bList)):
   print(True)
else:
    print(False)

    
