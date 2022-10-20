import pandas as pd


# name of the file
file = pd.ExcelFile('Precios-área-y-producción-de-café.xlsx')

# name of the sheet '6. Precio OIC Mensual'
df = pd.read_excel(file, sheet_name = '6. Precio OIC Mensual')
# df = pd.read_excel(file, sheet_name = '6. Precio OIC Mensual')
df.head()

# removes the first column as it doesn't have any data
df = df.drop(df.columns[[0,-1]], axis = 1)

# remove the first 5 columns as is part of the format in the excel file
df = df.drop(index = df.index[0:6],
       axis = 0)

# because the first 5 rows where deleted, I need to reset the index to be 0 and not to start at row # 6
df = df.reset_index(drop=True)

# renames the column for an easier comprenhesion 
df = df.rename(columns = {'Unnamed: 1': 'Date', 'Unnamed: 2':'OIC_price',
                          'Unnamed: 3':'Colombia_ny', 'Unnamed: 4':'Colombia_europe', 'Unnamed: 5':'Colombia_average',
                          'Unnamed: 6':'Other_ny', 'Unnamed: 7':'Other_europe','Unnamed: 8':'Other_average',
                          'Unnamed: 9':'Brazil_ny', 'Unnamed: 10':'Brazil_europe', 'Unnamed: 11':'Brazil_average',
                          'Unnamed: 12':'Robustas_ny', 'Unnamed: 13':'Robustas_europe','Unnamed: 14':'Robustas_average'})
df.head()

print(df.columns)

# create a copy of the data frame to modify it and to keep the original intact
eda = df.copy()

# checking that both dataframes are diffetent in memory
print(f' Memory for df: {id(df)} ----- Memory for eda: {id(eda)}')
# changes the format of the column 'Date' for just the year and the month
eda['Date'] = pd.to_datetime(eda['Date'], format = '%d%m%Y')

lista = list(eda.columns)
lista.pop(0)

for item in lista:
    eda[item] = eda[item].astype(float)
    
#checking descriptive statistics
eda.describe()

# saves the table as a png or svg
#df_styled = eda.describe().style.background_gradient()
#dfi.export(df_styled, "table statistics.png")
