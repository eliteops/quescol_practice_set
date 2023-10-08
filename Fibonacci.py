user = int(input())
first, second = 0, 1
for i in range(user):
    if i <= 1:
        result = i
    else:
        result = first + second
        first = second
        second = result
    print(result, end = ', ')
