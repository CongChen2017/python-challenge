import os
import csv

# dictionary of States

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# specify folder name

folderName = 'raw_data'

# Loop through files in target folder

fileNames = os.listdir(folderName)

for filename in fileNames:

	# set file path

	csvpath = os.path.join(folderName, filename)

	# initiate lists

	EmpID = []
	First = []
	Last = []
	newDOB = []
	newSSN = []
	newState = []

	# read csv file

	with open(csvpath, newline='') as csvfile:

		csvreader = csv.reader(csvfile, delimiter=',')

		# skip the header row

		next(csvreader, None)

		# loop remaining rows and write data into lists

		for row in csvreader:

			EmpID.append(row[0])
			First.append(row[1].split(" ")[0])
			Last.append(row[1].split(" ")[1])
			newDOB.append(row[2].split("-")[1] + "/" + row[2].split("-")[2] + "/" + row[2].split("-")[0])
			newSSN.append("***-**-" + row[3].split("-")[2])
			newState.append(us_state_abbrev[row[4]])

	# zip all lists into tuples
	newcsv = zip(EmpID, First, Last, newDOB, newSSN, newState)

	# Open file using "write" mode. Specify the variable to hold the contents
	with open('New_' + filename, 'w', newline='') as newfile:

	    # Initialize csv.writer
	    csvwriter = csv.writer(newfile, delimiter=',')

	    # Write the first row (column headers)
	    csvwriter.writerow(['Emp ID', 'First Name', 'Last Name',
	    'DOB', 'SSN', 'State'])

	    # Write other rows
	    for employee in newcsv:
	        csvwriter.writerow(employee)



