class Animal:
    pass

class Cat(Animal):
    pass

animal: Animal = Cat()
cats: list[Cat] = []

# Type alias
CatList = list[Cat]
cats: CatList = []

# Forward reference
class Dog(Animal):
    @staticmethod
    def create() -> 'Dog':
        return Dog()

    @staticmethod
    def get_list() -> list['Dog']:
        return []
