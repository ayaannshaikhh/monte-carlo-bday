# Birthday Problem Monte Carlo Simulation

This project estimates the probability that **at least two people in a group share the same birthday** using a **Monte Carlo simulation** in Python.

Instead of computing the probability mathematically, this program repeatedly simulates random birthdays and measures how often a duplicate occurs.

---

## Overview

The simulation works by:

1. Generating random birthdays for `N` people
2. Checking whether any birthdays are duplicated
3. Repeating this process many times
4. Estimating probability as:

probability ≈ (number of successful trials) / (total trials)

---

## How It Works

### `run_simulation(args)`
Generates random birthdays for a group of people.

- `num_people`: number of people in the group
- `days_in_year`: number of possible birthdays (default typically 365)

Returns a list of randomly generated birthdays.

---

### `is_success(result)`
Checks whether **at least one duplicate birthday exists** in the simulation.

It compares:
- length of the list
- length of the set version of the list

If they differ, a duplicate exists.

---

### `monte_carlo(num_trials, args)`
Runs the simulation multiple times and computes the estimated probability.

Default number of trials:
```
100000
```

More trials → more accurate estimate.

---

### `monte_carlo_bday_problem(n, days_in_year=365)`
Convenience function for running the birthday problem simulation.

Example:
```python
monte_carlo_bday_problem(25)
```

---

## Running the Program

Make sure Python 3.9+ is installed.

Run:

```bash
python main.py
```

Example output:

```
0.568
```

This means there is approximately a **56.8% chance** that at least two people in a group of 25 share a birthday.

---

## Example Code

```python
# 25 is the number of people we're using
print(monte_carlo_bday_problem(25))
```

---

## Notes

- Birthdays are assumed to be **uniformly distributed**
- Leap years are ignored unless `days_in_year` is changed
- Simulation accuracy improves with more trials

---
