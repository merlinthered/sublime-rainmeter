import sublime, sublime_plugin, rainmeter, os, re, threading
"""Module for opening paths containing Rainmeter-specific or Windows environment variables."""

#Files to open with sublime instead of the system default
settings = sublime.load_settings("Rainmeter.sublime-settings")
defexts = settings.get("rainmeter_default_open_sublime_extensions", "")
defexts = defexts.strip().strip(r"|").strip()
addexts = settings.get("rainmeter_open_sublime_extensions", "")
addexts = addexts.strip().strip(r"|").strip()

sublime_files = re.compile(r"(?i).*\.(" + addexts + "|" + defexts + r")\b")

def open_path(path, transient=False):
	"""Try to open a file or folder path or URL in the system default application, or in Sublime if it's a text file.

	Use transient=True to open a file in Sublime without assigning it a tab. 
	A tab will be created once the buffer is modified.

	Will return False if the path doesn't exist in the file system, and True otherwise.
	"""

	if not path: return False

	if not os.path.exists(path): return False
	
	sublime.set_timeout(lambda: sublime.status_message("Opening " + path), 10)
	if sublime_files.search(path): 
		if transient:
			sublime.set_timeout(lambda: sublime.active_window().open_file(path, sublime.TRANSIENT), 10)
		else:
			sublime.set_timeout(lambda: sublime.active_window().open_file(path), 10)
	else:
		os.startfile(path)

	return True

def open_url(url):
	"""Try opening a url with the system default for urls.

	Will return False if it's not a url, and True otherwise.
	"""
	if re.match(r"(?i)(https?|ftp)://", url.strip()):
		os.startfile(url)		
		sublime.set_timeout(lambda: sublime.status_message("Opening " + url), 10)
		return True
	else:
		return False


class TryOpenThread(threading.Thread):

	def __init__(self, line, region, opn):
		self.line = line
		self.region = region
		self.opn = opn
		threading.Thread.__init__(self)

	def run(self):
		#1. Selected text
		selected = self.line[self.region.a:self.region.b]
		if self.opn(selected): 
			return

		#2. String enclosed in double quotes

		#find the quotes before the current point (if any)
		lastquote=self.region.a-1
		while lastquote >= 0 and self.line[lastquote] != "\"":
			lastquote = lastquote - 1

		if not lastquote <= 0 and self.line[lastquote] == "\"":
			#find the quote after the current point (if any)
			nextquote = self.region.b
			while nextquote == len(self.line) or self.line[nextquote] != "\"":
				nextquote = nextquote + 1
			if not nextquote == len(self.line) and self.line[nextquote] == "\"":
				string = self.line[lastquote : nextquote].strip("\"")
				if self.opn(string):
					return

		#3. Region from last whitespace to next whitespace
		#find the space before the current point (if any)
		lastspace=self.region.a-1
		while lastspace >= 0 and self.line[lastspace] != " " and self.line[lastspace] != "\t":
			lastspace = lastspace - 1
		if lastspace <= 0 or self.line[lastspace] == " " or self.line[lastspace] == "\t":
			#find the space after the current point (if any)
			nextspace = self.region.b
			while nextspace < len(self.line) and self.line[nextspace] != " " and self.line[nextspace] != "\t":
				nextspace = nextspace + 1
			if nextspace >= len(self.line) or self.line[nextspace] == " " or self.line[nextspace] == "\t":
				string = self.line[lastspace : nextspace].strip()
				if self.opn(string):
					return

		#4. Everything after the first \"=\" until the end of the line (strip quotes)
		mtch = re.search(r"=\s*(.*)\s*$", self.line)
		if mtch and self.opn(mtch.group(1).strip("\"")): 
			return

		#5. Whole line (strip comment character at start)
		stripmatch = re.search(r"^[ \t;]*?([^ \t;].*)\s*$", self.line)
		print stripmatch.group(0)
		print stripmatch.group(1)
		if self.opn(stripmatch.group(1)):
			return


class RainmeterOpenPathsCommand(sublime_plugin.TextCommand):
	"""Try to open paths on lines in the current selection.

	Will try to open paths to files, folders or URLs on each line in the current selection.
	To achieve this, the following substrings of each line intersecting the selection are tested:

	1. The string inside the selection
	2. The string between possible quotes preceding and following the selection, if any
	3. The string between the preceding and following whitespace
	4. Everything after the first "=" on the line until the end of the line
	5. The whole line, stripped of preceding semicolons
	"""
	def run(self, edit):
		#Detect various scenarios of file paths and try to open them one after the other

		fnm = self.view.file_name()

		opn = lambda st: open_path(rainmeter.make_path(st, fnm)) or open_url(st)

		selection = self.view.sel()

		#Split all regions into individual segments on lines (using nicely confusing python syntax)
		lines = [j for i in map(lambda region: self.view.split_by_newlines(region), selection) for j in i]

		settings = sublime.load_settings("Rainmeter.sublime-settings")
		max_open_lines = settings.get("rainmeter_max_open_lines", 40)

		#refuse if too many lines selected to avoid freezing
		if len(lines) > max_open_lines and not sublime.ok_cancel_dialog("You are trying to open " + str(len(lines)) + " lines. \nThat's a lot, and could take some time. Try anyway?"):
			return

		found = False
		for linereg in lines:
			wholeline = self.view.line(linereg)
			thread = TryOpenThread(self.view.substr(wholeline), sublime.Region(linereg.a-wholeline.a, linereg.b-wholeline.a), opn)
			thread.start()

	def is_enabled(self):
		#Check if current syntax is rainmeter
		israinmeter = self.view.score_selector(self.view.sel()[0].a, "source.rainmeter")

		return israinmeter > 0

	def is_visible(self):
		return self.is_enabled()
