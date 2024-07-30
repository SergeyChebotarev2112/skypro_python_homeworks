from smartphone import Smartphone

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
