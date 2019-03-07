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

	
# Open input file
with open(sys.argv[1], 'r') as csv_file:
	# Open target file (will be overwritten)
	with open('patons_out.txt', 'w') as file_out:
		# Read CSV data
		csv_data = csv.reader(csv_file, delimiter=',')
		# Skip header row
		next(csv_data)
		
		# Extract names and spacing to the list names
		names = []
		for row in csv_data:
			if((int(row[3]) > 0) and (int(row[4]) > 0) and (row[5] == 'Ok')):
				# Concatenate first and last name
				name = row[0] + ' ' + row[1]
				# If name is to long, truncate it.
				if len(name) >= name_spacing :
					name = name[0:name_spacing - 1]
				# Spaces are inserted for uniform columns
				name = '{:<{width}}'.format(name, width=name_spacing)

				# Add to list
				names.append(name)
		i = 0	
		# Format the list in to columns and write to file
		for i in range(0, len(names) - n_col + 1, n_col) :
			for j in range(i, i + n_col):
				file_out.write(names[j])
			file_out.write('\r\n')
		
		# Fix last row if number of names if it isn't evently divided by n_col
		for j in range(i + n_col, len(names)):
			file_out.write(names[j])
			
		# Add final line break
		file_out.write('\r\n')
