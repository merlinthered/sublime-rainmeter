import sublime, getpass, platform, os, re, io, string, _winreg
"""Module for getting Rainmeter-specific paths"""

def get_program_path():
	"""Get the value of the #PROGRAMPATH# variable"""

	#Load setting
	settings = sublime.load_settings("Rainmeter.sublime-settings")
	rainmeterpath = settings.get("rainmeter_path", None)

	#If setting is not set, try default location
	if not rainmeterpath:
		#Default: "C:\Program Files\Rainmeter"
		programfiles = os.getenv("PROGRAMFILES")
		rainmeterpath = programfiles + "\\Rainmeter\\"

	#normalize path
	rainmeterpath = os.path.normpath(rainmeterpath) + "\\"

	#Check if path exists and contains Rainmeter.exe
	if not os.path.exists(rainmeterpath + "Rainmeter.exe"): 
		print "Path to Rainmeter.exe could not be found. Check your \"rainmeter_path\" setting."
		return
	return rainmeterpath

def get_program_drive():
	"""Get the value of the #PROGRAMDRIVE# variable"""
	
	rainmeterpath = program_path

	if not rainmeterpath: return

	if re.match("[a-zA-Z]:", rainmeterpath):
		return os.path.splitdrive(rainmeterpath)[0]

	if rainmeterpath.startswith(r"\\"):
		return os.path.splitunc(rainmeterpath)[0]

	return

def get_settings_path():
	"""Get the value of the #SETTINGSPATH# variable"""

	rainmeterpath = program_path

	if not rainmeterpath: return

	#Check if Rainmeter.ini is in Rainmeter program directory
	if os.path.exists(rainmeterpath + "Rainmeter.ini"):
		return rainmeterpath
	else: #If not, look in %APPDATA%\Rainmeter\
		appdata = os.getenv("APPDATA")
		if os.path.exists(appdata + "\\Rainmeter\\Rainmeter.ini"):
			return appdata + "\\Rainmeter\\"
		else:
			return None


def get_skins_path():
	"""Get the value of the #SKINSPATH# variable"""
	
	#First try to load the value from the "rainmeter_skins_path" setting
	settings = sublime.load_settings("Rainmeter.sublime-settings")
	skinspath = settings.get("rainmeter_skins_path", None)

	#if it's found, return it
	#We trust the user to enter something meaningful here and don't check anything.
	if skinspath: 
		return os.path.normpath(skinspath) + "\\"

	#If it's not set, try to detect it automagically
	
	rainmeterpath = program_path
	if not rainmeterpath: return

	settingspath = settings_path
	if not settingspath: return

	#First, try to read the SkinPath setting from Rainmeter.ini
	fhnd = io.open(settingspath + "Rainmeter.ini", )
	lines = fhnd.read()
	fhnd.close()

	#Find the skinspath setting in the file
	match = re.search(r"""(?imsx)
						(^\s*\[\s*Rainmeter\s*\]\s*$)  		#Find the first [Rainmeter] section
		               	(.*?
		               		(^\s*SkinPath\s*=\s* 			#Find the "SkinPath" and "="
		               			(?P<skinpath>[^$]+?)\s*?$ 	#Read until the next line ending and store in named group
		               	   	)
					   	).*?
						(?:^\s*\[\s*[^\[\]\s]+\s*\]\s*$)	#All of this needs to happen before the next section
						""", lines)

	#if skinspath setting was found, return it
	if match:
		#print "Skin path found in Rainmeter.ini"
		return match.group("skinpath").strip().replace("/", "\\")

	#if it's not found in the settings file, try to guess it

	#If program path and setting path are equal, we have a portable installation.
	#In this case, the Skins folder is inside the rainmeter path
	if rainmeterpath == settingspath:
		#print "Skin path found in #PROGRAMPATH# because portable installation"
		return rainmeterpath + "Skins\\"

	#If it's not a portable installation, we try looking into the "My Documents" folder
	#Since it could be relocated by the user, we have to query its value from the registry
	try:
		regkey = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders")
		keyval = _winreg.QueryValueEx(regkey, "Personal")

		pathrep = keyval[0]

		#The path could (and most likely, will) contain environment variables that have to be expanded first
		pathrep = os.path.expandvars(pathrep)
		
		#print "Guessed Skin path from My Documents location in registry"
		return pathrep + "\\Rainmeter\\Skins\\"

	except WindowsError:
		pass

	#If the value could not be retrieved from the registry, we try some educated guesses about default locations
	try:
		username = getpass.getuser()
	except Exception:
		print "Skins path could not be located. Please set the \"skins_path\" setting in your Rainmeter settings file."
		return
	else:
		mydocuments = ""
		#check if windows version is XP
		winversion = platform.version()
		if winversion.startswith("5"):
			mydocuments = "C:\\Documents and Settings\\" + username + "\\My Documents\\"
		else:
			mydocuments = "C:\\Users\\" + username + "\\Documents\\"
		
		print "Skin path guessed from user name and Windows version"
		return mydocuments + "Rainmeter\\Skins\\"
	
def get_plugins_path():
	"""Get the value of the #PLUGINSPATH# variable"""

	settingspath = settings_path
	if not settingspath: return
	return settingspath + "Plugins\\"

def get_addons_path():
	"""Get the value of the #ADDONSPATH# variable"""

	settingspath = settings_path
	if not settingspath: return
	return settingspath + "Addons\\"

def get_current_path(filepath):
	"""Get the value of the #CURRENTPATH# variable for the specified path.
	Returns None if the file path is not in the skins folder
	"""

	filepath = os.path.normpath(filepath)

	skinspath = skins_path
	if not skinspath or not filepath.startswith(skinspath): return

	if os.path.isfile(filepath): 
		return os.path.dirname(filepath) + "\\"
	else:
		return filepath + "\\"

def get_root_config_path(filepath):
	"""Get the value of the #ROOTCONFIGPATH# variable for the specified path
	Returns None if the path is not in the skins folder
	"""

	filepath = os.path.normpath(filepath)

	skinspath = skins_path
	if not skinspath or not filepath.startswith(skinspath): return

	relpath = os.path.relpath(filepath, skinspath)

	return skinspath + relpath.split("\\")[0] + "\\"

def get_current_file(filepath):
	"""Get the value of the #CURRENTFILE# variable for the specified path
	Returns None if the path is not in the skins folder
	"""

	filepath = os.path.normpath(filepath)

	skinspath = skins_path
	if not skinspath or not filepath.startswith(skinspath): return

	return os.path.basename(filepath)

def get_current_config(filepath):
	"""Get the value of the #CURRENTCONFIG# variable for the specified path
	Returns None if the path is not in the skins folder
	"""

	filepath = os.path.normpath(filepath)

	skinspath = skins_path
	if not skinspath or not filepath.startswith(skinspath): return

	if os.path.isfile(filepath): filepath = os.path.dirname(filepath)

	return os.path.relpath(filepath, skinspath)

def get_resources_path(filepath):
	"""Get the value of the #@# variable for the specified path
	Returns None if the path is not in the skins folder
	"""

	rfp = get_root_config_path(filepath)

	if not rfp: return

	return rfp + "@Resources\\"

def replace_variables(string, filepath):
	"""Replace Rainmeter built-in variables and Windows environment variables in string.
	
	Replaces occurrences of the following variables in the string:
	#CURRENTFILE#
	#CURRENTPATH#
	#ROOTCONFIGPATH#
	#CURRENTCONFIG#
	#@#
	#SKINSPATH#
	#SETTINGSPATH#
	#PROGRAMPATH#
	#PROGRAMDRIVE#
	#ADDONSPATH#
	#PLUGINSPATH#
	Any Windows environment variables (like %APPDATA%)
	filepath must be a skin file located in a subdirectory of the skins folder
	"""


	#lambdas for lazy evaluation
	variables = {"#CURRENTFILE#": 	lambda: get_current_file(filepath),
				"#CURRENTPATH#": 	lambda:get_current_path(filepath),
				"#ROOTCONFIGPATH#": lambda:get_root_config_path(filepath),
				"#CURRENTCONFIG#": 	lambda:get_current_config(filepath),
				"#@#": 				lambda:get_resources_path(filepath),
				"#SKINSPATH#": 		lambda: skins_path,
				"#SETTINGSPATH#": 	lambda: settings_path,
				"#PROGRAMPATH#": 	lambda: program_path,
				"#PROGRAMDRIVE#": 	lambda: program_drive,
				"#ADDONSPATH#": 	lambda: addons_path,
				"#PLUGINSPATH#": 	lambda: plugins_path}

	pattern = re.compile("(?i)" + "|".join(variables.keys()))
	#replace Rainmeter variables
	repl = pattern.sub(lambda x: variables[x.group().upper()](), string)
	#expand windows environment variables
	repl = os.path.expandvars(repl)
	return repl

def make_path(string, filepath):
	"""Make the string into an absolute path of an existing file or folder,

	replacing Rainmeter built-in variables relative to the file specified in filepath (see replace_variables())
	will return None if the file or folder doesn't exist, or if string is None or empty
	"""

	if not string: return None

	repl = replace_variables(string, filepath)
	norm = os.path.normpath(repl)
	
	#For relative paths, try folder of current file first
	
	if not os.path.isabs(norm):
		curpath = get_current_path(filepath)
		abso=norm
		if curpath:
			abso = os.path.join(curpath, norm)
		else:
			abso = os.path.join(os.path.dirname(filepath), norm)

		if os.path.exists(abso): 
			return abso
		
		#if that doesn't work, try relative to skins path (for #CURRENTCONFIG#)
		abso = os.path.join(skins_path, norm)
		if os.path.exists(abso): 
			return abso
			
	else: #for absolute paths, try opening containing folder if file does not exist
		if os.path.exists(norm): 
			return norm

		if os.path.exists(os.path.dirname(norm)):
			return os.path.dirname(norm)
		
	return

#initialize the paths 
#use these if you don't think the value could have changed since the import of the module)
program_path = get_program_path()
program_drive = get_program_drive()
settings_path = get_settings_path()
skins_path = get_skins_path()
plugins_path = get_plugins_path()
addons_path = get_addons_path()