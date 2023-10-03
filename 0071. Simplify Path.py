class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        out = []
        for s in path:
            if s == '..':
                try:
                    out.pop()
                except IndexError:
                    pass
                continue
            if s == '.':
                continue
            if s != '':
                out.append(s)
        return '/' + '/'.join(out)
