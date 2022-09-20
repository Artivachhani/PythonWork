#This module calculate area of different shapes

import math
pi = 3.14
class Shapes():
    def __init__(self):
        pass
    def FindArea(self):
        way = True
        while way:
            print("\nPress The Key To Find Area: ")
            print("1. Lines")
            print("2. Cylender")
            print("3. Cube")
            print("4. Cuboid")
            print("5. Sphere")
            print("6. Cone")
            x = int(input("\nËnter Your Choice: "))
            print("\n")
            if x == 1:
                x1 = int(input("Enter x1: "))
                x2 = int(input("Enter y1: "))
                y1 = int(input("Enter x2: "))
                y2 = int(input("Enter y2: "))
                l = Lines([x1,x2],[y1,y2])
                print("\n")
                l.find_length()
                l.find_slope()
            elif x== 2:
                height = float(input("Enter Height : "))
                radius = float(input("Enter Radius : "))
                c = Cylender(height,radius)
                print("\n")
                c.volume()
                c.surface_area()
            elif x== 3:
                length = float(input("Enter length : "))
            
                c = Cube(length)
                print("\n")
                c.volume()
                c.surface_area()
            elif x== 4:
                height = float(input("Enter Height : "))
                length = float(input("Enter Length : "))
                width = float(input("Enter Width : "))
                c = Cuboid(height,length,width)
                print("\n")
                c.volume()
                c.surface_area()
            elif x== 5:
                radius = float(input("Enter Radius : "))
                c = Sphere(radius)
                print("\n")
                c.volume()
                c.surface_area()
            elif x== 6:
                length = float(input("Enter sidelength : "))
                height = float(input("Enter height : "))
                radius = float(input("Enter radius : "))
                c = Cone(length,radius,height)
                print("\n")
                c.volume()
                c.surface_area()
            else:
                way = False


class Lines():
    
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2
        print("line created")

    def find_length(self):
        y2 = self.p2[1]
        y1 = self.p1[1]
        x2 = self.p2[0]
        x1 = self.p1[0]

        len1 = ((x2-x1)**2) + ((y2-y1)**2)
        length = math.sqrt(len1)
        print(f'The Length Of Line : {length}')

    def find_slope(self):
        
        y2 = self.p2[1]
        y1 = self.p1[1]
        x2 = self.p2[0]
        x1 = self.p1[0]
        slope = (y2-y1)/(x2-x1)
        print(f'The Slope Of Line: {slope}')


class Cylender():
    
    def __init__(self,height,radius):
        self.height = height
        self.radius = radius

    def volume(self):
        vol = pi * (self.radius**2) * self.height
        print (f'Volume Of Given Cylender : {vol}')

    def surface_area(self):
        surarea = pi * (self.radius**2)
        print (f'Surface Area Of Given Cylender : {surarea}')

class Cube():
    def __init__(self,length):
        self.length = length

    def volume(self):
        vol = self.length**3
        print(f'Volume Of Given Cube : {vol}')

    def surface_area(self):
        sa = 6 * (self.length**2)
        print(f'Surface Area Of Given Cube : {sa}')

class Cuboid():
    def __init__(self,length,width,height):
        self.length = length
        self.width = width
        self.height = height

    def volume(self):
        vol = self.length * self.width * self.height
        print(f'Volume Of Given Cuboid : {vol}')

    def surface_area(self):
        sa = (2*self.width*self.length) + (2 * self.width * self.height) + (2 * self.length * self.height)
        print(f'Surface Area Of Given Cuboid : {sa}')

class Sphere():
    def __init__(self,radius):
        self.radius = radius
        
    def volume(self):
        vol = 4/3 * pi * (self.radius **3)
        print(f'Volume Of Given Sphere : {vol}')

    def surface_area(self):
        sa = 4 * pi * (self.radius ** 2)
        print(f'Surface Area Of Given Sphere : {sa}')


class Cone():
    def __init__(self,sidelength,radius,height):
        self.sidelength = sidelength
        self.radius = radius
        self.height = height

    def volume(self):
        vol = 1/3 * pi * (self.radius ** 2) * self.height
        print(f'Volume Of Given Cone : {vol}')

    def surface_area(self):
        basearea = pi + (self.radius ** 2)
        sidearea = pi * self.radius * self.sidelength
        sa = basearea + sidearea
        print(f'Surface Area Of Given Cone : {sa}')


    

s = Shapes()
s.FindArea()

    
