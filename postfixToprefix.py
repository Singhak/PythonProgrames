def postfixToprifix(postfix):
	common = []
	print(postfix)
	for token in postfix:
		if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
			common.append(token)
		elif token in "*/-+%":
			oprd1 = common.pop()
			oprd2 = common.pop()
			value = token + oprd2 + oprd1
			common.append(value)
	return common

			
print("-*+ABC*-DE+FG" in postfixToprifix("AB+C*DE-FG+*-"))
