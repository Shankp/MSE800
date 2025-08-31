#LibraryItem is base class of the book items
class LibraryItem:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_book_details(self):
        return f"title : {self.title}, author : {self.author}"

#Child class that inherits method from Library item parent class
class Book(LibraryItem):              
    def __init__(self, title, author):
        super().__init__(title, author)
        self.title = title
        self.author = author

    def get_book_details(self):
        return f"title : {self.title}, author : {self.author}"

#Child class that inherits method from Library item parent class
class Magazine(LibraryItem):
    def __init__(self, title, author, issue_frequency):
        super().__init__(title, author)
        self.title = title
        self.author = author
        self.issue_frequency = issue_frequency

    def get_magazine_details(self):
        return f"\Magazine: title : {self.title}, author : {self.author}, issue frequency : {self.issue_frequency}"


class Libray:
    def __init__(self):
        self.booklist = []
        self.magazine_list = []

    def add_book(self, book: Book): 
        self.booklist.append(book)

    def add_Magazine(self, magazine: Magazine):
        self.magazine_list.append(magazine)

    def display_books(self):
        return self.magazine_list

    def display_magazines(self):
        return self.magazine_list


def main():
    """
    Main function to demonstrate the usage of the Library management system.
    This function performs the following steps::
    1. Initializes a Library instance.
    2. Creates a Book and a Magazine object with sample data.
    3. Adds the Book and Magazine to the Library.
    4. Retrieves and displays the list of books and magazines in the Library, printing their details.
    Returns:
        None
    """
    library = Libray()
    book = Book("city and rain", "John Foe")
    magazine = Magazine("city and rain", "John Foe", 10)
    library.add_book(book)
    library.add_Magazine(magazine)

    bookList = library.display_books()
    for book in bookList:
        print(f"\nBook: title : {book.title}, author : {book.author}")
    magazineList = library.display_magazines()
    for magazine in magazineList:
        print(f"\nMagazines: title : {magazine.title}, author : {magazine.author}, issue frequency : {magazine.issue_frequency}")


if __name__ == "__main__":
    main()
