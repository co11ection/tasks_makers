class A:
    
    def method1(self) -> None:
        print("Основной функционал")


class B(A):

    def method1(self) -> None:
        super().method1()
        print("Дополнительный функционал")


obj = B()

obj.method1()
