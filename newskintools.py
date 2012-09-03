import sublime, sublime_plugin, os, re, rainmeter, time

#Opens a new view and inserts a skin skeleton
class RainmeterNewSkinFileCommand(sublime_plugin.WindowCommand):
	def run(self):
		view = self.window.new_file()
		view.run_command("insert_snippet", {"name": "Packages/Rainmeter/Snippets/skin.sublime-snippet"})
		
		if os.path.exists("Packages/User/Rainmeter.tmLanguage"):
			view.set_syntax_file("Packages/User/Rainmeter.tmLanguage")
		else:
			view.set_syntax_file("Packages/Rainmeter/Rainmeter.tmLanguage")

#Prompts the user for the name of a skin and creates 
#a new skin of that name in the skins folder, if it doesn't already exist.
#Then opens the skin file, inserts a basic skin skeleton and refreshes Rainmeter
class RainmeterNewSkinCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.window.show_input_panel("Enter Skin Name:", "", (lambda name: self.createskin(name)), None, None)

	def createskin(self, name):		
		skinspath = rainmeter.skins_path
		if not skinspath or not os.path.exists(skinspath):
			sublime.error_message("Error while trying to create new skin: Skins path could not be found. Please check the value of your \"skins_path\" setting.")
			return

		name = os.path.normpath(name) + "\\"

		#Path where the new ini file will be created
		newskinpath = os.path.join(skinspath, name)

		#Path where the @Resources folder should be created
		basepath = os.path.join(skinspath, re.match("(.*?)\\\\", name).group(1))

		try:
			os.makedirs(newskinpath)
		except os.error:
			sublime.error_message("Error while trying to create new skin: Directory " + newskinpath + " could not be created. Does it already exist?")
			return

		try:
			os.makedirs(basepath + "\\@Resources"),
			os.makedirs(basepath + "\\@Resources\\Images")
			os.makedirs(basepath + "\\@Resources\\Fonts")
			os.makedirs(basepath + "\\@Resources\\Scripts")
		except os.error:
			sublime.status_message("Did not create @Resources folder or subfolders because they already exist")
		

		window = self.window
		filename = os.path.basename(os.path.normpath(name))
		open(newskinpath + filename + ".ini", 'a')
		newview = window.open_file(newskinpath + filename + ".ini")
		#we have to wait until the file is fully loaded (even if it's empty because it was just created)
		sublime.set_timeout((lambda: self.openskinfile(newview)), 100)

	def openskinfile(self, view):		
		if view.is_loading():
			sublime.set_timeout((lambda: self.openskinfile(self, newview)), 100)
			return

		view.run_command("insert_snippet", {"name": "Packages/Rainmeter/Snippets/skin.sublime-snippet"})

		if os.path.exists("Packages/User/Rainmeter.tmLanguage"):
			view.set_syntax_file("Packages/User/Rainmeter.tmLanguage")
		else:
			view.set_syntax_file("Packages/Rainmeter/Rainmeter.tmLanguage")

		self.window.run_command("refresh_config", {"cmd": []})
