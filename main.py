from Algorithms import *
from Models import *


if __name__ == "__main__":
    file_dir = "./Tests/Prueba3.txt"
    expanded_nodes, depth, total_time, cost, path = execute_cost_search(file_dir)

    map = Reader.read_map(file_dir)

    (y, x) = Agent.find_agent(map)
    agent = Agent(y, x)

    env = Environment(650, 750, map, agent)
    env.display_environment(expanded_nodes, depth, round(total_time, 6), cost, path)
