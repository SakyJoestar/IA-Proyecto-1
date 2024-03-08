from Action import Action
from Puzzle import Puzzle

class Node (object):
    def __init__(self, puzzle: Puzzle, action: Action, parent: 'Node', depth: int, cost: int):
        self.puzzle = puzzle
        self.action = action
        self.parent = parent
        self.depth = depth
        self.cost = cost

    def getPossibleActions(self) -> list[Action]:
        possibleActions = []
        parentPosition = self.parent.puzzle.actualPosition if self.parent is not None else (-1, -1)
        if self.puzzle.isValidMove(Action.UP, parentPosition):
            possibleActions.append(Action.UP)
        if self.puzzle.isValidMove(Action.DOWN, parentPosition):
            possibleActions.append(Action.DOWN)
        if self.puzzle.isValidMove(Action.LEFT, parentPosition):
            possibleActions.append(Action.LEFT)
        if self.puzzle.isValidMove(Action.RIGHT, parentPosition):
            possibleActions.append(Action.RIGHT)

        return possibleActions
    
    def applyAction(self, action: Action) -> 'Node':
        newPuzzle = self.puzzle.clone()
        newPuzzle.move(action)
        return Node(newPuzzle, action, self, self.depth + 1, self.cost + 1)
    
    def isGoal(self) -> bool:
        return self.puzzle.isGoal()