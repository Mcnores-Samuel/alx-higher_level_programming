# project: 0x0A-python-inheritance
## 0-lookup.py

```
This module has one function lookup(obj).

lookup(obj) return a list of available list and attributes of an object.

```
### lookup(obj)
```
Returns the list of available attributes and methods of an object

    args:
        obj(object): an object to list all its attributesa and methods.
    Returns: the list of available attributes and methods of an object
    
```
## 100-my_int.py

```
This module defines MyInt class
```
### MyInt(int)
```
Defines MyInt class which inverts the == and != operators
```
### __ne__(self, value)
```
Return the opposite if obj != value return True in place False
```
### __eq__(self, value)
```
Return the opposite if obj == value return False in place True
```
## 10-square.py

```
Defines a Rectangle subclass Square.
```
### Square(Rectangle)
```
Represent a square.
```
### __init__(self, size)
```
Initialize a new square.

        Args:
            size (int): The size of the new square.
        
```
## 11-square.py

```
Defines a Rectangle subclass Square.
```
### Square(Rectangle)
```
Represent a square.
```
### __init__(self, size)
```
Initialize a new square.

        Args:
            size (int): The size of the new square.
        
```
## 1-my_list.py

```
This module defines a class MyList with one method
print_sorted(self).

Inherits from the list class and prints a sorted list
for example:
>>> my_list = MyList()
>>> my_list.append(1)
>>> my_list.append(4)
>>> my_list.append(2)
>>> my_list.append(3)
>>> my_list.append(5)
>>> print(my_list)
[1, 4, 2, 3, 5]
>>> my_list.print_sorted()
[1, 4, 2, 3, 5]
>>> print(my_list)
[1, 4, 2, 3, 5]

```
### MyList(list)
```
define MyList class and Inherits from list class
```
### print_sorted(self)
```
Prints a sorted list object
```
## 2-is_same_class.py

```
This module defines a function is_same_class(obj, a_class)

is_same_class(obj, a_class) Take an obj check if is an instance of a class.
    pass

```
### is_same_class(obj, a_class)
```
Checks if obj is an instance of a class or not

    args:
        obj: an object to test if it is an instance of  a_class.
        a_class: a class a test against obj.
    Returns: True if obj is an instance of a_class or False otherwise.
    
```
## 3-is_kind_of_class.py

```
This module defines a function is_kind_of_class(obj, a_class)

is_kind_of_class(obj, a_class) Take an obj check if is an instance of a class.
    pass

```
### is_kind_of_class(obj, a_class)
```
Checks if obj is an instance of a class or
    if the object is an instance of a class that inherited from,

    args:
        obj: an object to test if it is an instance of  a_class.
        a_class: a class a test against obj.
    Returns: True if obj is an instance of a_class or False otherwise.
    
```
## 4-inherits_from.py

```
This module defines a function inherits_from(obj, a_class)

inherits_from(obj, a_class) Take an obj check if is an instance of a class.
    pass

```
### inherits_from(obj, a_class)
```
Checks if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class

    args:
        obj: an object to test if it inherits from  a_class.
        a_class: a class a test against obj.
    Returns: True if obj inherits from a_class or False otherwise.
    
```
## 5-base_geometry.py

```
This module defines a BaseGeometry class
```
### BaseGeometry
```
Defines a BaseGeometry class
```
## 6-base_geometry.py

```
This module defines a BaseGeometry class
```
### BaseGeometry
```
Defines a BaseGeometry class
```
### area(self)
```
aises an Exception with the message area() is not implemented
```
## 7-base_geometry.py

```
This module defines a BaseGeometry class
```
### BaseGeometry
```
Defines a BaseGeometry class
```
### area(self)
```
aises an Exception with the message area() is not implemented
```
### integer_validator(self, name, value)
```
Validates value to be an integer and greater than 0
```
## 8-rectangle.py

```
This module defines a BaseGeometry class
and subclass Rectangle

```
### Rectangle(BaseGeometry)
```
defines a Rectangle class that inherits from a BaseGeometry
```
### __init__(self, width, height)
```
Initializes Rectangle object

        args:
            width: a positive integers
            height: a positive integers
        
```
## 9-rectangle.py

```
This module defines a BaseGeometry class
and subclass Rectangle

```
### Rectangle(BaseGeometry)
```
defines a Rectangle class that inherits from a BaseGeometry
```
### __init__(self, width, height)
```
Initializes Rectangle object

        args:
            width: a positive integers
            height: a positive integers
        
```
### area(self)
```
Returns the area of the Rectangle object
```
### __str__(self)
```
String represantation of the Rectangle class
```
