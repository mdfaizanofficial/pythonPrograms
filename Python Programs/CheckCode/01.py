def max_ele(numbers):
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max
l1 = list()
for i in range(5):
    l1.append(int(input()))
print(max_ele(l1))
