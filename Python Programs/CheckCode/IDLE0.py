#name = input("Enter your name: ")
#age = int(input("Enter your age: "))
#print(f"Hello my name is {name} and i'm {age} years old.")


#show age in decimal , octal , binary , hexa-decimal
name=input("Enter your name: ")
originalAge = int(input("Enter your age: "))
ageInOctal = oct(originalAge)
ageInBinary = bin(originalAge)
ageInHex = hex(originalAge)
print(f"Hello {name} this is your age in decimal = {originalAge}")
print("your age in octal=",ageInOctal)
print("your age in Binary=",ageInBinary)
print("your age in Hexa-decimal=",ageInHex)
