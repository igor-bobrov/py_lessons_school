import pandas as pd
Regions, Countries, Cities  = pd.read_excel('dict_complete_data.ods', engine='odf', sheet_name="Регионы"), pd.read_excel('dict_complete_data.ods', engine='odf', sheet_name="Страны"), pd.read_excel('dict_complete_data.ods', engine='odf', sheet_name="Города")
country = input()
for row in Countries.iterrows():
    if row[1]['name'] == country:
        c_id = row[1]["country_id"]
        for i in Cities.iterrows():
            if c_id == i[1]["country_id"]:
                print (i[1]['name'])
        break