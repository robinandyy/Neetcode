class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create hash set to check for duplicates in O(n) time complexity and space complexity
        visited = set()
        for num in nums:
            if num in visited:
                return True
            visited.add(num)
        return False