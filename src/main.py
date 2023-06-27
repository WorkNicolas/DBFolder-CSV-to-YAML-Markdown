import csv
import os

# File Location
print('DBFolder CSV to YAML Format Converter')
source = input("Enter Directory: ")
directory = os.path.dirname(source) + '/'

with open(source, 'r') as csv_file:
    print('Converting CSV to YAML in ' + directory)
    # Read from CSV File
    csv_reader = csv.reader(csv_file)
    # Skip Header Value
    next(csv_reader)
    lines = []
    for line in csv_reader:
        lines.append(line)

    # Iterate entire CSV File
    for row in lines:
        markdown_content = f"""---
Name: {row[0]}
Type: {row[1]}
Status: {row[2]}
Score: {row[3]}
Author: {row[4]}
Completed: {row[5]}
Link: {row[6]}
Chapter: {row[7]}
Website: {row[8]}
---"""
        # Create Markdown
        filename = f"{row[0]}.md"
        print('Markdown has been saved in ' + directory + ' as ' + filename)
        with open(directory + filename, 'w') as file:
            file.write(markdown_content)
print('Process exit')
