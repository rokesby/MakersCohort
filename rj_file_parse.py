import os

from datetime import datetime

# Find the directory we executed the script from:
execution_dir = os.getcwd()

# Find the directory in which the current script resides:
file_dir = os.path.dirname(os.path.realpath(__file__))

# Print results
print(f"Execution dir - CWD: {execution_dir}")
print(f"File dir: {file_dir}")

filename = "/Users/reza/Code/python_foundations/extension_challenges/01_files/program/AirQuality.csv"

# Check if the file exists
# Open the file in read only mode.
f = open(filename, "r")
        
# Utilise the readlines file.
file_contents = f.readlines()

# Close the file once finished.
f.close

# Traverse each line and split() by semi colon. Grab the fourth column for averages.
count = 0
# running_total = 0

# monthTotals = {
#         '01' : [],
#         '02' : [],
#         '03' : [],
#         '04' : [],
#         '05' : [],
#         '06' : [],
#         '07' : [],
#         '08' : [],
#         '09' : [],
#         '10' : [],
#         '11' : [],
#         '12' : [],
#     }

month_list = {}

global_header = file_contents[0]
# print(file_contents[0])
# Drop the first row as we don't need for averages.
file_contents.pop(0)
# print(file_contents[0])


def create_month_file(month_file_name, list_of_rows):


    path_name = "/Users/reza/Code/python_foundations/extension_challenges/01_files/program/monthly_responses/"    
    f = open(path_name + month_file_name + ".csv", "w" )

    # Write the first line of headers.
    f.write(global_header)
    #file_contents = get_file_contents(filename)
    #f.write(file_contents[0])
    
    #file_contents.pop(0)

    for line in list_of_rows:
        #split_list = line.split(';')
    
        # Grab the value
        #if (split_list[0][3:5])=='03':
        # Write out line
        f.write(line)

    f.close



for line in file_contents:
    count += 1
    # Split the delimited line up into fields.
    split_list = line.split(';')    
    
    # If there is a date field populated, extract the month from it.
    if (split_list[0] != ""):
        #print(split_list[0])
        # monthTotals.get(split_list[0][3:5]).append(int(split_list[3]))
        # Populate the date string.
        line_date = datetime.strptime(split_list[0], "%d/%m/%Y")
        #print(line_date)
        # Extract the year and date.
        line_year = line_date.year
        line_month = line_date.month
        key = line_date.strftime('%m-%Y')
        #print(line_date.strftime('%m-%Y'))
        # month_year = str(line_month) + "-" + str(line_year)
        #print(key)

        # Check to see if this year/month combination is in the dictionary before we add this line to it.
        if key in month_list:
            # Add this line to the existing list of lines
            month_list.get(key).append(line) 
        else:
            # This is a new entry in the dictionary.
            new_line = []
            new_line.append(line)
            month_list_item = {key:new_line}
            month_list.update(month_list_item)


#print ("1st dictionary: " , month_list)

for month, lines in month_list.items():
    # Create a file for each item in the dictionary
    create_month_file(month, lines)


print(os.path.isdir("monthly_responses"))





