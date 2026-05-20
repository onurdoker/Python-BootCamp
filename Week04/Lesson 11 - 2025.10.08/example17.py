"""
Python OOP: Access Modifiers
Introduction: Why Is Access Control Needed? (Encapsulation)
Object-oriented programming (OOP) organizes programming by combining data (attributes/variables) and the function (methods) that operate on that
data into structures called class.

Access Modifiers determine whether certain data or methods within a class can be directly accessed or modified from outside the class - in other
words, whether they remain hidden or exposed.

This concept is known as Encapsulation.Its purpose is as follows:
- Security: Prevent critical data being accidentally or intentionally modified.
(Example: Preventing a bank account from being directly changed from outside the class)

- Organization: Hide the internal workings of a class from outside world, making the code easier to maintain and manage.
"""

"""
Unlike traditional OOP languages, Python does not acctually have "private" or "protected" keywords.

Instead, Python follows the philosophy of "Trust the Developer", and indicates access levels through naming conventions rather that strict
enforcement.

Here are the main conventions:
Access Level        Definition Style            Convention Name     Actual AccessBehavior
  Public            Normal name (name)          Public              Accessible from anywhere
  Protected         Single underscore (_name)   Protected           Technically accessible from anywhere, but signals "Please don't touch this from outside"
  Private           Double underscore (__name)  Private             Makes external access harder through name mangling
"""
