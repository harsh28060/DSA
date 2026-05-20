class MyHashSet:

    def __init__(self):
        self.data = []

    def add(self, key: int) -> None:
        if key not in self.data:
            self.data.append(key)

    def remove(self, key: int) -> None:
        if key in self.data:
            self.data.remove(key)        

    def contains(self, key: int) -> bool:
        return key in self.data

# Driver Code
obj = MyHashSet()

obj.add(1)
obj.add(2)

print(obj.contains(1))   # True
print(obj.contains(3))   # False

obj.add(2)

print(obj.contains(2))   # True

obj.remove(2)

print(obj.contains(2))   # False