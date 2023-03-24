import sqlite3

def connect():
    conn = sqlite3.connect('bookstore.db')
    c = conn.cursor()
    return conn, c

def create_table():
    conn, c = connect()
    c.execute("CREATE TABLE IF NOT EXISTS books (ID INT PRIMARY KEY, Title TEXT, Author TEXT, Quantity INT)")
    conn.commit()
    conn.close()

def add_book():
    conn, c = connect()
    id = input("Enter ID: ")
    title = input("Enter title: ")
    author = input("Enter author: ")
    quantity = input("Enter quantity: ")
    c.execute("INSERT INTO books VALUES (?, ?, ?, ?)", (id, title, author, quantity))
    conn.commit()
    conn.close()
    print("Book added successfully!")

def update_book():
    conn, c = connect()
    id = input("Enter ID of the book to update: ")
    title = input("Enter new title (leave blank if no change): ")
    author = input("Enter new author (leave blank if no change): ")
    quantity = input("Enter new quantity (leave blank if no change): ")

    if title:
        c.execute("UPDATE books SET Title = ? WHERE ID = ?", (title, id))
    if author:
        c.execute("UPDATE books SET Author = ? WHERE ID = ?", (author, id))
    if quantity:
        c.execute("UPDATE books SET Quantity = ? WHERE ID = ?", (quantity, id))

    conn.commit()
    conn.close()
    print("Book updated successfully!")

def delete_book():
    conn, c = connect()
    id = input("Enter ID of the book to delete: ")
    c.execute("DELETE FROM books WHERE ID = ?", (id,))
    conn.commit()
    conn.close()
    print("Book deleted successfully!")

def search_books():
    conn, c = connect()
    keyword = input("Enter title or author to search for: ")
    c.execute("SELECT * FROM books WHERE Title LIKE ? OR Author LIKE ?", ('%'+keyword+'%', '%'+keyword+'%'))
    books = c.fetchall()
    if len(books) == 0:
        print("No matching books found.")
    else:
        for book in books:
            print(book)
    conn.close()