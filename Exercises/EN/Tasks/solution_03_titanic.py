# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>


import os, csv
data_path = os.path.join('data','titanic.csv')
print data_path

with open(data_path,'r') as infile:
    reader = csv.reader(infile)
    data = list(reader)


print len(data)

### What percent of the people survied?

survived = 0
for d in data:
    try:
        if int(d[0]) == 1:
            survived+=1
    except ValueError:
        pass

print survived/float(len(data))*100

### Function

def titanic_function(data):
    tmp = {}
    for d in data:
        try:
            if int(d[0]) == 1:
                tmp['survived'] = tmp.get('survived',0) + 1
            else:
                tmp['not survived'] = tmp.get('not survived',0) + 1
        except ValueError:
                tmp['unknown'] = tmp.get('unknown',0) + 1
    return tmp

print titanic_function(data)

###What percent of males survived? Females?

def titanic_function(data):
    M = {}
    F = {}
    for d in data:
        try:
            if d[3] == 'male':
                if int(d[0]) == 1:
                    M['survived'] = M.get('survived',0) + 1
                else:
                    M['not survived'] = M.get('not survived',0) + 1
            elif d[3] == 'female':
                if int(d[0]) == 1:
                    F['survived'] = F.get('survived',0) + 1
                else:
                    F['not survived'] = F.get('not survived',0) + 1
            else:
                pass
        except ValueError:
            pass
    return {'male': M, 'female': F}

val = titanic_function(data)

print val['male']['survived']/float( val['male']['survived'] + val['male']['not survived'])*100
print val['female']['survived']/float(val['female']['survived'] + val['female']['not survived'])*100

