import pandas as pd

def read_and_clean(file, sheet_name, output_csv):
    # Read the Excel sheet
    df = pd.read_excel(file, sheet_name=sheet_name)
    
    # Drop columns where all values are NaN
    df_clean = df.dropna(axis=1, how='all')
    
    # Save to CSV without the index column
    df_clean.to_csv(output_csv, index=False)


read_and_clean(
    file='workbooks/Energy_Stats_Financial_Tables.xlsx',
    sheet_name='Annual Sales FINAL 06262023',
    output_csv='workbooks_csv/annual_sales.csv'
)

read_and_clean(
    file='workbooks/Energy_Stats_Generation_Tables.xlsx',
    sheet_name='AnnualOperationsData 2023-11-13',
    output_csv='workbooks_csv/annual_operations.csv'
)

read_and_clean(
    file='workbooks/Energy_Stats_Generation_Tables.xlsx',
    sheet_name='Monthly Gen 2001-2021',
    output_csv='workbooks_csv/monthly_generation.csv'
)

read_and_clean(
    file='workbooks/Energy_Stats_Infrastructure_2021.xlsx',
    sheet_name='LOOKUP INTERTIES 2023-11-08',
    output_csv='workbooks_csv/interties.csv'
)

read_and_clean(
    file='workbooks/Energy_Stats_Infrastructure_2021.xlsx',
    sheet_name='Infrastructure FINAL 2023-11-13',
    output_csv='workbooks_csv/infrastructure.csv'
)

read_and_clean(
    file='workbooks/Energy_Stats_Infrastructure_2021.xlsx',
    sheet_name='LOOKUP PLANTS 2023-11-13',
    output_csv='workbooks_csv/plants.csv'
)
