#  Library Management System

A simple **command-line Library Management System** built with **Python** and **SQLAlchemy ORM**.  
The system allows you to manage **Authors, Books, Members, and Loans** with a CLI interface.

---

## Features
- Manage Authors (add, list, delete)  
- Manage Books (add, list, delete, link to authors)  
- Manage Members (add, list, delete)  
- Borrow Book (create a loan record)  
- Return Book (mark loan as returned)  
- View Overdue Loans (see books not returned on time)  

---

##  Tech Stack
- **Python 3**  
- **SQLAlchemy ORM**  
- **SQLite** (default database, can be swapped with PostgreSQL/MySQL)  
- **Faker** (for seeding fake data)  

---

##  Project Structure
```
library_management_system/
│── lib/db/
│   ├── models.py        # SQLAlchemy models
│   ├── cli.py           # Command line interface
│   ├── database.py      # Database connection & session
│── seed.py              # Populate database with fake data
│── main.py              # Entry point
│── README.md            # Project documentation
```

---

##  Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/amos-kipkorir/library-management-system.git
   cd library_management_system
   ```

2. **Initialize the database**
   ```bash
   python main.py
   ```

3. **(Optional) Seed the database with fake data**
   ```bash
   python seed.py
   ```

---

## Usage
Run the system:
```bash
python main.py
```

Menu options:
```
Library Management System ===
1. Manage Authors
2. Manage Books
3. Manage Members
4. Borrow Book
5. Return Book
6. View Overdue Loans
7. Exit
```

---

##  Example
- Add authors and books  
- Register members  
- Borrow/return books  
- View overdue loans  

---

## Contributing
1. Fork the repo  
2. Create a new branch (`feature/new-feature`)  
3. Commit changes  
4. Push and create a pull request  

---
## Author

Amos Kipkorir

---

##  License
This project is licensed under the **MIT License**.