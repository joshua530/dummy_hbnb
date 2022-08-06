# AirBnB clone - The console
![ABNB Logo](./images/hbnb_logo.png)

## Description
This is the first version of the airbnb clone. It is comprised of a command line interpreter
and models.

### Command line interpreter
The interpreter is tasked with interpretation of commands that will allow one to create
model objects, interact with them and save them to a file when done.
The saved objects can be reloaded once the user logs in to the command line again later on.

### Models
The parent class is the `BaseModel`. All the other models will extend it.<br>
Other classes that will be implemented are `Review`, `User`, `Place`, `Amenity`, `PlaceAmenity`, `State` and `City`<br>
![ER Diagram](images/er-dig.jpg "entity relationship diagram")

## Commands
---
| Command   | Sample Usage                                  | Functionality                              |
| --------- | --------------------------------------------- | ------------------------------------------ |
| `help`    | `help`                                        | displays all commands available            |
| `create`  | `create <class>`                              | creates new object (ex. a new User, Place) |
| `update`  | `User.update('123', {'name' : 'Sam'})` | updates attribute of an object             |
| `destroy` | `User.destroy('123')`                         | destroys specified object                  |
| `show`    | `User.show('123')`                            | retrieve an object from a file, a database |
| `all`     | `User.all()`                                  | display all objects in class               |
| `count`   | `User.count()`                                | returns count of objects in specified class|
| `quit`    | `quit`                                        | exit the shell                             |

## Usage
Interactive Mode
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
Non-Interactive Mode
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## Environment
- Operating System: Ubuntu 20.04 LTS
- Language: Python 3.8.10
- Style guidelines: [pycodestyle 2.8.0](https://github.com/pycqa/pycodestyle), [google python style guidelines](https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings)
