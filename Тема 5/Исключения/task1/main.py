def add_func(a: int, b: int) -> int:
    if not isinstance(a, int):
        raise TypeError(f"У переменной a должен быть тип int, не {type(a)}")
    if not isinstance(b, int):
        raise TypeError(f"У переменной b должен быть тип int, не {type(b)}")

    if not a > 0:
        raise ValueError("Число a должно быть положительным.")
    if b <= 0:
        raise ValueError("Число b должно быть положительным.")

    return a + b


add_func(1, 1)
