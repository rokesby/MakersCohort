import os

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

# print(len(file_contents)) # 9742 lines of text.
print(file_contents[0])

# Drop the first row as we don't need for averages.
file_contents.pop(0)
print(file_contents[0])

# Traverse each line and split() by semi colon. Grab the fourth column for averages.
count = 0
split_list = []
running_total = 0


monthTotals = {
        '01' : [],
        '02' : [],
        '03' : [],
        '04' : [],
        '05' : [],
        '06' : [],
        '07' : [],
        '08' : [],
        '09' : [],
        '10' : [],
        '11' : [],
        '12' : [],
    }



for line in file_contents:
    count += 1
    # print("row line : ", count)
    split_list = line.split(';')
    # print("item value : ", split_list[3])
    
    # Grab the month from characters 3 and 4.
    # print("Month : ", split_list[0][3:5] )
    
    
    
    # Grab the value
    if (split_list[3] != ""):
        running_total += int(split_list[3])

        # Find the relevant dictionary item and add the value in there
            # Check for null values?
        # Based on the key, get the value
        monthTotals.get(split_list[0][3:5]).append(int(split_list[3]))
    

print("Total is : ", running_total)
print("Average is : ", round(running_total/count, 2))

print ("1st dictionary: " , monthTotals.keys())

outputTotals = {}

# Now output the results dictionary
counter=0


#for key, value in monthTotals:
    #outputTotals.update(key, len(value))
 #   counter += 1
    # len(list(value))
    # get the list lengthj
  #  my_list = list(value)
    # my_list_average = sum(my_list)/len(my_list)

    #outputTotals.__setitem__(counter, my_list_average)
    # Print out average value for each list
    #print("Dictionary key : ", key, " calc: ", len(value))

def calculate_average(numbers):
    if len(numbers)==0:
        return 0
    return round(sum(numbers)/len(numbers),2)


for month, totals in monthTotals.items():
    average = calculate_average(totals)
    outputTotals[int(month)]= average

print("2nd dictionary : ", outputTotals)


# Go through all the rows and convert the first field into a date
# Group together all the rows where the month is unique
# Send those rows to the 'average calculator' and store in a dictionary.

# stuff = "03"
# print(stuff)
# print(int(stuff))