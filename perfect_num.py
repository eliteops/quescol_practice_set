import math 
user_num = int(input('enter no to check if it is perfect or not ?'))
total = []
for i in range(1, user_num//2+1):   # from 1 to half of user_num , +1 added because range consider 1 less.
    if user_num % i == 0:           # checking if user_num is divisible by number.
        total.append(i)             # adding that number to the list.

print(total ,"=", sum(total))       # sum is used to add numbers and to use sum() function math module imported.
if sum(total) == user_num:          # checking if total equals to user_num
    print(f'{user_num} is a perfect number.')
else:
    print(f'{sum(total)} is not equals to {user_num}')
