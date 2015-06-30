import json
import time
import os

f = open('compile_commands.json')
compile_dict=json.load(f)
f.close()

for unit in compile_dict:
    os.chdir(unit['directory'])
    n = 3
    t = 0;
    for i in range(n):
        tick = time.time()
        os.system(unit['command'])
        tock = time.time()
        t += tock - tick
    unit['time'] = t/n

    print(unit['file'] + " " + str(unit['time']))

f = open('timing.json', 'w')
json.dump(compile_dict, f)
f.close()
