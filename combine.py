import pandas as pd
import os

# Folder containing the Excel files
folder_path = 'C:/Users/anson/Documents/GitHub/ansonwcy/google_maps_scraper/output'  # Update with the actual folder path

# List to hold DataFrames
df_list = []

# Loop through all files in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith('.xlsx'):
        file_path = os.path.join(folder_path, file_name)
        df = pd.read_excel(file_path)
        df_list.append(df)

# Concatenate all DataFrames
combined_df = pd.concat(df_list, ignore_index=True)

# Save the combined DataFrame to a new Excel file
output_file_path = 'C:/Users/anson/Documents/GitHub/ansonwcy/google_maps_scraper/combined/combined_file.xlsx'
combined_df.to_excel(output_file_path, index=False)

print(f"Combined file saved to {output_file_path}")