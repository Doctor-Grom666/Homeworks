my_dict = {'Ivan': 1992, 'Sasha': 1995, 'James': 1889}
print(my_dict)
print(my_dict.get('Ivan'), my_dict.get('Roman'))
my_dict.update({'Hanna': 1990, 'Robert': 2000})
delete = my_dict.pop('James')
print(delete)
print(my_dict)

my_set = {1, 2.3, 'List', 1, True, True, 'List', 1}
print(my_set)
my_set.add(10)
my_set.add(False)
my_set.remove('List')
print(my_set)