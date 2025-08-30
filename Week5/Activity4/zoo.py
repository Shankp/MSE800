class Color:
    def get_color(self):
        return "unknown"

class TransparentColor(Color):
    def get_color(self):
        return "transparent"

class Animal:
    def __init__(self, name, color: Color):
        self.name = name
        self.color = color

    def get_animal_color(self):
        return self.color.get_color()

def main():
    color = Color()
    unknown = Animal("mammal", color)
    print(f"{unknown.name} color: {unknown.get_animal_color()}")

    transparent_color = TransparentColor()
    fish = Animal("Goldfish", transparent_color)
    print(f"{fish.name} color: {fish.get_animal_color()}")

if __name__ == "__main__":
    main()
