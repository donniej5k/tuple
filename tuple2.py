# Existing library data
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def add_book(library, book):
    # Check if the book already exists in the library
    if book in library:
        print(f"The book '{book[0]}' by {book[1]} is already in the library.")
    else:
        library.append(book)
        print(f"The book '{book[0]}' by {book[1]} has been added to the library.")

# Example usage:
new_book1 = ("1984", "George Orwell")
new_book2 = ("Fahrenheit 451", "Ray Bradbury")

add_book(library, new_book1)  # Should indicate the book is already in the library
add_book(library, new_book2)  # Should add the book to the library

# Print the updated library to see the results
print(library)
