class A:
    name="Class A"

class B:
    name="Class B"


class C(B,A):
    pass

object=C()

print(object.name)


