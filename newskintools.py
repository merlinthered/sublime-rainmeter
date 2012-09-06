import os
import re
import time

import sublime
import sublime_plugin
import rainmeter


class RainmeterNewSkinFileCommand(sublime_plugin.WindowCommand):
    """Open a new view and insert a skin skeleton"""

    def run(self):
        view = self.window.new_file()
        view.run_command(
                "insert_snippet", 
                {"name": "Packages/Rainmeter/Snippets/skin.sublime-snippet"})
        
        if os.path.exists("Packages/User/Rainmeter.tmLanguage"):
            view.set_syntax_file("Packages/User/Rainmeter.tmLanguage")
        else:
            view.set_syntax_file("Packages/Rainmeter/Rainmeter.tmLanguage")


class RainmeterNewSkinCommand(sublime_plugin.WindowCommand):
    """Create a new skin, complete with folders, open it and refresh Rainmeter

    Prompts the user for the name of a skin and creates a new skin of that
    name in the skins folder, if it doesn't already exist. Then opens the skin
    file, inserts a basic skin skeleton and refreshes Rainmeter.

    """

    def run(self):
        self.window.show_input_panel("Enter Skin Name:", 
                                     "", 
                                     lambda name: self.create_skin(name),
                                     None, 
                                     None)

    def create_skin(self, name):     
        skinspath = rainmeter.skins_path()        
        if not skinspath or not os.path.exists(skinspath):
            sublime.error_message(
                    "Error while trying to create new skin: " +
                    "Skins path could not be found. Please check the value" +
                    " of your \"skins_path\" setting.")
            return

        name = os.path.normpath(name.strip("\\").strip("/")) + "\\"

        # Path where the new ini file will be created
        newskinpath = os.path.join(skinspath, name)

        # Path where the @Resources folder should be created
        basepath = os.path.join(skinspath, 
                                re.match("(.*?)\\\\", name).group(1))

        try:
            os.makedirs(newskinpath)
        except os.error:
            sublime.error_message(
                    "Error while trying to create new skin: " +
                    "Directory " + newskinpath + " could not be created. " +
                    "Does it already exist?")
            return

        # Check which folders should be created
        settings = sublime.load_settings("Rainmeter.sublime-settings")
        make_resources = settings.get(
                "rainmeter_new_skin_create_resources_folder", 
                True)
        make_images = settings.get(
                "rainmeter_new_skin_create_images_folder", 
                True)
        make_fonts = settings.get(
                "rainmeter_new_skin_create_fonts_folder", 
                True)
        make_scripts = settings.get(
                "rainmeter_new_skin_create_scripts_folder", 
                True)

        try:
            if make_resources: 
                os.makedirs(os.path.join(basepath, "@Resources"))
                if make_images: 
                    os.makedirs(os.path.join(basepath, "@Resources\\Images"))
                if make_fonts: 
                    os.makedirs(os.path.join(basepath, "@Resources\\Fonts"))
                if make_scripts: 
                    os.makedirs(os.path.join(basepath, "@Resources\\Scripts"))
        except os.error:
            sublime.status_message("Did not create @Resources folder or" +
                                   " subfolders because they already exist")
        

        window = self.window
        filename = os.path.basename(os.path.normpath(name))
        open(os.path.join(newskinpath, filename + ".ini"), 'a')
        newview = window.open_file(os.path.join(newskinpath, 
                                                filename + ".ini"))

        # We have to wait until the file is fully loaded (even if it's empty
        # because it was just created)
        sublime.set_timeout((lambda: self.open_skin_file(newview)), 100)

    def open_skin_file(self, view):       
        if view.is_loading():
            sublime.set_timeout(lambda: self.open_skin_file(self, newview), 
                                100)
            return

        view.run_command(
                "insert_snippet", 
                {"name": "Packages/Rainmeter/Snippets/skin.sublime-snippet"})

        if os.path.exists("Packages/User/Rainmeter.tmLanguage"):
            view.set_syntax_file("Packages/User/Rainmeter.tmLanguage")
        else:
            view.set_syntax_file("Packages/Rainmeter/Rainmeter.tmLanguage")

        sublime.run_command("rainmeter_refresh")
