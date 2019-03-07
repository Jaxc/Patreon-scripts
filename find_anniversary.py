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

from datetime import datetime
from datetime import timedelta

# Default values for arguments
name_spacing_default = 25
n_col_default = 3

# Print error fpr incorrect number of arguemnts
if (len(sys.argv) < 2) or (len(sys.argv) > 4):
	print ("Incorrect number of arguments.")
	print ("Correct usage:")
	print ("parse_patron filename")
	print ("parse_patron filename n_col")
	print ("parse_patron filename n_col name_spacing")
	print 
	print ("n_col dictates how many columns the names shall be outputted as.")
	print ("name_spacing dictates how many characters wide each row is. Names "
			+ "longer than this will be truncated ")
	print ("Unless overridden, the default values for n_col is " + 
			str(n_col_default) + "and name_spacing is " + 
			str(name_spacing_default))
	print("Exiting")
	exit()

	
# Set varaibles to default values unless specified
if len(sys.argv) == 2:
	name_spacing = name_spacing_default
	n_col = n_col_default
	
if len(sys.argv) == 3:
	name_spacing = name_spacing_default
	n_col = int(sys.argv[2])
	
if len(sys.argv) == 4:
	name_spacing = int(sys.argv[3])
	n_col = int(sys.argv[2])

this_month = datetime.today().replace(day=1)
last_month = this_month - timedelta(days=1)
next_month = this_month + timedelta(days=32)
	
# Open input file
with open(sys.argv[1], 'r') as csv_file:
	# Open target file (will be overwritten)
	with open('anniversary_out.txt', 'w') as file_out:
		# Read CSV data
		csv_data = csv.reader(csv_file, delimiter=',')
		# Skip header row
		next(csv_data)
		
		# Extract lists of users with anniversaries
		last_month_anniversarys = []
		this_month_anniversarys = []
		next_month_anniversarys = []
		for row in csv_data:
			# Extract name
			name = row[0] + ' ' + row[1]
			# Extract patreon start date
			patron_start = datetime.strptime(row[12], "%Y-%m-%d %H:%M:%S.%f")
			# Make sure patreon is still subscribed
			if((int(row[3]) > 0) and (int(row[4]) > 0) and (row[5] == 'Ok')):
				# Compare start against month
				if patron_start.month == last_month.month :
					# Calculate how many years since start
					years_active = str(last_month.year - patron_start.year)
					last_month_anniversarys.append(years_active + 
					" year(s) on " + str(patron_start.month) + "-" + 
					str(patron_start.day) + ": " + name + '\r\n')
					
				elif patron_start.month == this_month.month :
					years_active = str(this_month.year - patron_start.year)
					this_month_anniversarys.append(years_active + 
					" year(s) on " + str(patron_start.month) + "-" + 
					str(patron_start.day) + ": " + name + '\r\n')
					
				elif patron_start.month == next_month.month :
					years_active = str(next_month.year - patron_start.year)
					next_month_anniversarys.append(years_active + 
					" year(s) on " + str(patron_start.month) + "-" + 
					str(patron_start.day) + ": " + name + '\r\n')
				
			
		# Format the list in to columns and write to file
		file_out.write("Anniversaries this month: \r\n")
		for name in this_month_anniversarys:
			file_out.write(name)
		file_out.write('\r\n')
		
		file_out.write("Anniversaries last month: \r\n")
		for name in last_month_anniversarys:
			file_out.write(name)		
		file_out.write('\r\n')
		
		file_out.write("Anniversaries next month: \r\n")
		for name in next_month_anniversarys:
			file_out.write(name)		
		
		# Add final line break
		file_out.write('\r\n')
