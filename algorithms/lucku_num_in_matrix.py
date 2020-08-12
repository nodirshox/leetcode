class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        lucky_nums = []

        count = 0
        while count < len(matrix):
            item = matrix[count]
            inner_count = 0
            min_in_row = item[0]
            index_of_min_row = 0
            while inner_count < len(item):
                if min_in_row > item[inner_count]:
                    min_in_row = item[inner_count]
                    index_of_min_row = inner_count
                inner_count += 1

            second_count = 0
            luck_number = True
            while second_count < len(matrix):
                if count != second_count:
                    rest_matrix = matrix[second_count]
                    if min_in_row < rest_matrix[index_of_min_row]:
                        luck_number = False

                second_count += 1

            if luck_number:
                lucky_nums.append(min_in_row)
            count += 1

        return lucky_nums