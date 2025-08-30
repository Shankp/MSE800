class Color:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color


class TransparentColor(Color):
    def __init__(self, color):
        super().__init__(color)

    def get_color(self):
        return self.color


class Animal:
    def __init__(self, name, color: Color):
        self.name = name
        self.color = color

    def get_animal_color(self):
        return self.color.get_color()


def main():
    color = Color("Black")
    mammal = Animal("Mammal", color)
    print(f"{mammal.name} color: {mammal.get_animal_color()}")

    transparent_color = TransparentColor("transparent")
    fish = Animal("Goldfish", transparent_color)
    print(f"{fish.name} color: {fish.get_animal_color()}")


if __name__ == "__main__":
    main()
