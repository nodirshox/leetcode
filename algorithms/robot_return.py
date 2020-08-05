class Solution:
    def judgeCircle(self, moves: str) -> bool:
        base = [0, 0] #(x, y)
        result = False
        
        for letter in moves:
            if letter == 'U':
                base[1] = base[1] + 1 #(x, y+1)
            elif letter == 'D':
                base[1] = base[1] - 1 #(x, y-1)
            elif letter == 'R':
                base[0] = base[0] + 1 #(x+1, y)
            elif letter == 'L':
                base[0] = base[0] - 1 #(x-1, y)
        
        if base[0] == 0 and base[1] == 0:
            result = True
        
        return result