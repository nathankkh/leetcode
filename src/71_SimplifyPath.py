class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        arr = path.split('/')
        for c in arr:
            match c:
                case "..":
                    if stack:
                        stack.pop()
                case ".":
                    pass
                case "":
                    pass
                case _:
                    stack.append(c)
        return '/'+'/'.join(stack)
    
sol = Solution()
tc = "/home/"
sol.simplifyPath(tc)