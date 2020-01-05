# Design an algorithm to print all pairs of integers within an array which sum to a specified value.
# 
# Input: a = [1, 1, 3], sum = 4
# Output: [1, 3]

# Input: a = [2, 3, 4, 7, 8], sum = 10
# Output: [3, 7], [2, 8]

# first  simple/slow version we got working
def pairs_sum_to_x_1(arr, x):
	print(arr)
	pairs = []
	# time - O(n^2), space - O(n)
	for i in range(len(arr)): # O(n)
		numI = arr[i]
		for j in range(len(arr)): # O(n)
			numJ = arr[j]
			if numI != None and numJ != None and numI + numJ == x:
				print(f"found pair - i {i}, j {j}, numI {numI}, numJ {numJ}")
				pairs.append([numI, numJ])
				arr[i] = None
				arr[j] = None
	return pairs

# refactored first version to show that inner loop is essentially looking for a number in an array	
def pairs_sum_to_x_2(arr, x):
	print(arr)
	pairs = []
	# time - O(n^2), space - O(n)
	for i in range(len(arr)): # O(n)
		numI = arr[i]
		if numI == None:
			continue
		targetJ = x - numI
		for j in range(len(arr)): # O(n)
			numJ = arr[j]
			if numI != None and numJ != None and numJ == targetJ:
				print(f"found pair - i {i}, j {j}, numI {numI}, numJ {numJ}")
				pairs.append([numI, numJ])
				arr[i] = None
				arr[j] = None
	return pairs

# final optimal version where we use a dictionary
def pairs_sum_to_x_3(arr, x):
	occurrences = {}
	for num in arr:
		if num not in occurrences:
			occurrences[num] = 1
		else:
			occurrences[num] += 1
	print(f"occurrences {occurrences}")

	pairs = []
	# time - O(n), space - O(n)
	for i in range(len(arr)): # O(n)
		numI = arr[i]
		targetJ = x - numI
		# O(1)
		if targetJ in occurrences and occurrences[targetJ] >= 1 and occurrences[numI] >= 1:
			pairs.append([numI, targetJ])
			occurrences[numI] -= 1
			occurrences[targetJ] -= 1
	return pairs

print(pairs_sum_to_x_3([2, 3, 4, 7, 8], 10))
