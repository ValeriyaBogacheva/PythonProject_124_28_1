import json
from datetime import datetime
import time
from csv import DictWriter

with open("generator.json") as f:
    conf = json.load(f)

m1 = conf["m1"]
m2 = conf["m2"]
alpha = conf['alpha']
beta = conf['beta']
repeat = conf['repeat']

m = len(m1)
n = len(m2)
k = len(m2[0])

start_time = datetime.now()
for c in range(repeat):
    print(f'Проход - {c}')
    for u in range(len(m1)):
        for o in range(len(m2[0])):
            for p in range(len(m2)):
                m1[u][p] * m2[p][o]
elapsed_time = datetime.now() - start_time

print("Готово" , elapsed_time)
stats = {'Python затрачено времени':round(elapsed_time.total_seconds()*1000)}
header=['Python затрачено времени']
with open('statsPython.csv', 'a', newline='') as f:
    writer = DictWriter(f,fieldnames=header)
    writer.writerow(stats)
    f.close()
