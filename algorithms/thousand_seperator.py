class Solution:
    def thousandSeparator(self, n: int) -> str:
        converted = str(n)[::-1]
        new_number = ""
        format_count = 0
        for digit in converted:
            if format_count == 3:
                new_number += "."
                format_count = 0
            new_number += digit
            format_count += 1
        
        return new_number[::-1]