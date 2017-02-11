# coding: UTF-8

class Person(object):
  def __init__(self, name):
    self.name = name
  def greet(self):
    print "my name is %s" % self.name

class SuperPerson(Person):
  def shout(self):
    print "%s is SUPER!" % self.name

bob = Person("Bob")
tom = SuperPerson("Tom")

print bob.name

bob.greet()
tom.shout()
