def bonus_time(salary, bonus):
    new_salary = salary
    if bonus == True:
        new_salary *= 10
    elif bonus == False:
        new_salary *= 1
    return (f"${new_salary}")
        