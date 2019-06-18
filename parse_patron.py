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


def sortSecond(val):
    return val[1]


# Read parameters from config.ini
default_input = read_config_param('INPUT', 'DEFAULT_INPUT')
input_file = read_config_param('INPUT', 'INPUT_FILE')
name_spacing = int(read_config_param('PARSE_PATREON', 'NAME_SPACING'))
n_col = int(read_config_param('PARSE_PATREON', 'N_COL'))
output_sorting = read_config_param('PARSE_PATREON', 'OUTPUT_SORTING')
output_sorting_order = read_config_param('PARSE_PATREON', 'OUTPUT_SORTING_ORDER')

# Find latest CSV file or override it with INPUT_FILE
if default_input == 'Y':
	path=os.getcwd()
	csv_files = glob.glob('*.{}'.format('csv'))
	patreon_reports_date = []
	for csv_file in csv_files :
		standard_csv = re.search('PatreonReport_(\d{4}_\d{2}_\d{2})\.csv', csv_file)
		if standard_csv is not None :
			patreon_reports_date.append(datetime.datetime.strptime(standard_csv.group(1), '%Y_%m_%d'))
	newest_date = max(patreon_reports_date)
	input_file = newest_date.strftime("PatreonReport_%Y_%m_%d.csv")

# Decode the sorting order
sorting_ways = ['NAME', '', 'CURRENT_PLEDGE', 'LIFETIME_PLEDGE', '', '', '', '', '', '', 'COUNTRY', 'FIRST_PLEDGE_DATE', 'MAX_PLEDGED_AMOUNT']

for i in range(len(sorting_ways)) :
	if sorting_ways[i] == output_sorting:
		sort_col = i

if output_sorting_order == 'ASCENDING' :
	reverse = False
elif output_sorting_order == 'DECENDING' :
	reverse = True
else :
	raise exception ('Key OUTPUT_SORTING_ORDER in PARSE_PATREON is set incorrectly, please set it to either ASCENDING or DECENDING.')

# Open input file
with open(input_file) as csv_input_file:
	# Open target file (will be overwritten)
	with open('Patreon_name_list.txt', 'w', newline='') as file_out:
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

					# Prepare row for sorting
					row = [name, row[2], int(row[3]), int(row[4]),
						row[5],  row[6],  row[7],  row[8],  row[9],  row[10],
						row[11], row[12], int(row[13])]
					# Add to list
					names.append([name, row])
			except:
				# Error in row, could not parse
				print(row)
				print()

		# Sort names according to output sorting
		for i in range(len(names)):
			names[i][1] = names[i][1][sort_col]
		names.sort(key = sortSecond, reverse=reverse)
		i = 0
		# Format the list in to columns and write to file
		for i in range(0, len(names) - n_col + 1, n_col) :
			for j in range(i, i + n_col):
				file_out.write(names[j][0])
			file_out.write("\r\n")

		# Fix last row if number of names if it isn't evently divided by n_col
		if (len(names) < n_col) :
			for j in range(i, len(names)):
				file_out.write(names[j][0])
		else :
			for j in range(i + n_col, len(names)):
				file_out.write(names[j][0])
		# Add final line break
		file_out.write('\r\n')
