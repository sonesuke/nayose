import pandas as pd

df = pd.read_csv('data/KEN_ALL.CSV', encoding="cp932", header=None, dtype=str)

df['Zip'] = df[2]
df['State'] = df[6]
df['Address'] = df[6] + df[7] + df[8]

city_1 = df[7].str.extract('(大和郡山市|小郡市|蒲郡市)(.*)')
df.loc[city_1[0].notnull(), 'City'] = city_1[0]
df.loc[city_1[0].notnull(), 'Street'] = city_1[1].fillna('') + df[8]

city_2 = df[7].str.extract('(.+郡)(.+)')
index = df['City'].isnull()
df.loc[index, 'City'] = city_2[0]
df.loc[index, 'Street'] = city_2[1].fillna('') + df[8]

index = df['City'].isnull()
df.loc[index, 'City'] = df[7]
df.loc[index, 'Street'] = df[8]

df = df[['Zip', 'State', 'City', 'Street', 'Address']]


def serialize(df, columns, file_path):
    tgt = df[columns].drop_duplicates()
    tgt = tgt.reset_index(drop=True)
    tgt.to_feather(file_path)


serialize(df, ['State'], 'state.ft')
serialize(df, ['City'], 'city.ft')
serialize(df, ['Address'], 'address.ft')
serialize(df, ['State', 'City', 'Street', 'Address'], 'test.ft')
