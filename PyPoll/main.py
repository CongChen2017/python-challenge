import os
import csv
from collections import Counter

# specify folder name

folderName = 'raw_data'

# Loop through files in target folder

fileNames = os.listdir(folderName)

for filename in fileNames:


	# set file path

	csvpath = os.path.join(folderName, filename)

	# initiate list & variables

	candidate = []
	winner = ''
	vote = 0

	# read csv file

	with open(csvpath, newline='') as csvfile:

		csvreader = csv.reader(csvfile, delimiter=',')

		# skip the header row

		next(csvreader, None)

		# loop remaining rows and write data into lists

		for row in csvreader:

			candidate.append(row[2])

	# calculate total votes

	total = len(candidate)

	# generate dictionary for count results

	count = Counter(candidate)

	# loop through dictionary and find winner

	for key, value in count.items():

		if value > vote:

			winner = key
			vote = value


	# print out results in terminal

	print("")
	print("Election Results")
	print("----------------------------")
	print("Total Votes: " + str(total))
	print("----------------------------")
	for key, value in count.items():
		print(key + ": " + str("{0:.1f}".format(value/total*100)) + "% (" + str(value) + ")")
	print("----------------------------")
	print("Winner: " + winner)
	print("----------------------------")

	# generate txt file for the report

	with open('Report_' + filename.split('.')[0] + '.txt', 'w', newline='') as textfile:

		textfile.write("Election Results" + "\n")
		textfile.write("----------------------------" + "\n")
		textfile.write("Total Votes: " + str(total) + "\n")
		textfile.write("----------------------------" + "\n")
		for key, value in count.items():
			textfile.write(key + ": " + str("{0:.1f}".format(value/total*100)) + "% (" + str(value) + ")" + "\n")
		textfile.write("----------------------------" + "\n")
		textfile.write("Winner: " + winner + "\n")
		textfile.write("----------------------------")
		

