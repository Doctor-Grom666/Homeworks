immutable_var = 1, 'String', True, 2.8
print(immutable_var)

# immutable_var[0] = 4
# print(immutable_var)
# Кортеж является неизменяемым объектом, поэтому попытка изменить значения элементов приведёт к ошибке
# Закомментировал код выше, чтобы ошибка не выводилась в консоль

mutable_list = [1, 'String', True, 2.8]
mutable_list[0] = 4
print(mutable_list)

