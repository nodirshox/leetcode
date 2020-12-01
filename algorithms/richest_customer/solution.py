class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = 0
        for oneCustomer in accounts:
            customerWealth = 0
            for wealth in oneCustomer:
                customerWealth += wealth
            
            if richest < customerWealth:
                richest = customerWealth
        
        return richest