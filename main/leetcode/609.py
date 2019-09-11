class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        contents = {}

        for long_str in paths:
            elements = long_str.split()
            root_path = elements[0]
            for i in range(1, len(elements)):
                op, cl = elements[i].find('('), elements[i].find(')')
                name = elements[i][:op]
                content = elements[i][op + 1:cl]
                if content in contents:
                    contents[content].append(root_path + '/' + name)
                else:
                    contents[content] = [root_path + '/' + name]

        return [v for _, v in contents.items() if len(v) > 1]