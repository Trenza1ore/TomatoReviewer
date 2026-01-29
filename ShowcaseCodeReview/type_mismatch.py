def add_numbers(a: int, b: int) -> int:
    return a + b


def process_string(text: str) -> str:
    return text.upper()


def calculate_average(numbers: list[int]) -> float:
    return sum(numbers) / len(numbers)


def get_first_item(items: list[str]) -> str:
    return items[0]


def main():
    result1 = add_numbers("5", 10)
    print(result1)

    result2 = process_string(123)
    print(result2)

    result3 = calculate_average(["1", "2", "3"])
    print(result3)

    result4 = get_first_item([1, 2, 3])
    print(result4)

    value = "hello" + 42
    print(value)

    number = 123
    result5 = number.upper()
    print(result5)


if __name__ == "__main__":
    main()
