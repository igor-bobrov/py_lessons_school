import pandas as pd
Regions, Countries, Cities  = pd.read_excel('dict_complete_data.ods', engine='odf', sheet_name="Регионы"), pd.read_excel('dict_complete_data.ods', engine='odf', sheet_name="Страны"), pd.read_excel('dict_complete_data.ods', engine='odf', sheet_name="Города")
cities, regions, countries, city2region, region2country = dict(), dict(), dict(), dict(), dict()
for row in Regions.iterrows():
    if row[1]['region_id'] not in regions:
        regions[row[1]['region_id']] = row[1]['name']
    if row[1]['region_id'] not in region2country:
        region2country[row[1]['region_id']] = row[1]['country_id']
for row in Countries.iterrows():
    if row[1]['country_id'] not in countries:
        countries[row[1]['country_id']] = row[1]['name']
for row in Cities.iterrows():
    if row[1]['city_id'] not in cities:
        cities[row[1]['city_id']] = row[1]['name']
    if row[1]['region_id'] not in city2region:
        city2region[row[1]['city_id']] = row[1]['region_id']
pd.DataFrame(list(regions.items()), columns=['ID', 'Name']).to_csv('regions.csv', index=False)
pd.DataFrame(list(cities.items()), columns=['ID', 'Name']).to_csv('cities.csv', index=False)
pd.DataFrame(list(countries.items()), columns=['ID', 'Name']).to_csv('countries.csv', index=False)
pd.DataFrame(list(city2region.items()), columns=['City ID', 'Region ID']).to_csv('city2region.csv', index=False)
pd.DataFrame(list(region2country.items()), columns=['Region ID', 'Country ID']).to_csv('region2country.csv', index=False)
