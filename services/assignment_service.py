import random
from typing import List, Tuple, Dict

MAX_ATTEMPTS = 10_000

def create_secret_santa_assignments(
    employees: List[Tuple[str, str]],
    last_year_assignments: Dict[Tuple[str, str], Tuple[str, str]]
) -> Dict[Tuple[str, str], Tuple[str, str]]:

    n = len(employees)
    if n < 2:
        raise ValueError("At least 2 employees are required for Secret Santa.")

    for attempt in range(MAX_ATTEMPTS):
        children = random.sample(employees, n)
        assignment = {}
        valid = True

        for i, parent in enumerate(employees):
            child = children[i]
            if parent == child:
                valid = False
                break
            if last_year_assignments.get(parent) == child:
                valid = False
                break

            assignment[parent] = child

        if valid:
            return assignment

    raise ValueError(f"Could not find valid assignment after {MAX_ATTEMPTS} attempts.")
