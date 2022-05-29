number = 2
list = []
while number > 0:
    test = number % 2
    number = number // 2
    list.append(test)
list.reverse()
print(list)


