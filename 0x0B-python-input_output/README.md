# Project: 0x0B-python-input_output
## 0-read_file.py

```
This module defines one function read_file(fileneme="")

read_file(fileneme="") reads data from a file in utf-8 and print
it to the console. The data is usually text in utf-8.

```
### read_file(filename="")
```
Read from a text file object and print out the text

    args:
        filename: The name of the file to read from.
    Returns: None.
    
```
## 10-student.py

```
This module defines a Student class
```
### Student
```
defines a student class
```
### __init__(self, first_name, last_name, age)
```
Initializes Student object
```
### to_json(self, attrs=[])
```
retrieves a dictionary representation of a Student instance
        args:
           attrs: is a list of strings, only attribute names contained
           in this list must be retrieved.
        
```
## 11-student.py

```
This module defines a Student class
```
### Student
```
defines a student class
```
### __init__(self, first_name, last_name, age)
```
Initializes Student object
```
### to_json(self, attrs=[])
```
retrieves a dictionary representation of a Student instance
        args:
           attrs: is a list of strings, only attribute names contained
           in this list must be retrieved.
        
```
### reload_from_json(self, json)
```
Replaces all attributes of the Student instance

        args:
            json: a dictionary
        
```
## 12-pascal_triangle.py

## 1-write_file.py

```
This module defines a function write_file(filename="", text="")

write_file(filename="", text="") write text to the file by overwriting the
current text in the file with the new text.

```
### write_file(filename="", text="")
```
Write text to a text file or overwrites a file.

    args:
        filename: a file to write to.
        text: the new text to write to the file.
    Returns: number of characters written.
    
```
## 2-append_write.py

```
This module defines a function append_write(filename="", text="")

append_write(filename="", text="") append or adds text at the end of the file.

```
### append_write(filename="", text="")
```
Append a text at the end of the file.

    args:
        filename: a file to write to.
        text: the new text to write to the file.
    Returns: number of characters written.
    
```
## 3-to_json_string.py

```
This module defines a function to_json_string(my_obj)

to_json_string(my_obj) returns the JSON representation of an object (string)

```
### to_json_string(my_obj)
```
Returns the JSON representation of an object (string)

    args:
        my_obj: an object to create its json representation.
    Returns: the JSON representation of an object (string)
    
```
## 4-from_json_string.py

```
This module defines a function from_json_string(my_str)

 from_json_string(my_str) returns the JSON representation of an object (string)

```
### from_json_string(my_str)
```
Returns an object (Python data structure) represented by a JSON string

    args:
        my_str: a string to create its json representation.
    Returns: an object (Python data structure) represented by a JSON string
    
```
```

    {"is_active": true, "info": {"age": 36, "average": 3.14},
    "id": 12, "name": "John", "places": ["San Francisco", "Tokyo"]}
    
```
```

        {"is_active": true, 12}
        
```
## 5-save_to_json_file.py

```
This module defines a function save_to_json_file(my_obj, filename)

save_to_json_file(my_obj, filename) writes an Object to a text file,
using a JSON representation

```
### save_to_json_file(my_obj, filename)
```
 Writes an Object to a text file,
    using a JSON representation

    args:
        my_obj: an object to it's json representation to a text file.
        filename: a file to write a json representation of my_obj object.
    
```
## 6-load_from_json_file.py

```
This module defines a function load_from_json_file(filename)

load_from_json_file(filename) creates an Object from a JSON file

```
### load_from_json_file(filename)
```
Creates an Object from a JSON file

    args:
        filename: JSON file to create an object from.
    Returns: the object created or Deserialized
    
```
## 7-add_item.py

```
This module contains a script for write data from commandline
to a JSON file and also reads back from the file.

```
## 8-class_to_json.py

```
This module defines a class_to_json(obj) function
```
### class_to_json(obj)
```
returns the dictionary description with simple data structure
```
## 9-student.py

```
This module defines a Student class
```
### Student
```
defines a student class
```
### __init__(self, first_name, last_name, age)
```
Initializes Student object
```
### to_json(self)
```
retrieves a dictionary representation of a Student instance
```
