class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        my_arr = []
        current = head

        while (current != None):
            my_arr.append(current.val)
            current = current.next

        power = len(my_arr) - 1
        decimal = 0

        for digit in my_arr:
            decimal += digit * (2 ** power)
            power -= 1
        
        return decimal