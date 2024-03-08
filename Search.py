from Node import Node
from Puzzle import Puzzle


def main():
    queueNodes = []
    index = 0

    puzzle = Puzzle()
    puzzle.loadMap('Prueba1.txt')
    intitialNode = Node(puzzle, None, None, 0, 0)

    queueNodes.append(intitialNode)

    while True:
        if index >= len(queueNodes):
            print('No solution found')
            break

        node = queueNodes[index]
        possibleActions = node.getPossibleActions()
        index += 1

        if node.isGoal():
            print('Goal found')
            print(node.puzzle.actualPosition)
            break

        for action in possibleActions:
            newNode = node.applyAction(action)
            queueNodes.append(newNode)

        






main()
