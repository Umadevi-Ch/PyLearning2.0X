#Inheritance
# Single
# Multiple
# MultiLevel
# Hybrid
# Heri
# API ,Web Automation -80%---> Single

# Multi level Inheritance
class GrandParent:

    def grandparent_method(self):
        return "Grandparent's method"

class Parent(GrandParent):
    def parent_method(self):
        return "Parent's method"

class Child(Parent):
    def child_method(self):
        return "Child's method"

child = Child()
print(child.grandparent_method())
print(child.parent_method())
print(child.child_method())