class Smartphone:
 def __init__(self, phone_brand, phone_model, phone_number):
  self.phone_brand = phone_brand
  self.phone_model = phone_model
  self.phone_number = phone_number


my_smartphone = Smartphone("Apple", "iPhone 13 Pro", "+79123456789")


print(my_smartphone.phone_brand) 
print(my_smartphone.phone_model) 
print(my_smartphone.phone_number) 