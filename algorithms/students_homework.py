class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        result = 0
        count = 0

        while count < len(startTime):
            if startTime[count] <= queryTime and endTime[count] >= queryTime:
                result +=1 
            count += 1

        return result