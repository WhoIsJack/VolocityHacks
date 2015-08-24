# -*- coding: utf-8 -*-
"""
Created on Thu Jul 02 14:55:41 2015

# Author	      Jonas Hartmann @ Gilmour Group @ EMBL Heidelberg

# Version		1.0

# Date	      14.07.2015

# Function		Exports HKEY_CURRENT_USER\...\Volocity key-value pairings to 
                 a .reg file on the Desktop. Such files can be used to restore 
                 registry entries and thus restore Volocity settings.

# License		None. You are free to use, change and redistribute this code 
                 as you like. Mention of the original author is encouraged, 
                 but not required.

# Warranty		This code is supplied "as is", without warranties or 
                 conditions of any kind. The author takes no responsibility 
                 for any inconvenience, damage or loss of data that may be 
                 incurred as a result of using this code.
            
"""

# Display information
print "---"
print "Volocity Settings Export Tool"
print "Made by Jonas Hartmann @ Gilmour Group"
print "Please report unexpected behavior to jonas.hartmann@embl.de"
print "---\n"

# Ask user for filename
print "You are exporting Volocity's current settings."
print "The settings file will appear on the desktop."
filename = raw_input("Please enter the desired output filename (without extension): ")

# Export the reg file for Volocity to the specified filename
# Warning: Volocity's registry path may have to be adjusted depending on the 
#          installation of Volocity, although I have not seen this to be
#          necessary on any of the machines I've tested it.
from os import system
system("reg export HKCU\\SOFTWARE\\Improvision\\Volocity \"C:\\Users\\Gilmour Lab\\Desktop\\"+filename+".reg\"")

# Wait for 3 seconds before closing the prompt.
from time import sleep
sleep(3)