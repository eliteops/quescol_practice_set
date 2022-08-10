n = int(input())
reverse = 0
temp = n
while temp!=0:
	reverse = reverse*10 + temp%10
	temp = temp//10
if reverse == n:
	print(n,'is a palindrome')
else:
	print(n,'not a palindrome.')
  
