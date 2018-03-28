def reverseNum(num):
	rev_num = 0
	n = num
	while num > 0:
		rev_num = rev_num * 10 + num % 10
		num = num//10
	print("Reverse of number {} is {}".format(n, rev_num))
	
reverseNum(3251)
