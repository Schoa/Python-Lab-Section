class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_to_index = {}

        for index, num in enumerate(nums):
            complement = target - num

            if complement in num_to_index:
                return [num_to_index[complement], index]
            
            num_to_index[num] = index

solution = Solution()

# Input
nums_input = input()
nums = list(map(int, nums_input.split()))

target = int(input())

# Output
result = solution.twoSum(nums, target)

print(result)