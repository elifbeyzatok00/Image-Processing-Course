import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('personel_list.csv', sep=';')
print (df)

plt.figure(figsize=(12, 6)) # set the size of the plot (width, height)
# plt.plot(df.ad, df.yas) # plot the data (x, y)
# plt.xlabel('Adlar') # set the x-axis label
# plt.ylabel('Yaşlar') # set the y-axis label
# plt.title('Personel Yaşları') # set the title of the plot

# plt.subplot(1, 2, 1) # (rows, columns, panel number)
# plt.plot(df.ad, df.maas)
# plt.subplot(1, 2, 2)
# plt.plot(df.ad, df.yas)

# plt.scatter(df.ad, df.maas) # scatter plot

# plt.hist(df.maas, bins=10) # histogram

plt.pie(df.maas, labels=df.ad, autopct='%1.1f%%') # pie chart

plt.show()