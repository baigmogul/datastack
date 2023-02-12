import os
import json
from rules_engine import RulesEngine
from sudoku_solver import SudokuSolver

if __name__ == "__main__": 
    for file in os.listdir("testcases"):
        print("File:", file)
        with open(os.path.join("testcases", file)) as f:
            rules_config = json.loads(f.read())
        board = rules_config["board"]
        print("Board:", board)
        config_file = rules_config["name"]
        rules = rules_config["rules"]
        print("Rules:", rules_config["rules"])
        rules_engine = RulesEngine(rules_config)
        sudoku_solver = SudokuSolver(rules_engine)
        r = sudoku_solver.solve(board)
        print("Testcase:", file, "Expected:", rules_config["assert"], "Actual:", r, "Test Result:", r == rules_config["assert"])
        print()