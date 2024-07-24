class Smartphone:
 def __init__(self, phone_brand, phone_model, phone_number):
  self.phone_brand = phone_brand
  self.phone_model = phone_model
  self.phone_number = phone_number

# Пример создания объекта класса Smartphone
my_smartphone = Smartphone("Apple", "iPhone 13 Pro", "+79123456789")

# Создание списка из пяти объектов Smartphone
catalog = [
 Smartphone("Samsung", "Galaxy S23", "+79123456781"),
 Smartphone("Honor", "Magic6 Pro", "+79123456782"),
 Smartphone("Xiaomi", "Mi 13", "+79123456783"),
 Smartphone("POCO", "M6 Pro", "+79123456784"),
 Smartphone("Nokia", "G21", "+79123456785")
]

# Цикл для вывода информации о каждом объекте в списке
for item in catalog:
 print(f"{item.phone_brand} - {item.phone_model}. {item.phone_number}")