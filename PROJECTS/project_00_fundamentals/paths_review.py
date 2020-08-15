# REVIEW OF PATHS IN PYTHON TO ACCESS OTHER DIRECTORIES
# Santiago Garcia Arango, August 2020

import os

# Current Work Directory (Can change based on the directory where this is run)
print("\nOS.GETCWD():  ", os.getcwd())

# Current path for this specific python file (always the same)
print("\n__FILE__: ", __file__)

# Access the "parent directory" of the current python file executed
print("\nOS.PATH.DIRNAME(__FILE__): ", os.path.dirname(__file__) )

# Access upper folder two levels
upper_folder = os.path.dirname(os.path.dirname(__file__))
print("\nOS.PATH.DIRNAME(OS.PATH.DIRNAME(__FILE__)): ", upper_folder)

# Join path of folder with an specific sub-folder name (in this case "imgs")
new_path = os.path.abspath(os.path.join(upper_folder, "imgs"))
print("\nOS.PATH.ABS(OS.PATH.JOIN(upper_folder, \"imgs\")): ", new_path)
