# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


list = [2, 3, 4, 5, 6]
num = len(list)
list2=[]
for i in range(num):
    while i < len(list)/2 and num > len(list)/2:
        num = num - 1
        a = list[i] * list[num]
        list2.append(a)
        i += 1

print(list)
print(list2)





    
      


