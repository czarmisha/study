"""
In Python, object-oriented Programming (OOPs) is a programming paradigm that uses objects and classes in programming.
It aims to implement real-world entities like inheritance, polymorphisms, encapsulation, etc. in the programming.
The main concept of OOPs is to bind the data and the functions that work on that together
as a single unit so that no other part of the code can access this data.

OOPs Concepts in Python:
- Class
- Objects
- Polymorphism
- Encapsulation
- Inheritance
- Data Abstraction

https://www.geeksforgeeks.org/python-oops-concepts/?ref=lbp
"""

# Class
"""
A class is a collection of objects. A class contains the blueprints or the prototype from which the objects are being created.
It is a logical entity that contains some attributes and methods. 

To understand the need for creating a class let’s consider an example, let’s say you wanted to track the number of
dogs that may have different attributes like breed, and age. If a list is used, the first element could be the dog’s breed
while the second element could represent its age. Let’s suppose there are 100 different dogs, then how would you know which element
is supposed to be which? What if you wanted to add other properties to these dogs? This lacks organization and it’s
the exact need for classes. 
"""

# Objects
"""
The object is an entity that has a state and behavior associated with it. It may be any real-world object like a mouse,
keyboard, chair, table, pen, etc. Integers, strings, floating-point numbers, even arrays, and dictionaries, are all objects.
More specifically, any single integer or any single string is an object.
The number 12 is an object, the string “Hello, world” is an object, a list is an object that can hold other objects, and so on.
You’ve been using objects all along and may not even realize it.

An object consists of:

State: It is represented by the attributes of an object. It also reflects the properties of an object.
Behavior: It is represented by the methods of an object. It also reflects the response of an object to other objects.
Identity: It gives a unique name to an object and enables one object to interact with other objects.
To understand the state, behavior, and identity let us take the example of the class dog (explained above). 

The identity can be considered as the name of the dog.
State or Attributes can be considered as the breed, age, or color of the dog.
The behavior can be considered as to whether the dog is eating or sleeping.
"""
"""
The Python self  
Class methods must have an extra first parameter in the method definition. We do not give a value for this parameter when we call the method, Python provides it
If we have a method that takes no arguments, then we still have to have one argument.
This is similar to this pointer in C++ and this reference in Java.
When we call a method of this object as myobject.method(arg1, arg2), this is automatically converted by Python into MyClass.method(myobject, arg1, arg2) – this is all the special self is about.
"""

# Inheritance
"""
Python Inheritance
Inheritance is the capability of one class to derive or inherit the properties from another class.
The class that derives properties is called the derived class or child class and the class from which the properties are being derived is called the base class or parent class.
The benefits of inheritance are:

It represents real-world relationships well.
It provides the reusability of a code. We don’t have to write the same code again and again. Also, it allows us to add more features to a class without modifying it.
It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of B would automatically inherit from class A.
Types of Inheritance
Single Inheritance: Single-level inheritance enables a derived class to inherit characteristics from a single-parent class.
Multilevel Inheritance: Multi-level inheritance enables a derived class to inherit properties from an immediate parent class which in turn inherits properties from his parent class. 
Hierarchical Inheritance: Hierarchical-level inheritance enables more than one derived class to inherit properties from a parent class.
Multiple Inheritance: Multiple-level inheritance enables one derived class to inherit properties from more than one base class.
"""

# Polymorphism
"""
Polymorphism simply means having many forms. For example, we need to determine if the given species of birds fly or not, using polymorphism we can do this using a single function.

Polymorphism in Python
This code demonstrates the concept of inheritance and method overriding in Python classes.
It shows how subclasses can override methods defined in their parent class to provide specific behavior while still inheriting other methods from the parent class.
"""

# Encapsulation
"""
Encapsulation is one of the fundamental concepts in object-oriented programming (OOP).
It describes the idea of wrapping data and the methods that work on data within one unit.
This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data.
To prevent accidental change, an object’s variable can only be changed by an object’s method. Those types of variables are known as private variables.

A class is an example of encapsulation as it encapsulates all the data that is member functions, variables, etc.
"""

# Abstraction
"""
It hides unnecessary code details from the user. Also,  when we do not want to give out sensitive parts of our code implementation and this is where data abstraction came.

Data Abstraction in Python can be achieved by creating abstract classes.
"""
