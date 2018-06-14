def bubbleSort(alist):
	passCount = len(alist) - 1
	exchange = True
	while passCount > 0 and exchange:
		exchange = False
		for i in range(passCount):
			if alist[i] > alist[i+1]:
				exchange = True
				temp = alist[i]
				alist[i] = alist[i+1]
				alist[i+1] = temp
		passCount = passCount - 1
	return alist
	
testlist = [0, 11, 2, 8, 13, 17, 19, 32, 42,]
print(bubbleSort(testlist))

################################################################################################################
#
#   Analyze of Bubble sort
#
################################################################################################################
#
#   To analyze the bubble sort, we should note that regardless of how the items are arranged in the initial list, n−1 passes will be
#   made to sort a list of size n. The total number of comparisons is the sum of the first n−1 integers. 
#   Recall that the sum of the first n integers is 1/2n^2+1/2n. The sum of the first n−1 integers is 1/2n^2+1/2n−n, which is 1/2n^2−1/2n. 
#   This is still O(n2) comparisons. In the best case, if the list is already ordered, no exchanges will be made. 
#   However, in the worst case, every comparison will cause an exchange. On average, we exchange half of the time
#
