import sublime, sublime_plugin, re

class IndentRainmeterCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		#compile regexs to be used later
		rwhitespace_line = re.compile("^([ \\t]*)(.*)$")
		rfold_comment = re.compile("^([ \\t]*)(;;.*)")
		rsection_head = re.compile("^([ \\t]*)(\\[.*)$")

		#traverse view line by line
		line_count = len(self.view.lines(sublime.Region(0, self.view.size())))

		current_indent = -1
		adjustment = -1

		for i in range(0, line_count):
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

	def description():
		return "Indent Ini for Code Folding"
