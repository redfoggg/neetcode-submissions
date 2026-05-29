class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueEmails = set()

        for e in emails:
            local, domain = e.split('@')
            if '+' in local:
                local, _ = local.split('+', 1)
            local = local.replace(".", "")
            uniqueEmails.add("".join([local, "@", domain]))

        return len(uniqueEmails)

