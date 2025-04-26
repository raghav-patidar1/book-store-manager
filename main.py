from bookstore.store import BookStore
from bookstore.utils import validate_field_type
from bookstore.exceptions import DuplicateBookError, BookNotFoundError

def get_book_input():
    try:
        title = input("Enter title: ")
        author = input("Enter author: ")

        price = input("Enter price (e.g. 499.99): ")
        price = validate_field_type(price, "price", float)

        pages = input("Enter page count: ")
        pages = validate_field_type(pages, "pages", int)

        isbn = input("Enter ISBN: ")
        isbn = validate_field_type(isbn, "isbn", str)
       
        format_type = input("Enter format (ebook / printed): ").lower()

        return {
            "title": title,
            "author": author,
            "price": price,
            "pages": pages,
            "isbn": isbn,
            "format": format_type,
        }
    except ValueError as ve:
        print(f"[ERROR] {ve}")
        return None


def main():
    store = BookStore()

    while True:
        print("\n--- BookStore CLI Menu ---\n")
        print("1. Add Book")
        print("2. Delete Book by ISBN")
        print("3. Delete Book by Title")
        print("4. View All Books")
        print("5. Filter by Title")
        print("6. Filter by Author")
        print("7. Filter by Price")
        print("8. Exit")
        choice = input("Enter your choice (1-8): ")
    
        try:
            if choice == "1":
                book_data = get_book_input()
                if book_data:
                    try:
                        store.add_book(book_data)
                    except (DuplicateBookError, ValueError) as e:
                        print(f"[ERROR] {e}")

            elif choice == "2":
                isbn = input("Enter ISBN to delete: ")
                store.delete_book_by_isbn(isbn)

            elif choice == "3":
                title = input("Enter title to delete: ")
                store.delete_book_by_title(title)

            elif choice == "4":
                print("\n--- All Books in Inventory ---\n")
                for book in store.get_all_books():
                    print(book)

            elif choice == "5":
                title = input("Enter title to filter: ")
                results = [book for book in store.get_all_books() if book.title == title]
                if results:
                    for book in results:
                        print(book)
                else:
                    print("\nNo books found with that title.\n")

            elif choice == "6":
                author = input("Enter author name: ")
                results = [book for book in store.get_all_books() if book.author == author]
                if results:
                    for book in results:
                        print(book)
                else:
                    print("\nNo books found by that author.\n")

            elif choice == "7":
                try:
                    max_price = input("Enter max price: ")
                    max_price = validate_field_type(max_price, "max_price", float)
                    results = [book for book in store.get_all_books() if book.price <= max_price]
                    if results:
                        for book in results:
                            print(book)
                    else:
                        print("\nNo books found under that price.\n")
                except ValueError as ve:
                    print(f"\n[ERROR] {ve}\n")

            elif choice == "8":
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please select a number from 1 to 8.")

        except (DuplicateBookError, BookNotFoundError) as e:
            print(f"\n[EXCEPTION] {e}\n")


if __name__ == "__main__":
    main()
