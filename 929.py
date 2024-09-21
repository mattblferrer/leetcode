class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        unique_emails = set()

        for email in emails:
            local, domain = email.split("@")
            local = local.replace(".", "")  # remove dots from local name
            for i, char in enumerate(local):  # ignore everything after first +
                if char == "+":
                    local = local[:i]

            unique_emails.add(local + "@" + domain)

        return len(unique_emails)