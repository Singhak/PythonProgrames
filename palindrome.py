def palindrome(num):
	rev_num = 0
	n = num
	while num > 0:
		rev_num = rev_num * 10 + num % 10
		num = num//10
		
	print("Is number {} is a palindrome : {}".format(n, n == rev_num))
	
palindrome(9599)
palindrome(959
