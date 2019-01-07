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
def pairsSumToTarget(nums, targetSum):
    occurrences = {}
    for num in nums:
        if num in occurrences:
            occurrences[num] += 1
        else:
            occurrences[num] = 1
    print("occurrences " + str(occurrences))
    pairs = []
    for i in range(0, len(nums)):
        numI = nums[i]
        if occurrences[numI] == 0:
            continue
        numJ = targetSum - numI
        if numI == numJ:
            if occurrences[numI] >= 2:
                print("numI " + str(numI) + ", numJ " + str(numJ))
                pairs.append([numI, numJ])
                occurrences[numI] -= 2
                print("occurrences " + str(occurrences))
        else:
            if numJ in occurrences and occurrences[numJ] >= 1:
                print("numI " + str(numI) + ", numJ " + str(numJ))
                pairs.append([numI, numJ])
                occurrences[numI] -= 1
                occurrences[numJ] -= 1
                print("occurrences " + str(occurrences))
    print("\n pairs " + str(pairs))
# for j in range(i + 1, len(nums)):
#     if nums[i] != None and nums[j] != None:
#         if nums[j] == numJ:
#             print("i " + str(i) + ", j " + str(j))
#             pairs.append([nums[i], nums[j]])
#             nums[i] = None
#             nums[j] = None
#             print("nums " + str(nums))