class MyClass:
    """
    A simple class for demonstration.
    """
    class_attribute = "This is a class attribute"

    def __init__(self, name, value):
        """
        Initializes an instance of MyClass.
        """
        self.name = name
        self.value = value

    def my_method(self):
        """
        A simple method.
        """
        return f"Name: {self.name}, Value: {self.value}"


# Create an instance of MyClass
obj = MyClass("example", 100)

# 1. Get the type of the object
print("Type of object:", type(obj))

# 2. Get the list of attributes and methods of the object
print("\\nAttributes and methods:", dir(obj))

# 3. Get the memory address of the object
print("\\nMemory address:", id(obj))

# 4. Check if the object is an instance of a class
print("\\nIs obj an instance of MyClass?", isinstance(obj, MyClass))
print("Is obj an instance of str?", isinstance(obj, str))

# 5. Check if the object has a specific attribute
print("\\nHas attribute 'name'?", hasattr(obj, 'name'))
print("Has attribute 'age'?", hasattr(obj, 'age'))

# 6. Accessing docstrings
print("\\nDocstring for MyClass:", MyClass.__doc__)
print("Docstring for my_method:", obj.my_method.__doc__)

# 7. Accessing class attributes
print("\\nClass attribute:", obj.class_attribute)