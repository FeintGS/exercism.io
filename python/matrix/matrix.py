class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string

    def row(self, index):
        result = self.matrix_string.split('\n')
        result = result[index-1]
        result = result.split(' ')
        result = list(map(int, result))
        return result

    def column(self, index):
        num_rows = len(self.matrix_string.split('\n'))
        result = []
        for i in range(1, num_rows+1):
            r = self.row(i)
            result.append(r[index-1])
        return result


