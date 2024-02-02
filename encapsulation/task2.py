class A:

    def method1(self) -> None:
        print("Hello World")


class B(A):
    pass


b1 = B()

b1.method1()
