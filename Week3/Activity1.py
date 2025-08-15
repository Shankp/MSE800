

class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, 'r', encoding='utf-8') as file:
            content = file.read()
            return content

    def write(self, data):
        with open(self.filename, 'a', encoding='utf-8') as file:
            file.write(data + '\n')
            print(f"Data written to {self.filename}")

def main():
    file = FileHandler('demo.txt')
    print("Reading file content:")   
    print(file.read())
    print("\nWriting to file:")
    file.write("\nThis is a new line in the file.")

if __name__ == "__main__":
    main()