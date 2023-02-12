# Problem

You will write a solution validator for a board game similar to Sudoku. The game has an n by n board. Each row and column will be filled by numbers between 1 and n. Like Sudoku, each number can appear once and only once in each row and each column. But unlike Sudoku some adjacent cells have additional constraints between them. For example, in the board shown below cell (1, 1) should be greater than cell (1, 2), cell (2,3) should be greater than cell (3,3), and so on.

board =         [[1, 2, 3, 4],
                [4, 3, 2, 1],
                [2, 1, 4, 3],
                [3, 4, 1, 2]]

You will be writing a program to validate a given solution of the puzzle. You need to come up with the data structures to represent the board, the constraints and the solution, as well as the algorithm to validate it. For example here’s the pseudo code:

```
boolean validate_solution(board, solution):
        return true if the solution is valid, false otherwise
```

For the purpose of creating a running program, you can hard code a 4x4 board with constraints, and valid/invalid solutions to validate. The constraints should be modeled as initial values in your data structure, as opposed to logic in your code (i.e. you cannot do things like if cell(1,1) > cell(1,2) then …). Your solution must be executable and fully tested. Develop your solution the same way as you do in your work and pay attention to all details.

### Grading Guidelines

Your submission will be graded with the following factors considered, among others:

* Correctness - whether the solution give correct results
* Completeness - whether the solution covers all scenarios, including handling of error conditions
* Design - Well structured, easily readable and maintainable
* Testability - Easy to test. Following principles of test driven development
* Style - Elegance of the the code and solution

## Implementation

Project requires Python 3.6 or higher. It has no external dependencies. So you can just clone the repository and run the tests. Project can be executed by simply running - ```python3 solution.py```. It will run the tests and print the results.

### Files
* ```solution.py``` - Main program to run execute the solution
* ```rule.py``` - Rule class that defines the rules for the game
* ```rules_engine.py``` - Rules engine that helps provide additional constraints
* ```sudoku_solver.py``` - Core logic to solve the board with the given rules
* ```sample_rules.json``` - Sample rules file to load the rules from
* ```tests/*``` - Rules with constraints and sample boards to test the solution

### Classes

* ```Rule``` class acts as a data structure to hold the rule information. It contains all the information about the rule and the constraints.
* ```SudokuSolver``` class contains the core logic for validating the solution. It takes in the rules and the board as input and validates the solution. It uses ```RulesEngine``` to validate the additional constraints. 
* ```RulesEngine``` class contains the logic to validate the additional constraints. It takes in the rules and the board as input and validates the solution.
* ```Solution.py``` class contains the main program to run the solution. It takes in the rules file and the board as input and validates the solution.
* ```Tests/**``` contains the sample rules and sample boards to test the solution.

### Rules.json

Here is the sample_rules.json file:

```
{
    "version": "v1",
    "rules": [
        {
            "cell": [1, 1],
            "constraints": {
                "up": false,
                "down": false,
                "left": false,
                "right": true,
                "operator": "gt"
            }
        }
    ]
}
```

The cell represents the cell that is to be validated. The constraints field represents the constraints that are to be validated. The operator field represents the operator that is to be used for the validation. The operator can be one of the following - ```gt```, ```lt```, ```eq```, ```ne```, ```ge```, ```le```. The up, down, left and right fields represent the direction in which the constraint is to be validated. The value of the field can be either ```true``` or ```false```. If the value is ```true``` then the constraint is to be validated in that direction. If the value is ```false``` then the constraint is not to be validated in that direction.

### Testcases
Here is the same testcase.json file:

```
{
    "version": "v1",
    "name": "test_invalid_cell.json",
    "assert": false,
    "board":    [[1, 2, 3.0, 4],
                [4, 3, 2, 1],
                [2, 1, 4, 3],
                [3, 4, 1, 2]],
    "rules": [
        {
            "cell": [2, 1],
            "constraints": {
                "up": true,
                "down": false,
                "left": false,
                "right": false,
                "operator": "lt"
            }
        }
    ]
}
```

The board field represents the board that is to be validated. The rules field represents the rules that are to be validated. The assert field represents the expected result. If the value is ```true``` then the solution expects the result from the solver to be ```true``` as well. If the value is ```false``` then the solution expects the result from the solver to be ```false``` as well.
