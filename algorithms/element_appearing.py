class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count = 0
        number = None
        occurrence = 0

        while count < len(arr):
            if number == None:
                number = arr[count]
            item = arr[count]

            if number != arr[count]:
                number = arr[count]
                occurrence = 0

            if item == number:
                occurrence += 1
                
            if occurrence > len(arr) / 4:
                break

            count += 1

        return number