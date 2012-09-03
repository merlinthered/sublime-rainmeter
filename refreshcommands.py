import sublime, sublime_plugin, getpass, rainmeter

class RainmeterRefreshConfigCommand(sublime_plugin.WindowCommand):
	"""Refresh the skin at a given file path, or Rainmeter if no path is specified"""

	def run(self, cmd):
		#Get Rainmeter exe path
		rainmeter_exe = rainmeter.program_path
		if not rainmeter_exe:
			sublime.error_message("Error while trying to refresh Rainmeter skin: The Rainmeter executable could not be found. Pleas check the value of your \"rainmeter_path\" setting.")
			return
		rainmeter_exe = rainmeter_exe + "Rainmeter.exe"

		#refresh skin (or whole rainmeter if no skin specified)
		if not cmd:
			sublime.status_message("Refreshing Rainmeter")
			self.window.run_command("exec", {"cmd": [rainmeter_exe, "!RefreshApp"]})
		else:
			config = rainmeter.get_current_config(cmd[0])
			fil = rainmeter.get_current_file(cmd[0])
			if not fil: fil = ""
			if not config:
				sublime.error_message("Error while trying to refresh Rainmeter skin: The config could not be found. Please check the path of the config and your \"rainmeter_skins_path\" setting.")

			sublime.status_message("Refreshing config: " + config)

			#load activate setting
			settings = sublime.load_settings("Rainmeter.sublime-settings")
			activate = settings.get("rainmeter_refresh_and_activate", True)

			if activate:
				self.window.run_command("exec", {"cmd": [rainmeter_exe, "!ActivateConfig", config, fil, "&&", rainmeter_exe, "!Refresh", config], "shell": True})
			else:
				self.window.run_command("exec", {"cmd": [rainmeter_exe, "!Refresh", config]})

	def description(self):
		return "Refresh Rainmeter Config"

class RainmeterRefreshCurrentSkinCommand(sublime_plugin.TextCommand):
	"""Refresh the current skin file opened in a view"""

	def run(self, edit):

		#Get current file's path
		filepath = self.view.file_name()
		if not filepath: return
		
		#refresh config
		self.view.window().run_command("rainmeter_refresh_config", {"cmd": [filepath]})

	def is_enabled(self):

		#Check if current syntax is rainmeter
		israinmeter = self.view.score_selector(self.view.sel()[0].a, "source.rainmeter")

		return israinmeter > 0

	def description(self):
		
		return "Refresh Current Rainmeter Skin"