import pandas as pd

personal_list = {
    'ad': ['John', 'Anna', 'Peter', 'Linda'],
    'yas': [24, 13, 53, 33],
    'maas': [3500, 2000, 4500, 5000]
}

print(type(personal_list)) # <class 'dict'>

df = pd.DataFrame(personal_list)
print(type(df)) # <class 'pandas.core.frame.DataFrame'>
print(df)


df2 = pd.read_csv('personel_list.csv', sep=';')
print(df2) 

print(df2.head()) # ilk 5 satırı getirir
print(df2.tail()) # son 5 satırı getirir
print(df2.columns) # sütun isimlerini getirir
print(df2.describe()) # istatistiksel bilgileri getirir
print(df2.shape) # satır ve sütun sayısını getirir
print(df[df['maas'] > 4000]) # maası 4000 den büyük olanları getirir
print(df2.sum()) # sütunların toplamını getirir