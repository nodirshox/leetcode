class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        checked_email =[]
        
        for mail in emails:
            converted = mail.split('@')
            local_name = converted[0]
            domain_name = converted[1]
            
            filtered_local_name = ''
            for letter in local_name:
                if letter != '.' and letter != '+':
                    filtered_local_name += letter
                if letter == '+':
                    break
            
            full_email = filtered_local_name + '@' + domain_name
            
            if full_email not in checked_email:
                checked_email.append(full_email)
            
        return len(checked_email)