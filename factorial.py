## Uisng recursion

def recFactorial(num):
	if num == 0:
		return 1
	else :
		return num * findFactorial(num-1)
		
print(recFactorial(5))
## Using loop

def loopFactorial(num):
	temp_num = 1
	for n in range(1, num+1):
		temp_num = temp_num * n
	return temp_num
	
print(loopFactorial(5))
