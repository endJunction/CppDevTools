#!/bin/env python3

import os
import subprocess
import pandas as pd

def nm(obj_file):
    output = subprocess.check_output(
            ['nm','-C', '-S', obj_file],
            universal_newlines=True).splitlines()

    result = []
    obj = ''
    for line in output:
        #if result:
        #    print(result[-1])
        #print(line)
        if not line.strip():
            continue
        if not line.startswith('0'):
            if not line.startswith(' '):    # an object
                obj = line
                continue

            # a symbol without address and size
            address = 0
            size = 0
            symbol_type = line.lstrip()[0]
            name = line.lstrip()[2:]
            result.append({'object':obj, 'address':address, 'size':size,
                'type':symbol_type, 'name':name})
            continue

        # a normal line
        pos = line.find(' ')
        address = int(line[0:pos], 16)
        line = line[pos:].lstrip()
        if not line.startswith('0'):
            size = 0
            symbol_type = line[0]
            name = line.lstrip()[2:]
        else:
            (size,symbol_type,name) = line.split(' ', maxsplit=2)
            size = int(size, 16)

        result.append({'object':obj, 'address':address, 'size':size,
            'type':symbol_type, 'name':name})

    return pd.DataFrame(result, dtype=int)

def count_equal(df):
    df['count'] = df.groupby(['address','name','size','type']).transform(len)

def cost_by_count_and_size(df):
    df['cost'] = df['size'] * df['count']

    for i in df.sort('cost').tail(20)['name']:
        print(i)
