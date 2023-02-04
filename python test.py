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

colms = list(poke.columns)
poke = poke[colms[0:4] + [colms[-1]] + colms[4:12]]

print(poke.head(10))

poke.to_csv('modified_pokemon.csv', index = False)

# More filtering --------

new_df = poke.loc[(poke['Type 1'] == 'Grass' ) | (poke['Type 2'] == 'Poison')] # or = | and = &

print(new_df)
new_df.to_csv('filtered.csv', index = False)
print(poke.loc[poke['Name'].str.contains ('Mega')])
print(poke.loc[~poke['Name'].str.contains('Mega')]) # ~ --> not equal as an ex

import re # regular expressions as an ex. or symmbol in str.contains

# print(poke.loc[poke['Type 1'].str.contains('Fire|Grass', regex=True)]) # python is case sensitive what we can add is flags=re.I

print(poke.loc[poke['Type 1'].str.contains('Fire|Grass', flags=re.I, regex=True)])

print(poke.loc[poke['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)]) # ^ --> this weed out pi in the mid and [a-z]* everything that comes after

# Conditional Changes

poke.loc[poke['Type 1'] == 'Fire', 'Type 1'] = 'Flamer'
print(poke)

poke.loc[poke['Total'] > 600, 'Legendary'] = 'CHECK'
print(poke)

 # AGGREGATE STATISTICS (GROUP BY)
poke = pd.read_csv('pokemon_data.csv')
print(poke)
average = poke.groupby(['Type 1']).mean()
print(average)

sorting = poke.groupby(['Type 1']).mean().sort_values('Speed', ascending=False) # instead of mean we can use sum() or count()
print(sorting)

counting = poke.groupby(['Type 1']).count()
print(counting)

poke['count'] = 1

counting_ = poke.groupby(['Type 1', 'Type 2']).count()['count']
print(counting_)

# WORKING WITH A LARGE DATASET
for df in pd.read_csv('pokemon_data.csv', chunksize=10): #downsize it to 10 rows
    print("CHUNK")
    print(df)