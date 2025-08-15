class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        count = 0
        with open(self.filename, 'r', encoding='utf-8') as file:
            content = file.read()
            w = content.strip().split()    
            count += len(w)
            file.close()
            return count

    

def main():
    file = FileHandler('demo.txt')
    print("Reading file content:")   
    print("Number of words in the file : " + str(file.read()))
    

if __name__ == "__main__":
    main()