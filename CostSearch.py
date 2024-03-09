import time
from Node import Node
from Puzzle import Puzzle


def pathGoal(node):
    path = []
    while node.parent != None:
        path.append(node.puzzle.actualPosition)
        node = node.parent
    path.reverse()
    return path


def minCostNode(queueNodes):
    minCost = queueNodes[0].cost
    minIndex = 0

    for i in range(1, len(queueNodes)):
        if queueNodes[i].cost < minCost:
            minCost = queueNodes[i].cost
            minIndex = i

    return minIndex


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

        index = minCostNode(queueNodes)
        node = queueNodes[index]
        possibleActions = node.getPossibleActions()

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

        del queueNodes[index]


main()
