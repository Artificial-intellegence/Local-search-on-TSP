########################################
# CS63: Artificial Intelligence, Lab 2
# Fall 2020, Swarthmore College
########################################

from math import exp
from numpy.random import choice, multinomial#You should only need one of these.

def stochastic_beam_search(problem, pop_size, steps, init_temp, temp_decay, \
                           max_neighbors):
    """Implementes the stochastic beam search local search algorithm.
    inputs:
        - problem: A TSP or VRP instance.
        - pop_size: Number of candidates tracked.
        - steps: The number of moves to make in a given run.
        - init_temp: Initial temperature. Note that temperature has a slightly
                different interpretation here than in simulated annealing.
        - temp_decay: The multiplicative factor by which temperature is reduced
                on each step. The temperature parameters should be chosen such
                that e^(-cost / temp) never reaches 0.
        - max_neighbors: Number of neighbors generated each round for each
                candidate in the population.
    returns: best_candidate, best_cost
        The best candidate identified by the search and its cost.

    NOTE: In this case, you should always call random_neighbor(), rather than
          get_neighbor() or all_neighbors().
    """
    best_state = problem.random_candidate()
    best_cost = problem.cost(best_state)
    listOfCandidates=[]
    for i in range(pop_size):
        listOfCandidates.append(problem.random_candidate())
    step_counter = 0
    temp = init_temp
    for i in range(steps):
        step_counter += 1
        list=getNextStates(problem,max_neighbors,listOfCandidates)
        best_candidate_state=list[0]
        best_candidate_cost=list[1]
        listOfNextGeneration=list[2]
        if best_candidate_cost < best_cost:
            best_state = best_candidate_state
            best_cost = best_candidate_cost
            print("Step:(%d) Best cost:(%f)" %(step_counter, best_cost))
        prob_list=nextGenProb(listOfNextGeneration,temp)
        if prob_list == None:
            return best_state, best_cost
        indices = []
        for i in range(len(listOfNextGeneration)):
            indices.append(i)
        choices = choice(indices, pop_size, prob_list)
        chosenNextGen = []
        for i in choices:
            chosenNextGen.append(listOfNextGeneration[i][0])
        listOfCandidates=chosenNextGen
        temp*=temp_decay
    return best_state, best_cost

def getNextStates(problem,max_neighbors,listOfCandidates):
    listOfNextGeneration=[]
    best_cost=float('inf')
    best_state=0
    for candidate in listOfCandidates:
        for i in range(max_neighbors):
            neighbor_state, neighbor_cost = problem.random_neighbor(candidate)
            listOfNextGeneration.append((neighbor_state, neighbor_cost))
            if neighbor_cost < best_cost:
                best_state = neighbor_state
                best_cost = neighbor_cost
    return [best_state,best_cost,listOfNextGeneration]

def nextGenProb(listOfNextGeneration,temp):
    total_cost=0
    exp_list=[]
    for state,cost in listOfNextGeneration:
        exp_list.append(exp((-1)*cost/temp))
        total_cost+=exp((-1)*cost/temp)
    prob_list=[]
    for i in exp_list:
        if total_cost == 0:
            return None
        prob_list.append(i/total_cost)
    return prob_list
