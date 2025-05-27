class Solution:
    
    def isAnagram(self, s: str, t: str) -> bool:
        visited = {}
        # add all items from t to dictionary
        for item in t:
            if item not in visited:
                visited[item] = 1
            else:
                visited[item] += 1

        # subtract values from dictionary when they match in s
        for item in s:
            if item in visited:
                visited[item] -= 1
            else:
                return False
            
            # if a value goes below zero, not an anagram
            if visited[item] < 0:
                return False
        
        # if a value is not at zero, words are not anagrams
        for item in visited:
            if visited[item] > 0:
                return False
            
            
        return True
            



sol = Solution()
print(sol.isAnagram("dodg","god"))

            