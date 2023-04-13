import time
timetamp = time.strftime('%H:%M:%S')
message = "::WELCOME::"
print(message.center(30))
print("Current Time--->>",timetamp)
timetamp = time.strftime('%H')
name = input("Enter your name: ")

if (int(timetamp) >= 1 and int(timetamp) < 12):
    print('"Good Morning"', name)
elif (int(timetamp) >= 12 and int(timetamp) < 16):
    print('"Good Afternoon"', name)
elif (int(timetamp) >= 16 and int(timetamp) < 22):
    print('"Good Evening"', name)
else:
    print('"Good Night"')
