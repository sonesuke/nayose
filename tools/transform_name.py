import pandas as pd


first = []
last = []
with open("data/ime-import.txt", encoding="cp932") as f:
    for line in f.readlines():
        if line[0] == '!':
            continue
        pronunciation, characters, type = line.split('\t')
        if type.strip() == "姓":
            last.append(characters)
        elif type.strip() == "名":
            first.append(characters)

df = pd.DataFrame({'name': first})
df['count'] = 1
print(df)
df.to_feather("first_name.ft")

df = pd.DataFrame({'name': last})
df['count'] = 1
print(df)
df.to_feather("last_name.ft")
cd