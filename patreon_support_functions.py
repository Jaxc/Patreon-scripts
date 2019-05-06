###############################################################################
# Patron support function
# Made by Jaxcie
#
# This file contains functions shared by the Python scripts
###############################################################################

# import configparser to parse the config file
import configparser

def read_config_param(section, key) :

	config = configparser.ConfigParser()
	config.read('config.ini')

	if config.has_option(section, key) :
		return config[section][key];
	else :
		# Error no key found.
		print ("Error key " + key + " not found under " + section + " in config file.")

