def add_(num1: float, num2: float) -> float:
    return num1 + num2


def sub_(num1: float, num2: float) -> float:
    return num1 - num2


def div_(num1: float, num2: float) -> float:
    return num1 / num2


def mult_(num1: float, num2: float) -> float:
    return num1 * num2


def calc(num1: float, num2: float, operation: str) -> float:
    match operation:
        case "+":
            return add_(num1, num2)
        case "-":
            return sub_(num1, num2)
        case "/":
            return div_(num1, num2)
        case "*":
            return mult_(num1, num2)
