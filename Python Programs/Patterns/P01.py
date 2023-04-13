# Function Dimand Pyramid
def dimandPyramid(n):
    for i in range(1,n+1):
        print(" "*(n-i)," *"*(i))
    for i in range(1,n+1):
        print(" "*(i)," *"*(n-i))

# Function Call 
n = int(input("Enter your Number: "))
dimandPyramid(n)