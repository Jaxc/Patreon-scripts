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
# import os functions for file IO
import os
# import regex functions
import re
# import glob to filter csv files.
import glob
# import datetime to determine newest files
import datetime
# import shared functions
from patreon_support_functions import * 

# Read parameters from config.ini
default_input = read_config_param('INPUT', 'DEFAULT_INPUT')
input_file = read_config_param('INPUT', 'INPUT_FILE')
name_spacing = int(read_config_param('PARSE_PATREON', 'NAME_SPACING'))
n_col = int(read_config_param('PARSE_PATREON','N_COL'))


if default_input == 'Y':
	path=os.getcwd()
	csv_files = glob.glob('*.{}'.format('csv'))
	patreon_reports_name = []
	patreon_reports_date = []
	for csv_file in csv_files :
		standard_csv = re.search('PatreonReport_(\d{4}_\d{2}_\d{2})\.csv', csv_file)
		if standard_csv is not None :
			patreon_reports_date.append(datetime.datetime.strptime(standard_csv.group(1), '%Y_%m_%d'))
	newest_date = max(patreon_reports_date)
	input_file = newest_date.strftime("PatreonReport_%Y_%m_%d.csv")

# Open input file
with open(input_file) as csv_input_file:
	# Open target file (will be overwritten)
	with open('patons_out.txt', 'w', newline='') as file_out:
		# Read CSV data
		csv_data = csv.reader(csv_input_file, delimiter=',')
		
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
