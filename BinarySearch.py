### Without recursion###########

def binarySearch(alist, item):
	first = 0
	last = len(alist) - 1
	found = False
	while first < last and not found:
		midpoint = (first + last)//2
		midItem = alist[midpoint]
		if midItem == item:
			found = True
		elif item < midItem:
			last = midpoint - 1
		else:
			first = midpoint + 1
	return found
			
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))


### With recursion###########

def binarySearch(alist, item):
	if len(alist) == 0:
		return False
	else:
		midpoint = len(alist)//2
		midItem = alist[midpoint]
		if midItem == item:
			return True
		elif item < midItem:
			binarySearch(alist[:midpoint], item)
		else:
			binarySearch(alist[midpoint+1:], item)

			
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))


#############################################################################################################
#
# Analysis of Binary Search
#
######################################################################################################################
# To analyze the binary search algorithm, we need to recall that each comparison eliminates about half of the remaining items 
# from consideration. What is the maximum number of comparisons this algorithm will require to check the entire list? 
# If we start with n items, about n2 items will be left after the first comparison. After the second comparison, 
# there will be about n4. Then n8, n16, and so on.
#
# The number of comparisons necessary to get to this point is i where n2i=1. Solving for i gives us i=logn. 
# The maximum number of comparisons is logarithmic with respect to the number of items in the list. Therefore,
# the binary search is O(logn).
#############################################################################################################
