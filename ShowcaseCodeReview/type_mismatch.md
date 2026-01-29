# Issues in type_mismatch.py

This file demonstrates **type mismatches and incompatible operations** that mypy will flag.

## Mypy Issues:

1. **Type mismatch in `add_numbers` call**: Passing `str` ("5") where `int` is expected.

2. **Type mismatch in `process_string` call**: Passing `int` (123) where `str` is expected.

3. **Type mismatch in `calculate_average` call**: Passing `list[str]` where `list[int]` is expected.

4. **Type mismatch in `get_first_item` call**: Passing `list[int]` where `list[str]` is expected.

5. **Incompatible operation**: Adding `str` and `int` directly without conversion.

6. **Incompatible operation**: Calling `.upper()` method on an `int` (which doesn't have this method).

7. **Mypy messages you'll see**:
   - `error: Argument 1 to "add_numbers" has incompatible type "str"; expected "int"`
   - `error: Argument 1 to "process_string" has incompatible type "int"; expected "str"`
   - `error: Argument 1 to "calculate_average" has incompatible type "list[str]"; expected "list[int]"`
   - `error: Unsupported operand types for + ("str" and "int")`
   - `error: "int" has no attribute "upper"`

## How to fix:

- Ensure argument types match function parameter types
- Convert types explicitly when needed (e.g., `int("5")`, `str(123)`)
- Use proper type annotations and let mypy catch errors early
- Avoid calling methods that don't exist on the given type
- Use type guards or isinstance checks when dealing with union types
