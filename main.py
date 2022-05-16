# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

def filter(string):
    for i in range(len(string)):
        try:
            if string[i] == string[i+1]:
                return filter(string[:i] + string[i+2:])
        except IndexError:
            return string
    
    return string

print(filter('abbaca'))
print(filter('azxxzy'))

# ---- LeetCode Solution ----

class Solution:
    def removeDuplicates(self, string: str) -> str:
        for i in range(len(string)):
            try:
                if string[i] == string[i+1]:
                    return self.removeDuplicates(string[:i] + string[i+2:])
            except IndexError:
                return string
        
        return string

# NOTE: This passes 96/106 test cases.
