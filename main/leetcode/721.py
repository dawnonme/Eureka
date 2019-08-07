class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        from collections import defaultdict

        table = defaultdict(list)

        for account in accounts:
            name = account[0]
            emails = defaultdict(bool)
            for i in range(1, len(account)):
                emails[account[i]] = True
