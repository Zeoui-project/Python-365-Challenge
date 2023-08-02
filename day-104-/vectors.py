# vectors.py

class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"


# Testing Vector Class - TO BE DELETED
test = Vector(3, 5, 9)
print(test)
print(repr(test))

test = Vector(2, 2)
print(test)
print(repr(test))

test = Vector(y=5, z=3)
print(test)
print(repr(test))