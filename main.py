import os
from services.csv_service import (
    read_employees, read_last_year_assignments, write_assignments
)
from services.assignment_service import create_secret_santa_assignments

def main():
    # Adjust paths as needed
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    employees_csv = os.path.join(BASE_DIR, "data", "employees.csv")
    last_year_csv = os.path.join(BASE_DIR, "data", "last_year_assignments.csv")
    output_csv = os.path.join(BASE_DIR, "secret_santa_assignments.csv")

    # 1. Read employees
    employees = read_employees(employees_csv)

    # 2. Read last year's assignments
    last_year_assignments = read_last_year_assignments(last_year_csv)

    # 3. Create new assignments
    try:
        new_assignments = create_secret_santa_assignments(employees, last_year_assignments)
    except ValueError as err:
        print(f"ERROR: {err}")
        return

    # 4. Write assignments to CSV
    write_assignments(output_csv, new_assignments)
    print(f"Secret Santa assignments saved to {output_csv}")

if __name__ == "__main__":
    main()
