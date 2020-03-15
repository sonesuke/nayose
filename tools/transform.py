import csv
import re

state = set()
city = set()
with open('data/KEN_ALL.CSV', encoding="cp932") as f, open('test.csv', 'w') as g:
    reader = csv.reader(f)
    for row in reader:
        s = row[6]
        state.add(s)
        m = re.match('(大和郡山市|小郡市|蒲郡市)(.*)', row[7])
        if m:
            c = m[1]
            st = m[2] + row[8]
        else:
            m = re.match('(.+郡)(.+)', row[7])
            c = m[1] if m else row[7]
            st = m[2] + row[8] if m else row[8]
        city.add(c)
        full = row[6] + row[7] + row[8]
        g.write(','.join([full, s, c, st]) + '\n')

with open('states.txt', "w") as f:
    for s in state:
         f.write('"' + s + '",')

with open('cities.txt', "w") as f:
    for c in city:
        f.write('"' + c + '",')
