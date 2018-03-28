## using recursion 

def reverseStrRecursion(rev_str):
	if len(rev_str) == 0:
		return rev_str
	else:
		return reverseStrRecursion(rev_str[1:]) + rev_str[0]
	
print(reverseStrRecursion("I am anil"))

## without recursion

def reverseStr(rev_str):
	return rev_str[::-1]

print(reverseStr("I am anil"))
