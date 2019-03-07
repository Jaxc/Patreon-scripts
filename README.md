# Parse Patron
A script can be used to convert a csv output from patreon and convert this to a txt file with columns.

If you use this, please give me a shoutout and send me a message on twitter @jaxcieofficial

I just like to know that my things are helping someone :)

# Usage:
## Parse Patrons
python parse_patron.py filename

python parse_patron.py filename n_col

python parse_patron.py filename n_col name_spacing

n_col dictates how many columns the names shall be outputted as.

name_spacing dictates how many characters wide each row is. Names longer than this will be truncated.

Unless overridden, the default values for n_col is 3 and name_spacing is 25

results will be shown in patons_out.txt

## Find anniversary
python  find_anniversary.py filename  

results will be shown in "anniversary_out.txt"
