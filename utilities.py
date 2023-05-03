import os

def add_sufix_to_files_at_folder(path,prefix = None, sufix = None, override = False):
	for file in os.listdir(path):
		# Validate if filename has more than one dot on the name
		if file.count('.') == 1:
			# Separate the filename from the extension
			file_name,extension = file.split(".")
			
			# Prep the new filenname
			new_filename = file_name
			if prefix is not None:
				new_filename = str(prefix) + new_filename
			if sufix is not None:
				new_filename = new_filename + str(sufix)
			new_filename = str(new_filename) + "." + str(extension)
			
			# Lets Rename the file
			try:
				print("Lets rename it")
				os.rename(path + file, path + new_filename)
			except FileExistsError:
				print("File already Exists")
				if override == True:
					print("Removing existing file")
				
					# Delete the existing file
					os.remove(path + file)
				
					# Rename the new file
					os.rename(path + file, path + new_filename)
				
					print('File ' + file + ' was overriten.')
		else:
			print("Can't rename files with more than one point in the name, consider contributing to improve this!")