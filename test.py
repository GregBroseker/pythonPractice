import datetime

class Person: #parent class
  def __init__(self, fname, lname):
    self.first_name = fname
    self.last_name = lname

#This method is redundant and is done from inherited child method below (identify)
  #def printName(self):  
    #print(self.first_name, self.last_name)

class Age(Person): #child class
  def __init__(self, fname, lname, age):
    super().__init__(fname, lname)
    self.yearsAlive = age

  def identify(self):
    print("Hello, my name is ", self.first_name, self.last_name, "and I am", self.yearsAlive, "years old.")

x = Age("Greg", "Broseker", 28) 
x.identify()
user_date = datetime.datetime(2023, 2, 23, 23, 5, 30, 0)
print("The user date and time is: ", user_date)