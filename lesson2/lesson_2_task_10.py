def bank(X, Y):
 result = X
 for i in range(Y):
   result = result * 1.1
 return result
# Пример работы
result = bank(150, 5) 
print(result)