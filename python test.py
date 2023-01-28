import matplotlib.pyplot as plt
import pandas as pd


# data = (3, 6, 9, 12)
# fig, simple_chart = plt.subplots()
# simple_chart.plot(data)
# plt.show()
#
# x = [1, 2, 3]
# y = [4, 5, 9]
# z = [6, 7, 8]
# plt.plot(x,y)
# plt.plot(x,z)
# plt.title("plot")
# plt.xlabel("x axe")
# plt.ylabel("y axe and z")
# plt.legend(["this is y", "this is z"])
# plt.show()

sample_data = pd.read_csv('sample_data.csv')
print(sample_data.head())
print(type(sample_data))
print(sample_data.column_c.iloc[2])

plt.plot(sample_data.column_a, sample_data.column_b)
plt.plot(sample_data.column_a, sample_data.column_c, 'o')
plt.show()

countries = pd.read_csv('countries.csv')
print(countries)

#Compare the population growth in the US and China

us = countries[countries.country == 'United States']
print(us)