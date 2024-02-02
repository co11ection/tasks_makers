def func16(distance: float, fuel: float) -> str:
    return "На 100км было расходовано %dл горючего" % round(fuel / distance * 100)
