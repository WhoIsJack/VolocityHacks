
# Export Volocity Settings

## General
Exports all currently active settings (channel settings, acquisition protocol and stage points)
for Volocity to a registry (.reg) file so they can be restored at a later point in time.

## Details
Author: Jonas Hartmann @ Gilmour Group @ EMBL Heidelberg [github.com/WhoIsJack]
Version: 1.0
Date: 14.07.2015
Language: Python (.py) or Batch (.bat)

## Usage
- Use the batch (.bat) version unless you specifically need Python for some reason.
- Run the program, e.g. by double-clicking it.
- When prompted, type (or copy in) the name for your settings file. You do NOT need 
  to write the .reg extension in the name, as it will be added automatically.
- Confirm with >Enter< and the file should be written to your desktop.
  Be aware that unsaved changes in Volocity (e.g. when you change the laser intensity 
  without clicking the "safe" icon afterward) will not be exported.
- Restore settings by double-clicking the .reg file while and confirming all subsequently 
  appearing prompts. Volocity must be closed during this operation. Your settings should 
  be restored once you open Volocity again.

## Notes
- Transfer between different Volocity workstations is not recommended, as the hardware 
  setup may not be the same and things might get screwed up as a consequence.

## Compatibility and Requirements
- Only works on windows. Tested on Windows 7, Vista and XP.
- If you are using the Python version, Python 2.7 or an equivalent distribution is required.

## License
None. You are free to use, change and redistribute this code as you like. 
Mention of the original author is encouraged, but not required.

## Warranty
This code is supplied "as is", without warranties or conditions of any kind. The author takes 
no responsibility for any inconvenience, damage or loss of data that may be incurred as a 
result of using this code.
