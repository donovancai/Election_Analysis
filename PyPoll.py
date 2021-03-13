# The data we need to retrieve

#1. Total number of votes cast

#2. A complete list of candidates who received votes

#3. Total number of votes each candidate received

#4. Percentage of votes each candidate won

#5. The winner of the election based on popular vote


import csv
import os


# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis","election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save,"w") as outfile:

    # Write some data to the file.
    outfile.write("Counties in the Election\n")
    outfile.write("-" * 20 + "-\n")
    outfile.write("Arapahoe, \nDenver, \nJefferson")

# Close the file
outfile.close()

with open(file_to_load) as election_data:
# Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    headers= next(file_reader)
    print(headers)