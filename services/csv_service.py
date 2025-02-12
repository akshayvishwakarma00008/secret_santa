import csv
import os
from typing import List, Tuple, Dict


def read_employees(csv_file_path: str) -> List[Tuple[str, str]]:
    employees = []
    if not os.path.isfile(csv_file_path):
        raise FileNotFoundError(f"Could not find file: {csv_file_path}")

    try:
        with open(csv_file_path, mode='r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            for row in reader:
                name = row["Employee_Name"].strip()
                email = row["Employee_EmailID"].strip()
                employees.append((name, email))
    except KeyError:
        raise KeyError("CSV file must include 'Employee_Name' and 'Employee_EmailID' columns.")

    return employees


def read_last_year_assignments(csv_file_path: str) -> Dict[Tuple[str, str], Tuple[str, str]]:
    if not os.path.isfile(csv_file_path):
        return {}

    assignments = {}
    try:
        with open(csv_file_path, mode='r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            for row in reader:
                p_name = row["Employee_Name"].strip()
                p_email = row["Employee_EmailID"].strip()
                c_name = row["Secret_Child_Name"].strip()
                c_email = row["Secret_Child_EmailID"].strip()
                assignments[(p_name, p_email)] = (c_name, c_email)
    except KeyError:
        raise KeyError(
            "CSV file must have 'Employee_Name','Employee_EmailID',"
            "'Secret_Child_Name','Secret_Child_EmailID' columns."
        )

    return assignments


def write_assignments(
    output_csv_file_path: str,
    assignments: Dict[Tuple[str, str], Tuple[str, str]]
) -> None:
    fieldnames = ["Employee_Name", "Employee_EmailID", "Secret_Child_Name", "Secret_Child_EmailID"]
    with open(output_csv_file_path, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for (parent_name, parent_email), (child_name, child_email) in assignments.items():
            writer.writerow({
                "Employee_Name": parent_name,
                "Employee_EmailID": parent_email,
                "Secret_Child_Name": child_name,
                "Secret_Child_EmailID": child_email
            })
