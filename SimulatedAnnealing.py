########################################
# CS63: Artificial Intelligence, Lab 2
# Fall 2020, Swarthmore College
########################################

from math import exp
import random

def simulated_annealing(problem, runs, steps, init_temp, temp_decay):
    """Implementes the simulated annealing local search algorithm.
    inputs:
        - problem: A TSP or VRP instance.
        - runs: The number of times to start from a random initial candidate.
        - steps: The number of moves to make in a given run.
        - init_temp: Initial temperature for the start of each run. This should
                scale linearly relative to the cost of a typical candidate.
        - temp_decay: The multiplicative factor by which temperature is reduced
                on each step.
    returns: best_candidate, best_cost
        The best candidate identified by the search and its cost.

    NOTE: In this case, you should always call random_neighbor(), rather than
          get_neighbor() or all_neighbors().
    """
    best_state = problem.random_candidate()
    best_cost = problem.cost(best_state)
    step_counter = 0
    for i in range(runs):
        temp=init_temp
        curr_state = problem.random_candidate()
        curr_cost = problem.cost(curr_state)
        for j in range(steps):
            neighbor_state, neighbor_cost = problem.get_neighbor(curr_state)
            step_counter += 1
            delta=curr_cost-neighbor_cost
            if delta > 0 or random.random()<exp(delta/temp):
               curr_state = neighbor_state
               curr_cost = neighbor_cost
            if curr_cost < best_cost:
                best_state = curr_state
                best_cost = curr_cost
                print("Step:(%d) Best cost:(%f)" %(step_counter, best_cost))
            temp*=temp_decay
    return best_state, best_cost
