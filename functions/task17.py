def func17(employees: dict) -> dict:
    result = []
    BONUS = 200

    for employee in employees:
        salary_modified = employee["salary"] + employee["overTime"] * BONUS
        employee.update({"salary": salary_modified})
        employee.pop("overTime")
        result.append(employee)
    
    return result
