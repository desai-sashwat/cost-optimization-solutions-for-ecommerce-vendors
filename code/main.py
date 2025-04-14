import math

from numpy.random import rand
from numpy.random import choice
from numpy import asarray
from numpy import clip
from numpy import argmin
from numpy import min
from numpy import around


# define objective function
# f(x) = F(x) = Σi 1d-1 [100(xi+1 – xi2)2 + (xi – 1)2]
# f(x) = ∑(MC + TCi + PCm + PCp + TCo1 + TCo2 + TCc + ICw)

def obj(x):
    total = []
    for i in range(len(x)-1):
        total += 100 * math.pow((x[i+1] - math.pow(x[i], 2)), 2) + math.pow((x[i]-1), 2)
        #total += MC + TCi + PCm + PCp + TCo1 + TCo2 + TCc + ICw
    return total


# define mutation operation
def mutation(x, F):
    return x[0] + F * (x[1] - x[2])


# define boundary check operation
def check_bounds(mutated, bounds):
    mutated_bound = [clip(mutated[i], bounds[i, 0], bounds[i, 1]) for i in range(len(bounds))]
    return mutated_bound


# define crossover operation
def crossover(mutated, target, dims, cr):
    # generate a uniform random value for every dimension
    p = rand(dims)
    # generate trial vector by binomial crossover
    trial = [mutated[i] if p[i] < cr else target[i] for i in range(dims)]
    return trial


def differential_evolution(pop_size, bounds, iter, F, cr):
    # initialise population of candidate solutions randomly within the specified bounds
    pop = bounds[:, 0] + (rand(pop_size, len(bounds)) * (bounds[:, 1] - bounds[:, 0]))
    # evaluate initial population of candidate solutions
    obj_all = [obj(ind) for ind in pop]
    # find the best performing vector of initial population
    best_vector = pop[argmin(obj_all)]
    best_obj = min(obj_all)
    prev_obj = best_obj
    # run iterations of the algorithm
    for i in range(iter):
        # iterate over all candidate solutions
        for j in range(pop_size):
            # choose three candidates, a, b and c, that are not the current one
            candidates = [candidate for candidate in range(pop_size) if candidate != j]
            a, b, c = pop[choice(candidates, 3, replace=False)]
            # perform mutation
            mutated = mutation([a, b, c], F)
            # check that lower and upper bounds are retained after mutation
            mutated = check_bounds(mutated, bounds)
            # perform crossover
            trial = crossover(mutated, pop[j], len(bounds), cr)
            # compute objective function value for target vector
            obj_target = obj(pop[j])
            # compute objective function value for trial vector
            obj_trial = obj(trial)
            # perform selection
            if obj_trial < obj_target:
                # replace the target vector with the trial vector
                pop[j] = trial
                # store the new objective function value
                obj_all[j] = obj_trial
        # find the best performing vector at each iteration
        best_obj = min(obj_all)
        # store the lowest objective function value
        if best_obj < prev_obj:
            best_vector = pop[argmin(obj_all)]
            prev_obj = best_obj
            # report progress at each iteration
            print('Iteration: %d f([%s]) = %.5f' % (i, around(best_vector, decimals=5), best_obj))
    return [best_vector, best_obj]


# define population size
pop_size = 500
# define lower and upper bounds for every dimension
bounds = asarray([(-5.0, 5.0), (-5.0, 5.0)])
# define number of iterations
iter = 50
# define scale factor for mutation
F = 0.5
# define crossover rate for recombination
cr = 0.7

#Material Cost
MC = [
      [43.12 , 43.12 , 43.12],
      [43.12 , 43.12 , 43.12]
     ]

#Production Cost for Milk
PCm = [
       [5.70 , 5.70 , 5.70],
       [5.70 , 5.70 , 5.70]
      ]
#Production Cost for Other Products
PCp = [
       [1 , 1 , 1],
       [1 , 1 , 1]
      ]

#Inbound Transportation Cost
TCi = [
       [0.04 , 0.67 , 1.3],
       [0.03 , 0.47 , 0.91]
      ]

#Outbound Transportation Cost to Facility 1
TCo1 = [
        [0.05 , 0.9 , 1.75],
        [0.05 , 0.9 , 1.75]
       ]

#Outbound Transportation Cost to Facility 2
TCo2 = [
        [0.03 , 0.45 , 1.75],
        [0.03 , 0.45 , 0.87]
       ]

#Transportation Cost from Warehouse to Customer
TCc = [
        [11.9 , 13.16 , 8.9],
        [13.26 , 3 , 4.1]
       ]

#Inventory Cost at Warehouse
ICw = [
       [0.07 , 0.05 , 0.07],
       [0.07 , 0.05 , 0.07]
      ]

# perform differential evolution
solution = differential_evolution(pop_size, bounds, iter, F, cr)
print('\nSolution: f([%s]) = %.5f' % (around(solution[0], decimals=5), solution[1]))