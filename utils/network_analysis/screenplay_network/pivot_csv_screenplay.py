import pandas as pd

# Read the CSV file
csv_file = 'interactions_screenplay.csv'  # Replace with the actual file path
df = pd.read_csv(csv_file)


df = df.sort_values(by='Scene') 

# Pivot the DataFrame
pivot_df = df.pivot(index='Scene', columns='Name', values='Interactions').fillna(0)

# Reset index and rename columns
pivot_df = pivot_df.reset_index()
pivot_df.columns.name = None


# Save the pivoted DataFrame to a new CSV file
output_csv = 'output.csv'  # Replace with the desired output file path
pivot_df.to_csv(output_csv, index=False)

print("Pivoted data saved to", output_csv)

import pandas as pd

input_filename = 'output.csv'
output_filename = 'clean_output.csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(input_filename)

# Iterate through each column and convert floating-point numbers to integers
for column in df.columns:
    df[column] = df[column].apply(lambda x: int(x) if pd.notnull(x) and isinstance(x, float) else x)

# Write the modified DataFrame back to a CSV file
df.to_csv(output_filename, index=False)

print("Conversion complete. Output written to", output_filename)
