class A:

    def public(self) -> str:
        return "Public method"


    def _protected(self) -> str:
        return "Protected method"


    def __private(self) -> str:
        return "Private method"


obj1 = A()

print(obj1.public)
print(obj1._protected)
print(obj1._A__private)
