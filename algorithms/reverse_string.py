class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        min_count = 0
        max_count = len(s) - 1

        while min_count < len(s) / 2:
            first_item = s[min_count]
            last_item = s[max_count]
            #override
            s[min_count] = last_item
            s[max_count] = first_item
            
            min_count += 1
            max_count -= 1