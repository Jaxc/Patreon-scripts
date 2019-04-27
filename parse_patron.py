###############################################################################
# Patron name converter
# Made by Jaxcie
#
# This script can be used to convert a csv output from patreon and convert 
# this to a txt file with columns.
###############################################################################


# import csv to handle file
import csv
# import sys for input arguments
import sys
# import configparser to parse the config file
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

if config.has_option('INPUT', 'INPUT_FILE') :
	input_file = config['INPUT']['INPUT_FILE'];
else :
	# Error no input file name in config file.
	print ("Error no INPUT_FILE under INPUT in config file.")
	
if config.has_option('OUTPUT', 'NAME_SPACING') :
	name_spacing = int(config['OUTPUT']['NAME_SPACING']);
else :
	# Error no NAME_SPACING under OUTPUT in config file.
	print ("Error no NAME_SPACING under OUTPUT in config file.")
	
if config.has_option('OUTPUT', 'N_COL') :
	n_col = int(config['OUTPUT']['N_COL']);
else :
	# Error no N_COL under OUTPUT in config file.
	print ("Error no N_COL under OUTPUT in config file.")

# Open input file
with open(input_file) as csv_file:
	# Open target file (will be overwritten)
	with open('patons_out.txt', 'w', newline='') as file_out:
		# Read CSV data
		csv_data = csv.reader(csv_file, delimiter=',')
		
		# Extract names and spacing to the list names
		names = []
		for row in csv_data:
			try :
				if((float(row[3]) > 0.0) 
					and (float(row[4]) > 0.0) 
					and (row[5] == 'Ok')):
					# Concatenate first and last name
					name = row[0] + ' ' + row[1]
					# If name is to long, truncate it.
					if len(name) >= name_spacing :
						name = name[0:name_spacing - 1]
					# Spaces are inserted for uniform columns
					name = '{:<{width}}'.format(name, width=name_spacing)

					# Add to list
					names.append(name)
			except:
				# Error in row, could not parse
				print(row)
			
		i = 0	
		# Format the list in to columns and write to file
		for i in range(0, len(names) - n_col + 1, n_col) :
			for j in range(i, i + n_col):
				file_out.write(names[j])
			file_out.write("\r\n")
		
		# Fix last row if number of names if it isn't evently divided by n_col
		if (len(names) < n_col) :
			for j in range(i, len(names)):
				file_out.write(names[j])
		else :
			for j in range(i + n_col, len(names)):
				file_out.write(names[j])
		# Add final line break
		file_out.write('\r\n')
