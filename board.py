class board():
    def __init__(self):
        self.board = [[0 for _ in range(9)] for _ in range(9)]

    def input_number(self, row, col, number):
        input_row = row - 1
        input_col = col - 1
        if 0 > input_row > 9 and 0 > input_col > 9 and 0 > number > 9:
            raise ValueError("Row and column must be between 1-9 and number must be between 0-9.")
        self.board[input_row][input_col] = number
        
    def validate_row(self, row):
        input_row = sorted(self.board[row - 1])
        if 0 > row > 9:
            raise ValueError("Row must be between 1-9.")
        row_sum = sum(input_row)
        if row_sum != 45:
            return False
        for i in range(1, 10):
            if input_row.count(i) > 1:
                return False
        return True
    
    def validate_column(self, col):
        input_col = []
        if 0 > col > 9:
            raise ValueError("Column must be between 1-9.")
        for i in range(9):
            input_col.append(self.board[i][col - 1])
        input_col = sorted(input_col)
        col_sum = sum(input_col)
        if col_sum != 45:
            return False
        for i in range(1, 10):
            if input_col.count(i) > 1:
                return False
        return True
    
    def validate_square(self, square_row, square_col):
        if 0 > square_row > 3 and 0 > square_col > 3:
            raise ValueError("Square row and column must be between 1-3.")
        start_row = (square_row - 1) * 3
        start_col = (square_col - 1) * 3
        input_square = []
        for i in range(3):
            for j in range(3):
                input_square.append(self.board[start_row + i][start_col + j])
        input_square = sorted(input_square)
        square_sum = sum(input_square)
        if square_sum != 45:
            return False
        for i in range(1, 10):
            if input_square.count(i) > 1:
                return False
        return True
    
    def display_board(self):
        for row in self.board:
            # Convert each number to string
            str_row = [str(num) for num in row]
            # Group into three sublists
            groups = [str_row[i:i+3] for i in range(0, 9, 3)]
            # Join each group with ' | '
            group_strings = [' | '.join(group) for group in groups]
            # Join the groups with ' || '
            formatted_row = '|| ' + ' || '.join(group_strings) + ' ||'
            print(formatted_row)

def main():
    game_board = board()
    game_board.input_number(1, 1, 5)
    game_board.input_number(1, 2, 3)
    game_board.input_number(1, 3, 4)
    game_board.display_board()
    print("Row 1 valid:", game_board.validate_row(1))
    print("Column 1 valid:", game_board.validate_column(1))
    print("Square (1,1) valid:", game_board.validate_square(1, 1))

if __name__ == "__main__":
    main()
        
                      

