import sublime, sublime_plugin, re

class RainmeterIndentCommand(sublime_plugin.TextCommand):
	"""Indents a Rainmeter ini file so code folding is possible in a sensible way.
	
	Double semicolons at the start of a line indent everything until the next double semicolon
	so you can create custom fold markers.
	If nothing is selected, the whole file will be indented.
	If one or more regions are selected, only these lines will be indented
	without paying attention to the surroundings
	"""

	def run(self, edit):
		#compile regexs to be used later
		rwhitespace_line = re.compile("^([ \\t]*)(.*)$")
		rfold_comment = re.compile("^([ \\t]*)(;;.*)")
		rsection_head = re.compile("^([ \\t]*)(\\[.*)$")
		
		#if nothing is selected, apply to whole buffer
		if self.view.sel()[0].a == self.view.sel()[-1].b:
			regions = [sublime.Region(0, self.view.size())]
		else:	#if something is selected, apply only to selected regions
			regions = self.view.sel()

		for region in regions:
			#get numbers of regions' lines
			reg_lines = self.view.lines(region)
			line_nums = map(lambda reg: self.view.rowcol(reg.a)[0],reg_lines)

			#traverse selected lines			
			current_indent = -1
			adjustment = -1

			for i in line_nums:
				lines = self.view.lines(sublime.Region(0, self.view.size()))
				line = lines[i]
				line_content = self.view.substr(line)

				mfc = rfold_comment.search(line_content)
				#if current line is fold comment, extract indentation
				if mfc:			
					current_indent = len(mfc.group(1))
					adjustment = -1
				#else indent current line according to last fold comment
				else:				
					#strip leading whitespace
					mwl = rwhitespace_line.search(line_content)
					stripped_line = ""
					if mwl:
						stripped_line = mwl.group(2)
					#indent section heads by one more
					mse = rsection_head.search(stripped_line)
					if mse:
						adjustment = 0
						self.view.replace(edit, line, "\t" * (current_indent + 1) + stripped_line)
					else: #indent key = value line two more
						self.view.replace(edit, line, "\t" * (current_indent + 2 + adjustment) + stripped_line)

	def is_enabled(self):
		#Check if current syntax is rainmeter
		israinmeter = self.view.score_selector(self.view.sel()[0].a, "source.rainmeter")

		return israinmeter > 0

	def description(self):
		return "Indent Ini for Code Folding"
