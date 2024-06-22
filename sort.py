import pandas as pd

# Load the Excel file
file_path = 'C:/Users/anson/Documents/GitHub/ansonwcy/google_maps_scraper/combined/combined_file.xlsx' # Replace with the actual file name
df = pd.read_excel(file_path)

# Remove " · Visited link" from the 'name' column
df['name'] = df['name'].str.replace(' · Visited link', '')

# Remove duplicate rows
df = df.drop_duplicates()

# Drop rows with the same 'address'
df = df.drop_duplicates(subset='address', keep='first')

# Sort the DataFrame by 'reviews_average' column in descending order
sorted_df = df.sort_values(by='reviews_average', ascending=True)

# Save the cleaned and sorted DataFrame to a new Excel file
cleaned_sorted_file_path = 'C:/Users/anson/Documents/GitHub/ansonwcy/google_maps_scraper/combined/sorted_file.xlsx'
sorted_df.to_excel(cleaned_sorted_file_path, index=False)

cleaned_sorted_file_path
