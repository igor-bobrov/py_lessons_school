import pandas as pd # была изм на иное
cities, city2region, countries, region2country, regions = pd.read_csv('cities.csv'), pd.read_csv('city2region.csv'), pd.read_csv('countries.csv'), pd.read_csv('region2country.csv'), pd.read_csv('regions.csv')
for row in cities.iterrows():
    reg, cou = '', ''
    for row1 in city2region.iterrows():
        if row1[1]['City ID'] == row[1]['City ID']:
            for row2 in regions.iterrows():
                if row2[1]['Region ID'] == row1[1]['Region ID']:
                    reg = row2[1]['Region Name']
                    break
            for row2 in region2country.iterrows():
                if row2[1]['Region ID'] == row1[1]['Region ID']:
                    for row3 in countries.iterrows():
                        if row3[1]['Country ID'] == row2[1]['Country ID']:
                            cou = row3[1]['Country Name']
                            break
                    break
            break
    print(str(row[1]['City Name']) + ', ' + str(reg) + ', ' + str(cou))
