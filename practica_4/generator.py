import random
import json

def generateMatrixFloat(x,y):
    matrix = []

    for i in range(0, x):
        line=[]
        for j in range(0, y):
            line.append(random.uniform(0.0,10.0))
        matrix.append(line)
    return matrix

def generateMatrixInt(x,y):
    matrix = []

    for i in range(0, x):
        line=[]
        for j in range(0, y):
            line.append(random.randint(0,10))
        matrix.append(line)
    return matrix



try:
    x = int(input("Введите 1ую границу => "))
    y = int(input("Введите 2ую границу => "))
    z = int(input("Введите 3ую границу => "))
    alpha = int(input("Введите Alpha => "))
    beta = int(input("Введите Beta => "))
    repeat = int(input("Кол-во проходов => "))
    chet= int(input("Нечетное -0 / Четное - 1 =>"))
except :
    print("Ошибка границ, повторите попытку")
    quit()

if(chet == 0):

    matrix1 = generateMatrixFloat(x,y)
    matrix2 = generateMatrixFloat(y,z)
else:
    matrix1 = generateMatrixInt(x, y)
    matrix2 = generateMatrixInt(y, z)

mxs={'m1':matrix1,'m2':matrix2,'alpha':alpha,'beta':beta,'repeat':repeat}

with open('generator.json','w') as f:
    json.dump(mxs,f)
