# Task 4
# Inheritance and Classes

// Base class or the parent class
class Rectangle:
  Area = 0.00;
  def __init__(self, len, wid):
   self.len = len;
   self.wid = wid;

  def find_Area(self):
    self.Area = self.len * self.wid;

  def print_Area(self):
    print('The area is: ', self.Area);

// Derived class or the child class
class Trapezium(Rectangle):
  def __init__(self, len, wid, h):
    super().__init__(len, wid);   # constructor of Rectangle class
    self.h = h;                   # height of the trapezium

  def find_Area(self):
    self.Area = 0.5 * (self.len + self.wid) * self.h;   # function to find area

  def print_Area(self):
    print("The area of trapezium is:", self.Area);      # function to print area

# Rectangle class
r1 = Rectangle(10, 8);
r1.find_Area();
r1.print_Area();

# Trapezium class
t1 = Trapezium(10, 8, 5);
t1.find_Area();
t1.print_Area();
