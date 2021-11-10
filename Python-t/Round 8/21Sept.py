


# what does a property do?
### A decorator gives a function/method a bit of 
### extra functionality


##### Keep track of the monthly salary outgoings??

class Employee:
  pay_raise_amount = 1.1 # Class Attributes
  employees_number = 0
  monthly_salary = 0 
  def __init__(self, name, job, pay):
    self.name = name # John, 
    self.job = job # Admin,
    self.pay = pay # 65000,
    Employee.employees_number += 1 # Then do this!
    Employee.monthly_salary += self.pay

  def increase_pay(self):
    '''Instance Method'''
    self.pay *= Employee.pay_raise_amount

  @classmethod
  def new_raise_amount(classname, new_value):
    '''Class Method'''
    classname.pay_raise_amount = new_value

  @classmethod
  def raise_amount(cls): 
    cls.pay_raise_amount += 0.2 


  @classmethod 
  def employee_num(cls):
    return(cls.employees_number)

  @classmethod 
  def reset(cls):
    cls.employees_number = 0 
  
  @classmethod 
  def monthly_pay(cls): 
    return '£{}'.format(round(cls.monthly_salary/12, 2))
  

### Change any part of these!!
### Instance method!!
john = Employee('John', 'Admin', 65000)
alice = Employee('Alice', 'Manager', 75000)
chris = Employee('Chris', 'Developer', 105000)
bob = Employee('Bob', 'Team Member', 45000)


### Only effect the class
# @classmethod

#print(Employee.monthly_pay())


##### A class to represent a Person
## 2 attributes: firstname, lastname

# making an instance 

class Person:
  email_suffix = '@company.com'
  def __init__(self, firstname, lastname): 
    self.firstname = firstname 
    self.lastname = lastname 
    self.fullname = self.firstname + ' ' + self.lastname
  

  @property
  def full_name(self):
    return self.firstname + ' ' + self.lastname

  def hi (self): 
    return('Hi my name is {}'.format(self.fullname))

  @property
  def email(self): 
    return(self.firstname + '.' + self.lastname + Person.email_suffix)

Jay = Person('Jay','Lueng')
print(Jay.email)
#print(Jay.full_name)
#print(Jay.lastname)


Jay.lastname = 'Leunggg'
Jay.firstname = 'J'
print(Jay.email)

#print(Jay.full_name)


#### @property 
### Creating a dynamically updating attribute
### which looks like a method
