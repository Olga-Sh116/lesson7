class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("Этот метод должен быть переопределен в подклассе")

    def eat(self):
        print(f"{self.name} ест.")
class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        print(f"{self.name} чирикает.")

    def fly(self):
        print(f"{self.name} летает с размахом крыльев {self.wing_span} метров.")


class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print(f"{self.name} рычит.")

    def walk(self):
        print(f"{self.name} ходит с красивой {self.fur_color} шерстью.")


class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type

    def make_sound(self):
        print(f"{self.name} шипит.")

    def crawl(self):
        print(f"{self.name} ползает с {self.scale_type} чешуей.")
def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

# Пример использования
animals = [
    Bird("Попугай", 2, 0.5),
    Mammal("Тигр", 5, "оранжевый"),
    Reptile("Змея", 3, "скользкая")
]

animal_sound(animals)
