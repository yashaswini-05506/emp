def employee_details(name, empid, department, salary):
    result = (
        f"Employee Name: {name}\n"
        f"Employee Id: {empid}\n"
        f"Department: {department}\n"
        f"Salary: {salary}\n"
    )
    return result

if __name__ == "__main__":
    name = "Alice"
    empid = "E1001"
    department = "IT"
    salary = 50000   # Added salary value
    print(employee_details(name, empid, department, salary))