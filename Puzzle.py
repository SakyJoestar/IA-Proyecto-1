from Action import Action

class Puzzle (object):
    def __init__(self, board = [], actualPosition = None, goalPosition = None, size = 0, zero = 0):
        self.board = board
        self.actualPosition = actualPosition
        self.goalPosition = goalPosition
        self.size = size
        self.zero = zero

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(str(self.board))

    def __str__(self):
        return '\n'.join([str(self.board[i:i + self.size]) for i in range(0, len(self.board), self.size)])

    def __getitem__(self, index):
        return self.board[index]

    def __setitem__(self, index, value):
        self.board[index] = value

    def loadMap(self, file: str) -> None:
        with open(file, 'r') as f:
            auxMap = f.read().splitlines()
        mapString = [''.join(fila.split()) for fila in auxMap]
        map = [list(fila) for fila in mapString]
        self.size = len(map)
        self.board = map
        self.definePosition(map)
    
    def definePosition(self, map: list) -> None:
        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j] == '2':
                    self.actualPosition = (i, j)
                elif map[i][j] == '5':
                    self.goalPosition = (i, j)

    def isValidPosition(self, row, col, parentPosition) -> bool:
        isReturnParent = (row, col) == parentPosition
        isOutOfBoard = row < 0 or row >= self.size or col < 0 or col >= self.size
        isWall = self.board[row][col] == '1' if not isOutOfBoard else False

        return not isReturnParent and not isOutOfBoard and not isWall

    def isValidMove(self, action: Action, parentPosition: tuple[int, int]) -> bool:
        y, x = self.actualPosition

        moveUp = (y - 1, x)
        moveDown = (y + 1, x)
        moveLeft = (y, x - 1)
        moveRight = (y, x + 1)

        if action == Action.UP:
            return self.isValidPosition(moveUp[0], moveUp[1], parentPosition)
        elif action == Action.DOWN:
            return self.isValidPosition(moveDown[0], moveDown[1], parentPosition)
        elif action == Action.LEFT:
            return self.isValidPosition(moveLeft[0], moveLeft[1], parentPosition)
        elif action == Action.RIGHT:
            return self.isValidPosition(moveRight[0], moveRight[1], parentPosition)
        else:
            return False
        
    def move(self, action: Action) -> 'Puzzle':
        y, x = self.actualPosition

        if action == Action.UP:
            newRow, newCol = y - 1, x
        elif action == Action.DOWN:
            newRow, newCol = y + 1, x
        elif action == Action.LEFT:
            newRow, newCol = y, x - 1
        elif action == Action.RIGHT:
            newRow, newCol = y, x + 1

        self.board[y][x] = '0'
        self.board[newRow][newCol] = '2'
        self.actualPosition = (newRow, newCol)
        
    def clone(self) -> 'Puzzle':
        return Puzzle(self.board[:], self.actualPosition, self.goalPosition, self.size, self.zero)
    
    def isGoal(self) -> bool:
        return self.actualPosition == self.goalPosition