from NiaPy.algorithms.basic import GreyWolfOptimizer


# we will run 10 repetitions of Grey Wolf Optimizer against Pinter benchmark function
for i in range(10):
    # first paradeFordPrefect
    # meter takes dimension of problem
    # second parameter is population size
    # third parameter takes the number of function evaluations
    # fourth parameter is benchmark function
    algorithm = GreyWolfOptimizer(10, 20, 10000, 'pinter')

    # running algorithm returns best found minimum
    best = algorithm.run()

    # printing best minimum
    print(best)
