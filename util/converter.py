from abc import ABC, abstractmethod
from users import Cashier, Customer
from products import Hamburger, Soda, Drink, HappyMeal
#Write your code here

class Converter(ABC):
  @abstractmethod
  def convert(self,dataFrame,*args) -> list:
      pass  
  def print(self, objects):
    for item in objects:
      print(item.describe())

class CashierConverter(Converter):
  def convert(self,dataFrame):    
    cashiers = []
    for row in dataFrame.itertuples (index=False, name=None):
      args = (row[1], row[0], row[2], row[3], row[4])
      cashier = Cashier(*args)
      cashiers.append(cashier)
    return cashiers

class CustomerConverter(Converter):
  def convert(self,dataFrame):    
    customers = []
    for row in dataFrame.itertuples (index=False, name=None):
      args = (row[1], row[0], row[2], row[3], row[4])
      customer = Customer(*args)
      customers.append(customer)
    return customers

class ProductConverter(Converter):
  def convert(self,dataFrame, ProductType):    
    products = []
    for row in dataFrame.itertuples (index=False, name=None):
      product = ProductType(*row)
      products.append(product)
    return products