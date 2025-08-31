class LibraryItem:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_book_details(self):
        return f"title : {self.title}, author : {self.author}"


class Book(LibraryItem):
    def __init__(self, title, author):
        super().__init__(title, author)
        self.title = title
        self.author = author

    def get_book_details(self):
        return f"title : {self.title}, author : {self.author}"


class Magazine(LibraryItem):
    def __init__(self, title, author, issue_frequency):
        super().__init__(title, author)
        self.title = title
        self.author = author
        self.__issue_frequency = issue_frequency

    def get_magazine_details(self):
        return f"\Magazine: title : {self.title}, author : {self.author}, issue frequency : {self.__issue_frequency}"


class Libray:
    def __init__(self):
        self.booklist = []
        self.magazine_list = []

    def add_book(self, book: Book):
        self.booklist.append(book)

    def add_Magazine(self, magazine: Magazine):
        self.magazine_list.append(magazine)

    def display_books(self):
        for book in self.booklist:
            print(f"\nBook: title : {book.title}, author : {book.author}")

    def display_magazines(self):
        for magazine in self.magazine_list:
            print(magazine.get_magazine_details())


def main():
    library = Libray()
    book = Book("city and rain", "John Foe")
    magazine = Magazine("city and rain", "John Foe", 10)
    library.add_book(book)
    library.add_Magazine(magazine)

    library.display_books()
    library.display_magazines()


if __name__ == "__main__":
    main()
