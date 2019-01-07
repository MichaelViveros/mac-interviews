# Design an algorithm to print all pairs of integers within an array which sum to a specified value.
# 
# Input: a = [1, 1, 3], sum = 4
# Output: [1, 3]
# 
# Input: a = [ 7, 2, 5, 8, 3 ], sum = 10
# Output: [3, 7], [2, 8]

# a = [None, 1, None]

# numI + numJ = targetSum
# numJ = targetSum - numI
# numI = 1, numJ = 4 - 1 = 3

# searching a list - O(n)
# searching a hash map - O(1)
# { 1 => 2, 3 => 1 }
# numI = 1, numJ = 4 - 1 = 3, 
# 3 in hash map? yes!
# pair [1, 3]
# { 1 => 1, 3 => 0 }

# time - O(n), space - O(n)
def pairsSumToTarget(nums, targetSum):
    occurrences = {} # space - O(n)

    # time - O(n)
    for num in nums:
        if num in occurrences:
            occurrences[num] += 1
        else:
            occurrences[num] = 1
    print("occurrences " + str(occurrences))

    pairs = [] # space - O(n)
    # time - O(n * 1)
    for i in range(0, len(nums)): # time - O(n)
        numI = nums[i]
        if occurrences[numI] == 0:
            continue
        numJ = targetSum - numI
        if numI == numJ:
            if occurrences[numI] >= 2: # time - O(1)
                print("numI " + str(numI) + ", numJ " + str(numJ))
                pairs.append([numI, numJ])
                occurrences[numI] -= 2
                print("occurrences " + str(occurrences))
        else:
            if numJ in occurrences and occurrences[numJ] >= 1: # time - O(1)
                print("numI " + str(numI) + ", numJ " + str(numJ))
                pairs.append([numI, numJ])
                occurrences[numI] -= 1
                occurrences[numJ] -= 1
                print("occurrences " + str(occurrences))
    print("\n pairs " + str(pairs))

print("pairsSumToTarget([ 1, 1, 3 ], 4):\n")
pairsSumToTarget([ 1, 1, 3 ], 4)

print("\n\npairsSumToTarget([ 7, 2, 5, 8, 3 ], 10):\n")
pairsSumToTarget([ 7, 2, 5, 8, 3 ], 10)

# time - O(n^2), space - O(n)
def pairsSumToTargetSlow(nums, targetSum):
    pairs = [] # space - O(n)
    # time - O(n * n) = O(n^2)
    for i in range(0, len(nums)): # time - O(n)
        numI = nums[i]
        if numI == None:
            continue
        numJ = targetSum - numI
        for j in range(i + 1, len(nums)): # time - O(n)
            if nums[i] != None and nums[j] != None:
                if nums[j] == numJ:
                    print("i " + str(i) + ", j " + str(j))
                    pairs.append([nums[i], nums[j]])
                    nums[i] = None
                    nums[j] = None
                    print("nums " + str(nums))
        print("\n pairs " + str(pairs))