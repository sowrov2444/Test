class veicle:
    """Base class for all vehicles"""
    def __init__(self,name,manufacturer,color):
        self.name=name
        self.manufacturer=manufacturer
        self.color=color
    def drive(self):
        print("Driving",self.manufacturer,self.name)
    def turn(self,direction):
        print("Turning",self.name,"to",direction)
    def brake(self):
        print(self.name,"is stopping!")

if __name__ == "__main__":
    v1=veicle("Fusion 110 EX","Walton","Black")
    v2=veicle("Softail Delux","Harley-Davidson","Blue")
    v3=veicle("Mustang 5.0 GT Coupe","Ford","Red")
    v1.drive()
    v2.drive()
    v3.drive()
    v1.turn("left")
    v2.turn("right")
    v1.brake()
    v2.brake()
    v3.brake()
    v2.turn("dead")


class car(veicle):
    "car class"
    def change_gear(self,gear_name):
        """marhod for changing gear"""
        print(self.name,"is changing geat to",gear_name)
if __name__ == "__main__":
    c=car("Mustang 5.0 GT Coupe","Ford","Red")
    c.drive()
    c.brake()
    c.change_gear("p")
c.change_gear("3")
print("*+3")
ob=object()
print(type(ob))

class vehicle:
    """base class for all vehicles"""
    def __init__(self,name,manufacturer,color):
        self.name=name
        self.manufacturer=manufacturer
        self.color=color
    def driving(self):
        print("Driving",self.manufacturer,self.name)
    def turn(self,direction):
        print("Turning",self.name,"to",direction)
    def brake(self):
        print(self.name,"is stopping!")
class car(vehicle):
    "car class"
    def __init__(self,name,manufacturer,color,year):
        self.name=name
        self.color=color
        self.manufacturer=manufacturer
        self.year=2024
        self.wheels=4
        print("A new car has been created.Name:",self.name)
        print("It has",self.wheels,"wheels")
        print("The car was built in",self.year)
    def change_gear(self,gear_name):
        """method of changing gear"""
        print(self.name,"is changing gear to",gear_name)
if __name__ == "__main__":
    c=car("Mustang 5.0 GT Coupe","Ford","Red",2024)


# method overriding
class vehicle:
    "base class for all vehicles"
    def __init__(self,name,manufacturer,color):
        self.name=name
        self.manufacturer=manufacturer
        self.color=color
    def turn(self,direction):
        print("Turning",self.name,"to",direction)
class car(veicle):
    def __init__(self,name,manufacturer,color,year):
        self.name=name
        self.manufacturer=manufacturer
        self.color=color
        self.year=2023
        self.wheels=4
    def change_gear(self,gear_name):
        """mathod of changing gear"""
        print(self.name,"is changing gear to",gear_name)
    def turn(self,direction):
        print(self.name,"is turning",direction)

if __name__ == "__main__":
    c=car("Mustang 5.0 GT Coupe","Ford","Red",2017)
    v=veicle("Softail Delux","Harley-Davidson","Blue")
    c.turn("right")
    v.turn("right")

class vehicle:
    "Base class for all vehicles"
    def __init__(self,name,manufacturer,color):
        print("Creating a vehicle")
        self.name=name
        self.manufacturer=manufacturer
        self.color=color
class car(veicle):
    "car class"
    def __init__(self,name,manufacturer,color,year):
        print("creating a car")
        super().__init__(name,manufacturer,color)
        self.year=2022
        self.wheels=4
if __name__ == "__main__":
    c=car("Mustang 5.0 GT Coupe","Ford","Red",2022)
    print(c.name,c.year,c.wheels)


#turtle
import turtle
class AjobTurtle(turtle.Turtle):
    """AjobTurtle is a class for new type of turtle"""
    def forward(self,pixel):
        super().backward(pixel)
    def backward(self,pixel):
        super().forward(pixel)
    def left(self, angle):
        super().right(angle)
    def right(self, angle):
        print("I won't turn right, because I am ajob!")
if __name__ == "__main__":
    montu=AjobTurtle()
    montu.shape("turtle")
    montu.left(30)
    montu.forward(200)
    montu.left(450)# modifai 45 - 450
    montu.backward(100)
    montu.right(90)
    montu.forward(10)

    jhontu=turtle.Turtle()
    jhontu.shape("turtle")
    jhontu.left(30)
    jhontu.forward(200)
    jhontu.left(450)# modifai 45 - 450
    jhontu.backward(100)

    turtle.done



