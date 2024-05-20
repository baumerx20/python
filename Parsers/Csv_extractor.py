import csv

#Starter for examining output files

def extract_columns_and_rows(input_file, output_file, columns_to_extract, rows_to_extract):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=columns_to_extract)
        writer.writeheader()

        for row in reader:
            if all(row.get(col) for col in columns_to_extract) and any(row.get(col) in rows_to_extract for col in columns_to_extract):
                writer.writerow({col: row[col] for col in columns_to_extract})


input_file = 'large_file.csv'
output_file = 'extracted_data.csv'
columns_to_extract = ['column1', 'column2', 'column3'] 

extract_columns_and_rows(input_file, output_file, columns_to_extract, rows_to_extract)
