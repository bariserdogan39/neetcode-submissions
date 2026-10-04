class Solution:
    def isValid(self, s: str) -> bool:
        
        dicts = {"(": ")", '{': '}', '[': ']'}
        stack = []
        for i in s:
            if i in dicts:
                stack.append(dicts[i])
            else:
                if not stack or stack.pop() != i:
                    return False
        return len(stack) == 0