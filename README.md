# DB Folder CSV to YAML Markdown
Create markdown files from CSV for DBFolder (ObsidianMD Plugin).

## Process
- Skips header values from the CSV file.
- Appends cells to `lines`.
- Uses a `for` loop to create the following code:
```
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
```
- Go to main.py and modify according to the header that one uses.
- Indexes in rows are columns.

## Notes
I only needed this for one usecase, which is why it is not robust. But it can be easily modified according to one's own needs.