import os
import os.path as osp


surfix_table = {"Python": "py", "Java": "java", "C++": "cpp", "C": "c"}


class LeetcodeManager:
    def __init__(self, file_path="./meta.txt", root="."):
        self.file_path = file_path
        self.root = root

    def attempt_new_problem(self, num, language="Python"):
        print("Creating workplace for new problem No. %d..." % num)
        workplace_path = osp.join(self.root, str(num))
        if not osp.isdir(workplace_path):
            os.mkdir(workplace_path)

        readme = open(osp.join(workplace_path, "README.md"), "w")
        readme.close()

        if language not in surfix_table:
            raise NotImplementedError(
                "The language type %s is invalid or not implemented." % language
            )

        surfix = surfix_table[language]

        solution = open(osp.join(workplace_path, "solution." + surfix), "w")
        solution.close()

        print("Finished creating workplace for problem No. %d." % num)
