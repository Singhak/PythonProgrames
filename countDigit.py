def countDigit(num):
	count = 0
	n = num
	while num > 0:
		count = count + 1
		num = num//10
	
	print("Total number of digit in {} is {}".format(n, count))
	
countDigit(13425)
