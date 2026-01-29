# Issues in missing_annotations.py

This file demonstrates **missing type annotations and inconsistent return types** that mypy will flag.

## Mypy Issues:

1. **Missing type annotations**: All functions lack type hints, making it unclear what types are expected and returned.

2. **Inconsistent return types in `get_user_info`**: Returns `dict`, `str`, or `None` depending on the condition, which violates type consistency.

3. **Missing annotations lead to type errors**: Without annotations, mypy cannot catch type mismatches like passing `int` where `str` is expected in `format_message`.

4. **Unclear parameter types**: Functions like `calculate_total` and `combine_values` don't specify what types they accept, leading to potential runtime errors.

5. **Mypy messages you'll see**:
   - `error: Function is missing a type annotation`
   - `error: Incompatible return value type (got "str", expected "dict[str, Any]")`
   - `error: Incompatible types in assignment (expression has type "str | dict[str, Any] | None", variable has type "dict[str, Any]")`
   - `error: Argument 1 to "format_message" has incompatible type "int"; expected "str"`
   - `error: Unsupported operand types for + ("str" and "int")`

## How to fix:

- Add type annotations to all function parameters and return types
- Use `typing` module for complex types (e.g., `Optional`, `Union`, `Dict`, `List`)
- Ensure consistent return types, or use `Union` if multiple types are intentional
- Use `Optional[T]` or `T | None` for functions that can return `None`
- Enable strict mypy checking to catch these issues early
- Consider using `Protocol` or `TypeVar` for generic functions
