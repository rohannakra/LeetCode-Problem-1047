# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

def filter(string):
    if string == "":    # When there are no adjacent duplicates to start with.
        return ""
        
    for i in range(len(string)):
        try:
            if string[i] == string[i+1]:
                return filter(string[:i] + string[i+2:])    # edit string and call func until there are no duplicates
        except IndexError:    # This happens if we're on the last element (no adjacent duplicates)
            return string

print(filter('abbaca'))    #  -> 'ca'
print(filter('azxxzy'))    # -> 'ay'
print(filter('aaaaaaaaa'))    # -> 'a' (since there are 9 'a' characters, one would remain)

# ---- LeetCode Solution ----

class Solution:
    def removeDuplicates(self, string: str) -> str:
        if string == "":
            return ""

        for i in range(len(string)):
            try:
                if string[i] == string[i+1]:
                    return self.removeDuplicates(string[:i] + string[i+2:])
            except IndexError:
                return string

# NOTE: This passes 97/106 test cases.
