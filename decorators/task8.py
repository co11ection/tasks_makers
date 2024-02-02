def get_age(human: tuple) -> int:
    return human[2]


def sort_names(func):
    def wrapper(*args, **kwargs):
        people = args[0]
        people.sort(key=get_age)
        result = func(people)

        return result
    
    return wrapper


@sort_names
def prefix_name(people: list) -> list:
    result = []

    for human in people:
        gender = human[3]
        name = human[0]
        surname = human[1]
        
        if gender == "M":
            result.append(f"Mr. {name} {surname}")
        else:
            result.append(f"Ms. {name} {surname}")

    return result


print(
    prefix_name([
        ("Leo", "Nimoy", 40, "M"),
        ("Carrie", "Fisher", 35, "F"),
        ("Harrison", "Ford", 38, "M"),
    ])
)
