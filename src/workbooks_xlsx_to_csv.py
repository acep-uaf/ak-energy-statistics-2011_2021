import pandas as pd

annual_sales = pd.read_excel(
    'workbooks/Energy_Stats_Financial_Tables.xlsx', 
    sheet_name = 'Annual Sales FINAL 06262023',
    header = 0)
annual_sales.to_csv('workbooks_csv/annual_sales.csv', index = False)


annual_operations = pd.read_excel(
    'workbooks/Energy_Stats_Generation_Tables.xlsx',
    sheet_name = 'AnnualOperationsData 2023-11-13',
    header = 0
)
annual_operations.to_csv('workbooks_csv/annual_operations.csv', index = False)


monthly_generation = pd.read_excel(
    'workbooks/Energy_Stats_Generation_Tables.xlsx',
    sheet_name = 'Monthly Gen 2001-2021',
    header = 0
)
monthly_generation.to_csv('workbooks_csv/monthly_generation.csv', index = False)


interties = pd.read_excel(
    'workbooks/Energy_Stats_Infrastructure_2021.xlsx',
    sheet_name = 'LOOKUP INTERTIES 2023-11-08',
    header = 0
)
interties.to_csv('workbooks_csv/interties.csv', index = False)


infrastructure = pd.read_excel(
    'workbooks/Energy_Stats_Infrastructure_2021.xlsx',
    sheet_name = 'Infrastructure FINAL 2023-11-13',
    header = 0
)
infrastructure.to_csv('workbooks_csv/infrastructure.csv', index = False)


plants = pd.read_excel(
    'workbooks/Energy_Stats_Infrastructure_2021.xlsx',
    sheet_name = 'LOOKUP PLANTS 2023-11-13',
    header = 0
)
plants.to_csv('workbooks_csv/plants.csv', index = False)
