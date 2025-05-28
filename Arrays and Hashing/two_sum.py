class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        visited = {}

    
        for i in range(len(nums)):
            # check if target - current value is in hash map
            value = target - nums[i]

            # if yes, return difference and current index
            if value in visited:
                return [visited[target-nums[i]], i]
            
            # otherwise, add current value and index to hash map
            else:
                visited[nums[i]] = i

sol = Solution()
print(sol.twoSum([3,4,6,10],7)) # expected output [0,1]