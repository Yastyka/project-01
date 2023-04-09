
class Table(object):
 
    def __init__(self, rows, cols):
        self._rows = rows
        self._cols = cols
        self._table = [[0] * cols for _ in range(rows)]
 
    def get_value(self, row, col):
        return (self._table[row][col] if 0 <= row < self._rows and 0 <= col < self._cols
                else None)
 
    def set_value(self, row, col, value):
        self._table[row][col] = value
 
    def n_rows(self):
        return self._rows
 
    def n_cols(self):
        return self._cols
 
    def add_row(self, row):
        self._table.insert(row, [0] * self._cols)
        self._rows += 1
 
    def add_col(self, col):
        for row in range(self._rows):
            self._table[row].insert(col, 0)
        self._cols += 1



def main():
   
    tab = Table(5, 5)
    tab.set_value(1, 1, 0)
    for i in range(tab.n_rows()):
        for j in range(tab.n_cols()):
            print(tab.get_value(i, j), end=' ')
        print()
    print()
 
    tab.add_row(1)
 
    for i in range(tab.n_rows()):
        for j in range(tab.n_cols()):
            print(tab.get_value(i, j), end=' ')
        print()
    print()

    tab.add_col(1)
 
    for i in range(tab.n_rows()):
        for j in range(tab.n_cols()):
            print(tab.get_value(i, j), end=' ')
        print()
    print()


if __name__ == "__main__":
    main()


