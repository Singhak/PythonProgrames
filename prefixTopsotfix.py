def prefixTopostfix(prefix):
	common = []
	print(prefix)
	for token in reversed(prefix):
		if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
			common.append(token)
		elif token in "*/-+%":
			oprd1 = common.pop()
			oprd2 = common.pop()
			value = oprd1 + oprd2 + token
			common.append(value)
	return common
	
print("AB+C*DE-FG+*-" in prefixTopostfix("-*+ABC*-DE+FG"))
