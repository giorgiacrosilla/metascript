import re
import csv

# Read the XML content from the external file
xml_file = "eyes-wide-shut-1999-transcription.xml"
with open(xml_file, "r", encoding="utf-8") as f:
    xml_content = f.read()

# Define regular expressions for extracting relevant data
timeline_pattern = r'<timeline xml:id="(.*?)".*?<when xml:id="line_start" absolute="(.*?)".*?<when xml:id="line_end" absolute="(.*?)".*?</timeline>'
matches = re.findall(timeline_pattern, xml_content, re.DOTALL)

# Initialize the CSV data list with headers
csv_data = [["index", "line_start", "line_end"]]

# Populate CSV data
for match in matches:
    index, line_start, line_end = match
    csv_data.append([index, line_start, line_end])

# Write data to CSV file
csv_filename = "output.csv"
with open(csv_filename, "w", newline="", encoding="utf-8") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(csv_data)

print(f"CSV file '{csv_filename}' created successfully.")
