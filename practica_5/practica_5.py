import json
import random
from PIL import Image, ImageDraw, ImageFont

with open("config.json") as f:
    conf = json.load(f)

print("x - ",conf["size"][0],"| y -", conf["size"][1], "поколений - ", conf["steps"])
x = conf["size"][0]
y = conf["size"][1]
steps = conf["steps"]
color = conf["color"]
cells = []

for i in range(0,y):
    lineCell = []
    for j in range(0,x):
        lineCell.append(random.choice([0, 1]))
    cells.append(lineCell)

print(cells)

def near(pos: list , system=[[-1 , -1] , [-1 , 0] , [-1 , 1] , [0 , -1] , [0 , 1] , [1 , -1] , [1 , 0] , [1 , 1]]):
    count = 0
    for i in system:
        if cells[(pos[0] + i[0]) % len(cells)][(pos[1] + i[1]) % len(cells[0])]:
            count += 1
    return count

for n in range(0,steps):
    print("Поколение : ",n)
    cells2 = cells
    for i in range(0,y):
        for j in range(0,x):
            if(cells[i][j]):
                if(near([i,j]) not in (2,3)):
                    cells2[i][j] = 0
                    continue
                cells2[i][j] = 1
                continue
            if(near([i,j]) == 3):
                cells2[i][j] = 1
                continue
            cells2[i][j] = 0
        cells = cells2

im = Image.new('RGB',(x*10,y*10+50),(255,255,255))
draw = ImageDraw.Draw(im)

for i in range(0,y):
    for j in range(0, x):
        if(cells[i][j] == 1):
            draw.rectangle((i*10,j*10,i*10+10,j*10+10),fill=color)
        elif(cells[i][j] > 1):
            draw.rectangle((i * 10, j * 10, i * 10 + 10, j * 10 + 10), fill=color)
font = ImageFont.truetype("arial.ttf", 32, encoding='UTF-8')
draw.text((0,y*10+15),f'Поколений: {steps} | Размеры: {x}x{y}',font=font,fill = (0,0,0))
im.show()
im.save(f'{steps}_{x}x{y}_life.png')



