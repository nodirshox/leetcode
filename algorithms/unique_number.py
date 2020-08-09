class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        result = []
        selected_nums = []

        i = 0
        is_unique = True

        for num in arr:
            j = 0
            occurence = 1

            if num not in selected_nums:
                selected_nums.append(num)
                
                for numbers in arr:
                    if i != j:
                        if num == numbers:
                            occurence += 1
                    j += 1
                if occurence in result:
                    is_unique = False
                    break
                result.append(occurence)

            i += 1
            
        return is_unique