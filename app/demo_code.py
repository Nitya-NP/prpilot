def calculate_average(numbers):
    total = 0
    for n in numbers:
        total = total + n
    average = total / len(numbers)
    return average

def get_user(id):
    user = database.find(id)
    print(user.name)
    return user
