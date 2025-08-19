def add(a: int, b: int) -> int:
    return a + b

def divide(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

if __name__ == "__main__":
    print("Add 2 + 3 =", add(2, 3))
    print("Divide 10 / 2 =", divide(10, 2))
