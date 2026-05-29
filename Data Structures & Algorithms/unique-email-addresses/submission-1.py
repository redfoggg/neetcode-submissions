class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueEmails = set()

        for e in emails:
            local, domain = e.split('@')
            local = local.split('+', 1)[0].replace(".", "")
            local = local.replace(".", "")
            uniqueEmails.add(f"{local}@{domain}")

        return len(uniqueEmails)

