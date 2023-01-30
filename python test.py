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

# sample_data = pd.read_csv('sample_data.csv')
# print(sample_data.head())
# print(type(sample_data))
# print(sample_data.column_c.iloc[2])
#
# plt.plot(sample_data.column_a, sample_data.column_b)
# plt.plot(sample_data.column_a, sample_data.column_c, 'o')
# plt.show()
#
# countries = pd.read_csv('countries.csv')
# print(countries)

#Compare the population growth in the US and United Kingdom

# us = countries[countries.country == 'United States']
# print(us)
# print(countries.country.unique())
#
# uk = countries[countries.country == 'United Kingdom']
# print(uk)

# plt.plot(us.year, us.population / 10**6)
# plt.plot(uk.year, uk.population / 10**6)
# plt.legend(['us', 'uk'])
# plt.xlabel('year')
# plt.ylabel('population')
# plt.show()


# a = us.population.iloc[0]
# b = us.population
# calc_per = b/a*100
# print(calc_per)
#c = uk.population.iloc[0]
#
# plt.plot(us.year, us.population / a * 100)
# plt.plot(uk.year, uk.population / c * 100)
# plt.legend(['us', 'uk'])
# plt.xlabel('year')
# plt.ylabel('population growth (first year)')
# plt.show()


# Data Pokemon
poke = pd.read_csv('pokemon_data.csv')
print(poke.head(5))
print(poke.tail(10))
print(poke.columns)
print(poke['Name'][0:11])
print(poke[['Name', 'Type 1', 'Type 2']])
print(poke.iloc[3,1])

#  iteration through each row by taking all parameteres
# for index,row in poke.iterrows():
#     print(index,row)

#  iteration through specified parameter
# for index,row in poke.iterrows():
#     print(index,row['Type 1'])
#
# print(poke.loc[poke['Type 1']=="Ground"]) # where clause in sql
#
# print(poke.describe())
#
# print(poke.sort_values('Type 1', ascending=False)) # desc as in sql
# print(poke.sort_values(['Type 1', 'Name'], ascending=[1,0]))

# Starting to amend the data

# poke['Total'] = poke['HP'] + poke['Attack'] + poke['Defense'] + poke['Sp. Def'] + poke['Sp. Atk'] + poke['Speed']

# print(poke.head(10))
# poke = poke.drop(columns='Total')


poke['Total'] = poke.iloc[:, 4:10].sum(axis=1) #another way to sum the values , axis =1 means it would add horizontally values , for vertically use axis = 0
print(poke.head(5))


