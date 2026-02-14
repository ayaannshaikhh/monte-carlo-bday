import random

def run_simulation(args: dict) -> list[int]:
    N = args["num_people"]
    days = args["days_in_year"]
    return [random.randint(1, days) for _ in range(N)]

def is_success(result: list[int]) -> bool:
    return len(result) != len(set[int](result))

def monte_carlo(num_trials: int = 100000, args: dict = {}) -> float:
    successes = 0

    for _ in range(num_trials):
        results = run_simulation(args)
        if is_success(results):
            successes += 1

    return successes / num_trials

def monte_carlo_bday_problem(n: int, days_in_year: int = 365) -> float:
    return monte_carlo(args={"num_people": n, "days_in_year": days_in_year})

# 25 is the number of people we're using
print(monte_carlo_bday_problem(25))
