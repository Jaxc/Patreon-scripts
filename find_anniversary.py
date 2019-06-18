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

this_month = datetime.today().replace(day=1)
last_month = this_month - timedelta(days=1)
next_month = this_month + timedelta(days=32)

# Open input file
with open(input_file, 'r') as csv_file:
	# Open target file (will be overwritten)
	with open('patreon_anniversary.txt', 'w', newline='') as file_out:
		# Read CSV data
		csv_data = csv.reader(csv_file, delimiter=',')

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
			try :
				if((float(row[3]) > 0) and (float(row[4]) > 0) and (row[5] == 'Ok')):
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
			except:
				# Error in row, could not parse
				print(row)

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
