a = input("Enter Your Number: ")

try:
    for i in range(1,11):
        print(f"{int(a)} x {int(i)} = {int(a)*i}")
except :
    if(a=="quit" or a=="Quit"):
        print("No error")  
    else:  
        raise TypeError("Value should be intiger")
    