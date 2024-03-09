from Node import Node
from Puzzle import Puzzle


def pathGoal(node):
    path = []
    while node.parent != None:
        path.append(node.puzzle.actualPosition)
        node = node.parent
    path.reverse()
    return path


def main():
    queueNodes = []
    index = 0

    puzzle = Puzzle()
    puzzle.loadMap("Prueba1.txt")
    intitialNode = Node(puzzle, None, None, 0, 0)

    queueNodes.append(intitialNode)

    while True:
        if index >= len(queueNodes):
            print("No solution found")
            break

        node = queueNodes[index]
        possibleActions = node.getPossibleActions()
        index += 1

        if node.isGoal():
            print("Goal found")
            print(node.puzzle.actualPosition)
            print("Cost: ", node.cost)
            print("Depht: ", node.depth)
            print("Path: ", pathGoal(node))
            break

        for action in possibleActions:
            newNode = node.applyAction(action)
            queueNodes.append(newNode)


main()
