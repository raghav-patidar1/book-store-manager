
# 📚 BookStore Manager CLI

A clean, scalable, and modular Command-Line Interface (CLI) project built using Python.
It demonstrates real-world OOP principles such as inheritance,abstraction, encapsulation, access specifiers, custom exceptions, custom iterators, decorators and magic methods, with a strong focus on project architecture and maintainability.


## ✨ Features

- Add new books with proper validations.

- Remove books by Title or ISBN.

- View all books in the store.

- Filter books by author, title, and price.

- Custom Exception Handling.

- Input validation and error messages.

- Designed with a modular structure for easy scaling and maintenance.


## 🧠 Concepts Used

- Object-Oriented Programming (OOP)

- Abstract Base Classes (abc)

- Custom Decorators

- Custom Iterators (__iter__, __next__)

- Custom Exceptions

- Property Decorators (@property)

- Modular Code Organization

- CLI Input Validation


## 📂 Project Structure


```bash
  book-store-manager/
    │
    ├── bookstore/             # Package containing all core modules
    │   ├── __init__.py         # Package initializer
    │   ├── models.py           # Book model with validation
    │   ├── store.py            # BookStore manager class
    │   ├── utils.py            # Decorators and utility functions
    │   └── exceptions.py       # Custom exceptions
    │
    ├── main.py                 # CLI runner script
    ├── .gitignore              # Files/directories to ignore in Git
    └── README.md               # Project documentation

```


## 🚀 How to Use

### 1. Clone the Repository

```bash
git clone https://github.com/raghav-patidar1/book-store-manager.git

cd book-store-manager
```

### 2. Run the Application

```bash
python main.py
```
    

## 🚀 Future Scope

- Django-based web app version
- Persistent database backend (SQLite / PostgreSQL)
- RESTful API layer


## 🤝 Contributions

Pull requests are welcome! Feel free to fork the repository and submit your improvements.


## 📄 License

This project is licensed under the MIT License.

