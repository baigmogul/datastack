class Rule:
    def __init__(self, cell, left=False, right=False, up=False, down=False, op="gt") -> None:
        self.op = op
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.cell = (cell[0], cell[1])

    def __eq__(self, other):
        return self.cell == other.cell

    def __hash__(self):
        return hash(self.cell)

    def __str__(self) -> str:
        return f"Rule(cell={self.cell}, left={self.left}, right={self.right}, up={self.up}, down={self.down}, op={self.op})"