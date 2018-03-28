def sumOfdigit(num):
	sum = 0
	n = num
	while num > 0:
		sum = sum + num % 10
		num = num//10
	
	print("Sum of digit in {} is {}".format(n, sum))
	
sumOfdigit(12345)
