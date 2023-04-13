# LinkedIn Quiz
def multiplier(y):
    return lambda x:x*y
f = multiplier(2)
print(f(False))
print(f(True))
print(f(3))