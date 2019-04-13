class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = path.split("/")
        path.reverse()
        stack = [""]
        while path:
            element = path.pop()
            if element == ".." and stack:
                stack.pop()
            elif element and element != '.' and element != '..':
                stack.append(element)
        res = "/".join(stack)
        if not res:
            return '/'
        elif res[0] != '/':
            return '/' + res
        else:
            return res
