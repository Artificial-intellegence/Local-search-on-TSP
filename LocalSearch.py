#! /usr/bin/env python3
########################################
# CS63: Artificial Intelligence, Lab 2
# Fall 2020, Swarthmore College
########################################
# NOTE: you should not need to modify this file.
########################################

import json
from argparse import ArgumentParser

from TSP import TSP
from VRP import VRP
from HillClimbing import hill_climbing
from SimulatedAnnealing import simulated_annealing
from BeamSearch import stochastic_beam_search

def parse_input():
    parser = ArgumentParser()
    parser.add_argument("search", choices=["HC","SA","BS"],
                        help="Local search algorithm to use: HC, SA, or BS")
    parser.add_argument("problem", choices=["TSP","VRP"],
                        help="Type of problem to solve: TSP or VRP.")
    parser.add_argument("coordinates", type=str,\
                        help="JSON file with city coordinates.")
    parser.add_argument("-config", type=str, default="default_config.json",\
                        help="JSON file with search and problem parameters.")
    parser.add_argument("-plot", type=str, default="map.pdf",\
                        help="Filename for map output.")
    args = parser.parse_args()
    with open(args.config) as f:
        config = json.load(f)
    args.search_args = config[args.search]
    args.problem_args = config[args.problem]
    return args

def main():
    args = parse_input()
    if args.problem == "TSP":
        problem = TSP(args.coordinates, **args.problem_args)
    if args.problem == "VRP":
        problem = VRP(args.coordinates, **args.problem_args)
    if args.search == "HC":
        search_alg = hill_climbing
    if args.search == "SA":
        search_alg = simulated_annealing
    if args.search == "BS":
        search_alg = stochastic_beam_search
    solution, cost = search_alg(problem, **args.search_args)
    if args.problem == "TSP":
        print("route:")
        print(solution)
    if args.problem == "VRP":
        print("routes:")
        for i,tour in enumerate(solution):
            print(str(i+1)+":",tour)
    print("cost:", cost)
    problem.plot(solution, args.plot)

if __name__ == "__main__":
    main()
