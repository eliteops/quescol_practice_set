num = int(input('enter'))
def reverse(num):
    if num < 10:
        return num
    else:
        return (int(str(num % 10)+str(reverse(num // 10)))) ''' here we are using recursion by 
                                                                 calling function again and again and getting 
                                                                 remainder and adding that number as a string.'''
def palindrome(num):
    if num == reverse(num):                                # checking here if num is equals to reversed num...
        return 1
if palindrome(num) == 1:
    print(f" {num} it is a palindrome number \
and reverse is this {reverse(num)} ")
else:
    print(f"{num} not a palindrome number .\
reverse is this {reverse(num)}")
