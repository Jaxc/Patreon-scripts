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

# Print error fpr incorrect number of arguemnts
if (len(sys.argv) != 2) :
	print ("Incorrect number of arguments.")
	print ("Correct usage:")
	print ("find_anniversary.py filename")
	print ("Exiting")
	exit()

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
