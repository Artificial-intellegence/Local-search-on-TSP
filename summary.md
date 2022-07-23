# Comparing local search methods

You should pick one test case, such as `Lower_48.json`, and do multiple runs for each local search. Be sure to experiment with the default parameter settings to try to get the best results you can.  Then run at least 3 experiments using each search method.

We tested the algorithms on the 'United_States_25.json' map.

| HC     | Best Cost |
| ------ | --------- |
| run 1  |  147.999  |
| run 2  |  149.046  |
| run 3  |  147.999  |
| Avg    |  148.348  |

HC parameters:    "runs":3,
                  "steps":500,
                  "rand_move_prob": 0.25

| SA     | Best Cost |
| ------ | --------- |
| run 1  |  147.999  |
| run 2  |  147.999  |
| run 3  |  148.005  |
| Avg    |  148.001  |

SA parameters:      "runs":3,
                    "steps":500,
                    "init_temp":100,
                    "temp_decay":1.2

| BS     | Best Cost |
| ------ | --------- |
| run 1  |  296.168  |
| run 2  |  273.257  |
| run 3  |  275.630  |
| Avg    |  281.685  |

BS parameters:  "pop_size":500,
                "steps":500,
                "init_temp":200,
                "temp_decay":0.99,
                "max_neighbors":3

Which local search algorithm (HC, SA, or BS) most consistently finds the best tours and why do you think it outperforms the others?

SA most consistently finds the best tours on this map. HC also performs quite well and finds tours with costs in a very tightly
bounded range. However, BS does extremely poorly here (almost twice the avg cost!), and this was also the case on the India_15 map. We hypothesize this is the
case due to the smaller search space of the map we chose to experiment on. BS has the tendency to converge too quickly on suboptimal areas
of the search space. In a smaller search space, each subsequent generation is more likely to be clustered together simply due to the size of
the space - despite randomness in the process that comes up with the next generation, it is easier for BS to more quickly converge on
suboptimal areas than HC and SA in smaller search spaces, hence the large performance disparities we have demonstrated above.
