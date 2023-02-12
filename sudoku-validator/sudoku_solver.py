def has_unique_numbers(row) -> bool:
    # Check if the row has unique numbers
    for number in row:
        if row.count(number) > 1:
            return False
    return True


def has_valid_numbers(row) -> bool:
    # Check if the row has valid numbers
    for number in row:
        # Check if the number is an integer
        if not isinstance(number, int):
            return False
        # Check if the number is positive
        if number <= 0:
            return False
        # Check if the number is less than the length of the row
        if number > len(row):
            return False
    return True


def get_column(board, col) -> list:
    # Get the column at the given index
    column = []
    for row in board:
        column.append(row[col])
    return column


def validate_column(board, col) -> bool:
    # Check if the column has valid numbers
    if not has_valid_numbers(get_column(board, col)):
        return False

    # Check if the column has unique numbers
    if not has_unique_numbers(get_column(board, col)):
        return False

    return True


def validate_row(row) -> bool:
    # Check if the row has valid numbers
    if not has_valid_numbers(row):
        return False

    # Check if the row has unique numbers
    if not has_unique_numbers(row):
        return False

    return True


def is_square(board) -> bool:
    # Check if the board is a square
    for row in board:
        if len(row) != len(board):
            return False
    return True


def validate_board(board) -> bool:
    # Check if the board is empty
    if not board:
        return False
        
    # Check if the board is a list
    if not isinstance(board, list):
        return False

    # Check if the board is a square
    if not is_square(board):
        return False

    # Check if the board has valid rows
    for row in board:
        if not validate_row(row):
            return False

    # Check if the board has valid columns
    for col in range(len(board)):
        if not validate_column(board, col):
            return False

    return True


class SudokuSolver:

    def __init__(self, rules_engine) -> None:
        self.rules_engine = rules_engine

    def solve(self, board) -> bool:
        # Check if the board is valid
        if not validate_board(board):
            return False
        # Check if the board satisfies the rules
        if not self.validate_constraints(board):
            return False

        return True

    def validate_constraints(self, board) -> bool:
        rules = self.rules_engine.get_rules()
        if not rules:
            return True
        for row in range(len(board)):
            for col in range(len(board[row])):
                for rule in rules:
                    if rule.cell == (row, col):
                        if rule.left and col != 0:
                            if rule.op == "gt":
                                if board[row][col] <= board[row][col - 1]:
                                    return False
                            elif rule.op == "lt":
                                if board[row][col] >= board[row][col - 1]:
                                    return False
                        if rule.right and col != len(board[row]) - 1:
                            if rule.op == "gt":
                                if board[row][col] <= board[row][col + 1]:
                                    return False
                            elif rule.op == "lt":
                                if board[row][col] >= board[row][col + 1]:
                                    return False
                        if rule.up and row != 0:
                            if rule.op == "gt":
                                if board[row][col] <= board[row - 1][col]:
                                    return False
                            elif rule.op == "lt":
                                if board[row][col] >= board[row - 1][col]:
                                    return False
                        if rule.down and row != len(board) - 1:
                            if rule.op == "gt":
                                if board[row][col] <= board[row + 1][col]:
                                    return False
                            elif rule.op == "lt":
                                if board[row][col] >= board[row + 1][col]:
                                    return False
        return True