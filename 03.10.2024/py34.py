import pandas as pd
cities, city2region, countries, region2country, regions = pd.read_csv('cities.csv'), pd.read_csv('city2region.csv'), pd.read_csv('countries.csv'), pd.read_csv('region2country.csv'), pd.read_csv('regions.csv')
country = input()
towns = list()
town = 0
for row in countries.iterrows():
    if row[1]['Country Name'] == country:
        for row1 in region2country.iterrows():
            if row1[1]['Country ID'] == row[1]['Country ID']:
                for row2 in city2region.iterrows():
                    if row2[1]['Region ID'] == row1[1]['Region ID']:
                        for row3 in cities.iterrows():
                            if row3[1]['City ID'] == row2[1]['City ID']:
                                towns.append(row3[1]['City Name'])
                                break
        break
print(towns)

