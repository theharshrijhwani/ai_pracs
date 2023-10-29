import random


def obj_func(x):
    return -x**2


def hillClimb(max_it, step_size, x):
    for _ in range(max_it):
        curr_val = obj_func(x)
        nxt_x = x + random.uniform(-step_size, step_size)
        nxt_val = obj_func(nxt_x)

        if nxt_val > curr_val:
            x = nxt_val

    return x


max_it = 1000
step_size = 0.1
init_x = 5.0


optimal_soln = hillClimb(max_it, step_size, init_x)

print(f"Optimal solution is: {optimal_soln}")
print(f"f(x) = {obj_func(optimal_soln)}")
