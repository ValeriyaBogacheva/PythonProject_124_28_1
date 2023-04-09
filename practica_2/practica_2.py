

#Работа со строками

string1 = "This is a string. "
string2 = " This is another string. "


print(string1+string2)

print("len - " , len(string2))
print("title - " + string1.title())
print("lower - " + string1.lower())
print("upper - " + string1.upper())
print("rstrip - " + string1.rstrip())
print("lstrip - " + string2.lstrip())
print("strip - " + string2.strip())
print("strip('. ') - " + string2.strip('. '))

d = "Some text"
print(d[5])
print(d[0:4])
print(d[0:4:2])
#d[0] = 'T'


#Работа с числами

int1 = 5
int2 = 8
print("/", 5 / 8)
print("%", 8 % 5)
print("**", 5 ** 8)
print("Int", int1)
param = "string" + str(15)

#Преобразование данных

n1 = input("Введите 1 число: ")
n2 = input("Введите 2 число: ")
n3 = float(n1) + float(n2)
print(n1 + " plus " + n2 + " = ","{:5.0f}".format(n3).lstrip())


a = 1/3
print("{:7.3f}".format(a))
a = 2/3
b = 2/9
print("{:7.3f} {:7.3f}".format(a, b))
print("{:10.3e} {:10.3e}".format(a, b))


#Списки
list1 = [82,8,23,97,92,44,17,39,11,12]
print(dir(list1))
list1[0] = 80
list1[7] = 41

list1.append(50)
list1.insert(4, 100)
list1.pop(0)
list1.pop(len(list1)-1)
print(list1)

list1.sort(reverse=True)
list2 = [3,5,6,2,33,6,11]
lis = sorted(list2)

print(lis)
print(list1)

#Кортежи

print(dir(tuple))
seq = (2,8,23,97,92,44,17,39,11,12)
print(seq.count(8))
print(seq.index(44))
listseq = list(seq)
print(type(listseq))
listseq.append(5)

#Словари
D = {'food': 'Apple', 'quantity': 4, 'color': 'Red'}
D['quantity'] += 10
print(D['food'] , D['quantity'])
dp={}

dp["name"] = input("Введите имя: ")
dp["age"] = input("Введите возраст: ")

print(dp)

#Вложенность хранения данных
rec = {'name': {'firstname': 'Bob', 'lastname': 'Smith'}, 'job': ['dev', 'mgr'], 'age': 25}
print(rec['name']['firstname']+ ' ' + rec['name']['lastname'])
print(rec['name']['firstname'])
print(*rec['job'])
rec['job'].append('junior')

print("Имя:", rec['name']['firstname'], rec['name']['lastname'] + '\n',
      "Должности: ", *rec['job'], '\n',
      "Лет: ", rec["age"])

