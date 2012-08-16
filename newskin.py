import sublime, sublime_plugin, os.path

class NewSkinCommand(sublime_plugin.WindowCommand):
	def run(self):
		view = self.window.new_file()
		view.run_command("insert_snippet", {"name": "Packages/Rainmeter/Snippets/skin.sublime-snippet"})
		
		if os.path.exists("Packages/User/Rainmeter.tmLanguage"):
			view.set_syntax_file("Packages/User/Rainmeter.tmLanguage")
		else:
			view.set_syntax_file("Packages/Rainmeter/Rainmeter.tmLanguage")


