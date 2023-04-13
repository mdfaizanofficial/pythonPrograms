first = int(input("Enter your First Number: "))
symbol = input("Enter symbol +,-,*,/,% :  ")
second = int(input("Enter your  Second Number: "))

if symbol == '+':
    print("ADDTION ", first+second)

elif symbol == '-':
    print("SUBTRACTION ", first-second)

elif symbol == '*':
    print("MULTIPLICATION ", first*second)

elif symbol == '*':
    print("MULTIPLICATION ", first*second)

elif symbol == '/':
    if second == 0:
        print("infinite")
    else:
        print("DIVISION ", first/second)

elif symbol == '%':
        print("REMINDAR ", first % second)

else:
        print("Invalid sybmol...")
