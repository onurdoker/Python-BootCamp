"""
Scope refers to the location where a variable, function, or object is defined and its accessibility from other parts of the code.
In Python, every name (variables, functions, classes, etc.) resides within a scope.
The scope defines the region where a name is valid.

Python follows LSB (Local-Scope Behavior) rules when resolving name lookup.

L - Local ->  Function or methods are defined the existing functions/classes.
E - Enclosing -> if functions are nested within other functions, the inner function's scope is limited to its parent function.
G - Global -> Things defined at the module (file) level are accessible throughout the script.
B - Built-in -> Python has built-in names like len, print, int etc.

Python looks for a name in the following order when resolving it:
Local -> Enclosing -> Global -> Built-in
"""

"""
! Local Scope

x parameter define in function. It is not accessible outside the function
"""


def function():
    x = 500
    print(x)


function()
# print(x) # NameError: name 'x' is not defined
