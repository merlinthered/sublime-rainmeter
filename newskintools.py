import sublime, sublime_plugin, os, getskinspath, time

#Opens a new view and inserts a skin skeleton
class NewSkinFileCommand(sublime_plugin.WindowCommand):
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
class NewSkinCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.window.show_input_panel("Enter Skin Name:", "MySkin", (lambda name: self.createskin(name)), None, None)

	def createskin(self, name):		
		skinspath = getskinspath.get_skins_path()
		if not skinspath or not os.path.exists(skinspath):
			sublime.error_message("Error while trying to create new skin: Skins path could not be found. Please check the value of your \"skins_path\" setting.")
			return

		newskinpath = skinspath + name + "\\"

		try:
			os.makedirs(newskinpath + "\\@Resources\\Images")
			os.makedirs(newskinpath + "\\@Resources\\Fonts")
			os.makedirs(newskinpath + "\\@Resources\\Scripts")
		except os.error:
			sublime.error_message("Error while trying to create new skin: Directory " + newskinpath + " could not be created. Does it already exist?")
			return

		window = self.window
		open(newskinpath + name + ".ini", 'a')
		newview = window.open_file(newskinpath + name + ".ini")
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
