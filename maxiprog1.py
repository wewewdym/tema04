return max_value

input_list = [3, 8, 1, 6, 2, 7, 4, 5] # пример входного списка
n=int(input())
input_list =[]

for i in range (n):
num=int(input())
input_list.append(num)

print("Максимальное значение в списке:", find_maximum_value(input_list))
