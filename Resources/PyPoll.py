#Indirect Path Dependencies
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
       # Print each row in the CSV file.#'ed the following because we want to omit header
    #for row in file_reader:
        #print(row)
#If we wanted to read column headers
# for row in file_reader:
    #print(row[0])

#We don't want column headers for analysis. To make sure they are skipped by using next function:
# Print the header row.
    headers = next(file_reader)
    print(headers)





