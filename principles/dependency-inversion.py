# https://www.youtube.com/watch?v=Kv5jhbSkqLE
# a key ingredient of dependency inversion and many of the other design patterns is abstraction
# you need a mechanism in your programming language that allows you to separate the description or definition of the interface
# from the actual implementation of something
from abc import ABC, abstractmethod

# ABC- abstract base class to model abstraction

# In an abstract class, you can specify what the interface should be that a class should adhere to
# so let's create an abstract class that defines the interface for things (LightBulb and Fan) that can be turn on and turn off
class Switchable(ABC):
    @abstractmethod  # this is an annotation
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class LightBulb(
    Switchable
):  # LightBulb inherits from Switchable. LightBulb is a subclass of Switchable. LightBulb implements the interface that defines in Switchable.
    def turn_on(self):
        print("LightBulb: turned on...")

    def turn_off(self):
        print("LightBulb: turned off...")


class Fan(Switchable):
    def turn_on(self):
        print("Fan: turned on...")

    def turn_off(self):
        print("Fan: turned off...")


class ElectricPowerSwitch:
    def __init__(self, c: Switchable):
        self.client = c
        self.on = False

    def press(self):
        if self.on:
            self.client.turn_off()
            self.on = False
        else:
            self.client.turn_on()
            self.on = True


# s = Switchable() - this won't work, Switchable abstracts are not allowed to create an instance of the class
# but you are allowed is to create a subclass of Switchable
# Switchable purely serves as a definition of the kind of methods that a class that inherits from Switchable should have
# l = LightBulb()
# f = Fan()
# switch = ElectricPowerSwitch(l)
switch = ElectricPowerSwitch(LightBulb())
switch.press()
switch.press()

# moral lession  - instead of the two classes - LightBulb and  ElectricPowerSwitch are directly coupled,
# instead of the two classes - Fan and  ElectricPowerSwitch are directly coupled,
# we have decoupled them through an interface, in this case called Switchable
# since ElectricPowerSwitch is no longer dependent on "LightBulb" and we use an abstract class, then we can add more objects that turn on and turn off like "Fan"
