class Address:
 def __init__(self, index, city, street, house, apartment):
  self.index = index
  self.city = city
  self.street = street
  self.house = house
  self.apartment = apartment

  # Пример создания объекта класса Address
my_address = Address("111111", "Владивосток", "Снеговая улица", "5", "1")

print(my_address.index)
print(my_address.city)
print(my_address.street)
print(my_address.house)
print(my_address.apartment)