class Matrix:
    def __init__(self, matrix_string):
        rows = matrix_string.split("\n")
        self.matrix = []
        for r in rows:
            row_elements = r.split(" ")
            self.matrix.append([int(element) for element in row_elements])
    def row(self, index):
        return self.matrix[index-1]
    def column(self, index):
        columns = []
        for i in range(len(self.matrix)):
            columns.append(self.matrix[i][index-1])
        return columns
