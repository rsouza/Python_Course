
zipcodes = {}
zipcodes['80403'] = 'Boulder, CO, Boulder County'
zipcodes['80123'] = 'Monument, CO El Paso County'
zipcodes['80919'] = 'Colorado Springs, CO El Paso County'

# Solution with lists
names = {}
names['Pat'] = ['80403','773-333-3445']
names['Bob'] = ['80919','773-333-3445']
names['Jane'] = ['80132','773-333-3445']

name = 'Pat'
print name, 'lives in', zipcodes[names[name][0]], names[name][1]

# Solution with dictionary
names = {}
names['Pat'] =  {'zip':'80403','phone':'773-333-3445'}
names['Bob'] =  {'zip':'80403','phone':'773-333-3445'}
names['Jane'] = {'zip':'80403','phone':'773-333-3445'}

name = 'Pat'
print name, 'lives in', zipcodes[names[name]['zip']], names[name]['phone']

