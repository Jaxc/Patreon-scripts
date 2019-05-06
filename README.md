# Parse Patron
A script can be used to convert a csv output from patreon and convert this to a txt file with columns.

If you use this, please give me a shoutout and send me a message on twitter @jaxcieofficial .

I just like to know that my things are helping someone :)

# Usage:
Two scripts are provided, one for outputting all Patreon backers names and one for finding aniversaries.
Both scripts are configured by the config.ini file. Once configured just run the file to get the disired output.
The input \*.csv file needs to be placed in the same folder as the scrips and config files.

The output for parse_patron is shown in "patons_out.txt" and the output of find_anniversary.py is shown in "anniversary_out.txt". Both of these files will be stored in the folder the script is executed from and will overwrite any old files with the same name.

The following settings are available to configure
## INPUT
INPUT controls settings for the different tools. The current settings are:
### DEFAULT_INPUT
  This flag tells if the file is of the patreon export file name (PatreonReport_YYYY_MM_DD.csv)
  ```Y``` marks that the default name is used.
  
  Default value: ```Y```
### INPUT_FILE
  This flag defines the name of the file to be read, only used if DEFAULT_INPUT is set to something other than ```Y```.
  
  Default Value: ```<empty>```
## PARSE_PATREON
This section of config holds settings for the parse_patreon script.
### NAME_SPACING
  This parameter dictates how many characters wide each column is. Names longer than this will be truncated.
  
  Default Value: ```25```
### N_COL
  This parameter dictates how many columns the names shall be outputted as.
  
  Default value: ```3```
