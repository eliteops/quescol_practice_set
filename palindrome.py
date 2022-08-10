n = int(input())
reverse = 0                              # we will get reverse value here. 
temp = n				 # it is used for using while loop.
while temp!=0:				 # temp value will be decrease to 0 for ending loop. 
	reverse = reverse*10 + temp%10	 # x10 is used to get complete reverse number and % used to get reverse number one by one.
	temp = temp//10			 # // it is a floor division and used to get positive quotient(भागफल).
if reverse == n: 			 # if reverse mathches with n then congrats it is a palindrome.
	print(n,'is a palindrome')
else:
	print(n,'not a palindrome.')	 # else not a palindrome.
  
