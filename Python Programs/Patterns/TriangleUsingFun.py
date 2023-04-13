# Triangle using function with a trick

def triangle(n):
    for i in range(1,n+1):
         print(" "*(n-i)," *"*i)
    return triangle

triangle(5)

print("<------------>")

# Pattern using fun in python
def patt(n):
    for i in range(1,n+1):
        print("  "*(n-i),"* "*i)
    return patt

patt(5)

# two statement in one line in pyton
print("Hello ",end=""); print("Python")
