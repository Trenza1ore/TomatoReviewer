def process_data(data):
    return data * 2


def get_user_info(user_id):
    if user_id == 1:
        return {"name": "John", "age": 30}
    elif user_id == 2:
        return "Jane"
    else:
        return None


def calculate_total(items):
    total = 0
    for item in items:
        total += item
    return total


def format_message(name, age):
    return f"{name} is {age} years old"


def combine_values(a, b):
    return a + b


def main():
    result1 = process_data(5)
    print(result1)

    info1 = get_user_info(1)
    info2 = get_user_info(2)
    info3 = get_user_info(3)
    print(info1, info2, info3)

    total = calculate_total([1, 2, 3, 4, 5])
    print(total)

    message = format_message(123, "thirty")
    print(message)

    combined = combine_values("hello", 42)
    print(combined)


if __name__ == "__main__":
    main()
