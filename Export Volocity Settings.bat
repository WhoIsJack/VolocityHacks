@Echo off

:: Author		Jonas Hartmann @ Gilmour Group @ EMBL Heidelberg
:: Version		1.0
:: Date			14.07.2015
:: Function		Exports HKEY_CURRENT_USER\...\Volocity key-value pairings to a .reg file on the Desktop.
::				Such files can be used to restore registry entries and thus restore Volocity settings.
:: License		None. You are free to use, change and redistribute this code as you like. Mention of the
::				original author is encouraged, but not required.
:: Warranty		This code is supplied "as is", without warranties or conditions of any kind. The author 
::				takes no responsibility for any inconvenience, damage or loss of data that may be incurred
::				as a result of using this code.

:: Show information
Echo ---
Echo Volocity Settings Export Tool
Echo Made by Jonas Hartmann @ Gilmour Group
Echo Please report unexpected behavior to jonas.hartmann@embl.de
Echo ---
Echo.

:: Ask user for output filename
Echo You are exporting your current Volocity settings. 
Echo The settings file will appear on the desktop.
Set /p fn="Please enter the desired output filename (without extension): "
Echo.

:: Export the reg file for Volocity to the specified filename
:: Warning: Volocity's registry path may have to be adjusted depending on the installation of Volocity.
Reg export "HKEY_CURRENT_USER\Software\Improvision\Volocity" "%USERPROFILE%\Desktop\%fn%.reg"

:: Wait for 3 seconds before closing the prompt. Do not display waiting information.
Timeout 3 > NUL