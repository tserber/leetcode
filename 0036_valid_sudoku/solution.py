class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        def check_row_identicity(row):
            counter = 0
            row_nums = set()
            for number in row:
                if number != '.':
                    counter += 1
                    row_nums.add(number)
            # print(counter)
            # print(row_nums)
            if len(row_nums) != counter:
                return True

        quadrants = {i: [] for i in range(9)}
        verticals = {i: [] for i in range(9)}
        for i, row in enumerate(board):

            if i in [0, 1, 2]:
                for j, val in enumerate(row):
                    if val == ".":
                        continue
                    verticals[j].append(val)
                    if j in [0, 1, 2]:
                        quadrants[0].append(val)
                    if j in [3, 4, 5]:
                        quadrants[1].append(val)
                    if j in [6, 7, 8]:
                        quadrants[2].append(val)
            if i in [3, 4, 5]:
                for j, val in enumerate(row):
                    if val == ".":
                        continue
                    verticals[j].append(val)
                    if j in [0, 1, 2]:
                        quadrants[3].append(val)
                    if j in [3, 4, 5]:
                        quadrants[4].append(val)
                    if j in [6, 7, 8]:
                        quadrants[5].append(val)
            if i in [6, 7, 8]:
                for j, val in enumerate(row):
                    if val == ".":
                        continue
                    verticals[j].append(val)
                    if j in [0, 1, 2]:
                        quadrants[6].append(val)
                    if j in [3, 4, 5]:
                        quadrants[7].append(val)
                    if j in [6, 7, 8]:
                        quadrants[8].append(val)

            if check_row_identicity(row):
                return False
        print(quadrants)
        for row in quadrants.values():
            if check_row_identicity(row):
                return False
        for row in verticals.values():
            if check_row_identicity(row):
                return False
        return True
