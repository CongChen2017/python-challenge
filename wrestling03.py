
import os
import csv

folderName = 'wrestling_raw_data'

fileNames = os.listdir(folderName)

for filename in fileNames:

	# set file path

	# rawfile = input("which file you want to handle? ")

	
	# csvpath = os.path.join('wrestling_raw_data', rawfile)
	csvpath = os.path.join(folderName, filename)

	# read csv file
	name = []
	win = []
	loss = []
	draw = []
	winper = []
	lossper = []
	drawper = []
	

	with open(csvpath, newline='') as csvfile:

		csvreader = csv.reader(csvfile, delimiter=',')

		next(csvreader, None)

		for row in csvreader:

			Totalgame = int(row[1]) + int(row[2]) + int(row[3])
			winperc = "{0:.2f}".format(int(row[1])/Totalgame)
			Lossperc = "{0:.2f}".format(int(row[2])/Totalgame)
			drawperc = "{0:.2f}".format(int(row[3])/Totalgame)
			name.append(row[0])
			win.append(row[1])
			loss.append(row[2])
			draw.append(row[3])
			winper.append(winperc)
			lossper.append(Lossperc)
			drawper.append(drawperc)

		allinfo = zip(name, win, loss, draw, winper, lossper, drawper)

	# Open file using "write" mode. Specify the variable to hold the contents
	with open(filename, 'w', newline='') as newfile:

	    # Initialize csv.writer
	    csvwriter = csv.writer(newfile, delimiter=',')

	    # Write the first row (column headers)
	    csvwriter.writerow(['Wrestler', 'Wins', 'Losses',
	    'Draws', 'Win percentage', 'Loss percentage', 'Draw percentage'])

	    # Write other rows
	    for player in allinfo:
	        csvwriter.writerow(player)





