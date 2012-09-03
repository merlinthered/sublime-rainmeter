import sublime, sublime_plugin, os.path, rainmeter

class RainmeterOpenSkinsFolderCommand(sublime_plugin.WindowCommand):
	def run(self):
		skinspath = rainmeter.skins_path
		if not skinspath or not os.path.exists(skinspath):
			sublime.error_message("Error while trying to open Rainmeter skins folder: Directory not found. Please check the value of your \"skins_path\" setting.")
			return 
		self.window.run_command("open_dir", {"dir": skinspath})
