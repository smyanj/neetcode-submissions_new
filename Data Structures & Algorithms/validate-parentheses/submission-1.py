class Solution:
    def isValid(self, s: str) -> bool:
        matches = {'}':'{', ')':'(', ']':'['}
        stack = []

        for val in s:
            if val in matches.values():
                stack.append(val)
            else:
                if matches[val] == stack[-1]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0