class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        domains = set()
        for email in emails:
            split_point = email.find('@')
            local = email[:split_point]
            plus = local.find('+')
            if plus != -1:
                local = local[:plus]
            last = 0
            while True:
                period = local.find('.', last)
                if period == -1:
                    break
                local = local[:period] + local[period + 1:]
                last = period
            true_name = local + email[split_point:]
            domains.add(true_name)

        return len(domains)