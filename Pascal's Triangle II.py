class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex < 2:
            return [1] * (rowIndex + 1)

        prev_row = self.getRow(rowIndex - 1)
        start_row = [1]
        for i in range(len(prev_row) - 1):
            start_row.append(prev_row[i] + prev_row[i + 1])
        start_row.append(1)

        return start_row
