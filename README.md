# AirBnB Clone - The Console

## Description of the Project

The **AirBnB Clone** project is the foundation of a comprehensive web application inspired by the popular AirBnB platform. This initial phase focuses on creating a command-line interface (CLI) for managing various objects, setting up the groundwork for future development including database storage, APIs, and front-end integration.

Key objectives of this project include:
- Building a base class to handle initialization, serialization, and deserialization of objects.
- Implementing a file storage system for persistent data storage.
- Creating models such as `User`, `State`, `City`, `Place`, etc., that inherit from the base class.
- Developing a command interpreter to perform CRUD operations on objects.
- Writing comprehensive unit tests for all modules and functionalities.

---

## Description of the Command Interpreter

The command interpreter is a console application that enables users to manage AirBnB objects interactively. It provides commands for creating, reading, updating, and deleting objects, as well as retrieving specific statistics.

### How to Start the Command Interpreter

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/AirBnB_clone.git
   cd AirBnB_clone
   ```

2. Make the console executable:
   ```bash
   chmod +x console.py
   ```

3. Run the console:
   ```bash
   ./console.py
   ```

The prompt `(hbnb)` will appear, indicating that the interpreter is ready to accept commands.

---

### How to Use the Command Interpreter

The interpreter supports the following commands:

#### **Basic Commands**
| Command                          | Description                               |
|----------------------------------|-------------------------------------------|
| `quit`                           | Exits the console                         |
| `EOF`                            | Exits the console                         |
| *empty line*                     | Does nothing                              |

#### **Object Management Commands**
| Command                          | Description                               |
|----------------------------------|-------------------------------------------|
| `create <class_name>`            | Creates a new instance of a class         |
| `show <class_name> <id>`         | Displays the string representation of an object |
| `destroy <class_name> <id>`      | Deletes an object by its ID               |
| `all [<class_name>]`             | Displays all objects, optionally filtered by class |
| `update <class_name> <id> <attribute> <value>` | Updates an object's attribute |

---

### Examples

#### Create an object
```bash
(hbnb) create User
<instance_id>
```

#### Show an object
```bash
(hbnb) show User 1234-5678-9012
[User] (1234-5678-9012) {'id': '1234-5678-9012', 'created_at': '...', 'updated_at': '...'}
```

#### Update an object
```bash
(hbnb) update User 1234-5678-9012 name "John Doe"
(hbnb) show User 1234-5678-9012
[User] (1234-5678-9012) {'id': '1234-5678-9012', 'created_at': '...', 'updated_at': '...', 'name': 'John Doe'}
```

#### List all objects
```bash
(hbnb) all
[User] (1234-5678-9012) {'id': '1234-5678-9012', 'created_at': '...', 'updated_at': '...', 'name': 'John Doe'}
[Place] (abcd-efgh-ijkl) {'id': 'abcd-efgh-ijkl', 'created_at': '...', 'updated_at': '...'}
```

---

## Authors

All contributors to this project are listed in the `AUTHORS` file at the root of the repository.

---

## Repository Information

- **GitHub Repository**: [AirBnB_clone](https://github.com/your-username/AirBnB_clone)
- **Files**:
  - `README.md`: Project documentation.
  - `AUTHORS`: List of contributors.

## Contributing

This project follows a branch and pull request workflow. Contributors should:
1. Create a new branch for their feature or fix.
   ```bash
   git checkout -b <branch_name>
   ```
2. Commit changes and push the branch to the repository.
   ```bash
   git push origin <branch_name>
   ```
3. Open a pull request for review and approval.


