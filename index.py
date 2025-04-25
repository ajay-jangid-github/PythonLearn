from typing import List
# print("hello, mera pahla python program")

# a = [2,3,4,5]
# target = 6
# for i in range(0,3):
#   for j in range(i+1,4):
#     if a[i] + a[j] == target:
#       print(i,j)
#       break

class Solution:
		def twoSum(self, A: List[int], target: int) -> List[int]:
			for i in range(len(A)):
				for j in range(i + 1, len(A)):
					if A[i] + A[j] == target:
						return [i, j]

sol = Solution()
result = sol.twoSum([2,3,4,7],9)
print(result)

    