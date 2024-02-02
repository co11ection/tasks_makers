def to_fahrenheit(k: int) -> float:
    assert k > 0, "Холоднее абсолютного нуля!"

    return (k - 273.15) * 9 / 5 + 32
