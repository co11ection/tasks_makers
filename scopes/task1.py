def foo() -> None:
    var = "переменная foo"


    def bar() -> None:
        global var

        var = "переменная bar"


    print("переменная в foo: ", var)
    bar()


foo()
print("переменная в foo: ", var)
