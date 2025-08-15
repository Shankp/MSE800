
def read_file():
    with open('demo.txt', 'r', encoding='utf-8') as fileDate:
        content = fileDate.read()  # Read the entire file content
        print(content)
        fileDate.close()
        print("File has been read successfully.")

def write_file():
    with open('demo.txt', 'a', encoding='utf-8') as fileDate:
        fileDate.write("This is a new line in the file.\n")
        fileDate.close()
        print("File has been written successfully.")

def main():
    read_file()
    write_file()

if __name__ == "__main__":
    main()