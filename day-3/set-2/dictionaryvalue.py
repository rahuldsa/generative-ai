employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

new_dict = {emp: defaults.copy() for emp in employees}

print(new_dict)
