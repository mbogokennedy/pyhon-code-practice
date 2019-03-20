class person():
	def __init__(self, name, job=None, pay=0):
		self.name = name
		self.job =job
		self.pay = pay
	def firstname(self):
		return self.name.split()[0]
	def lastname(self):
		return self.name.split()[-1]
	def giveRaise(self):
		self.pay = (self.pay * (1 + percent))
		return self.pay
	
class Manager(person):
	def __init__(self, name, pay):
		person.__init__(self, name, "mrg", pay)
	def giveRaise(self, percent, bonus=.10):
		person.giveRaise(percent+bonus)

if __name__ == '__main__':
	chris = Manager('Chris Jones', 50000)
	chris.giveRaise(.20)
	print(chris)
	
	
# class Person:
    # """
    # Class represents a person
    # """

    # def __init__(self, name, job=None, pay=0):
        # """
        # Constructor method
        # """
        # self.name = name
        # self.job = job
        # self.pay = pay

    # def __del__(self):
        # """
        # Deconstructor: it will be called when gc recycle this object, or *del* called.
        # """
	
		
    # def last_name(self):
        # """
        # The first argument of instance methods is *self*.
        # It's the reference to current instance, just like *this* in C++ and Java.
        # """
        # return self.name.split()[-1]

    # def give_raise(self, percent):
        # self.pay = int(self.pay * (1 + percent))
	
	
# class Manager(Person):

  # def __init__(self, name, pay):
    # super().__init__(name, 'manager', pay)

  # def give_raise(percent, bouns=.10):
    # Person.give_raise(self, percent + bouns)
# if __name__ == '__main__':
    # sue = Person('Sue Jones', 8000)
    # sue.give_raise(.20)
    # print(sue)     # ('Jones', 8800)