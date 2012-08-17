# sublime-rainmeter

This package for [Sublime Text 2][1] makes developing Rainmeter skins even more fun.

## Features

### Syntax Highlighting

![Syntax Highlighting][im1]

Syntax highlighting is turned on by default for files with the .ini and .inc extensions. It works best with the included color schemes, although other color schemes might work, too. 

There are four builtin color schemes you can choose from by copying `Rainmeter.sublime-settings` from the Rainmeter package directory to your User directory and changing the path to the .tmTheme file.

![Color Schemes][im2] 

If a certain file type doesn't open with Rainmeter highlighting even though you want it to, select View > Syntax > Open all with current extension as... > Rainmeter.

### Code Completion

![Code Completion][im3]

Code completion is activated by default. While typing, it will suggest completions from a list of options, values, builtin variables and more. When auto-completing a bang, the required and optional (in braces) parameters are also added, and you can cycle through them by pressing `tab` or `shift+tab`.

Additionally, code snippets for common usages of each meter and measure type, and all native plugins are included. The names of those snippets start with a "t" for template, so if you want to insert a basic template for a string meter, type `tstring` and hit enter, if you want to insert a metadata block, type `tmetadata`. There is also a snippet with a basic structure of a skin file called `tskin`.

You can see all available snippets by looking in the `Snippets` folder in the Rainmeter package directory. If you feel that one of those snippets needs to be changed in order to be more useful, don't hestiate to contact me.

### Tools

<a name='AutomaticIndentation'/>
#### Automatic Indentation for Code Folding

![Automatic Indentation][im4]

Sublime Text 2 supports folding indented code sections. The command `indent_rainmeter` automatically indents a rainmeter source file so code folding is possible in a sensible way. Hit `ctrl+alt+i` to activate it. All options in a section are indented and can be folded away. Additionally, inserting a comment line starting with a double semicolon: `;;` will indent everything after it so it can be folded until the next `;;` that you indented by the same amount. This is useful if you want to fold a specific section of code, like all measures or meters. If you want to add a nice looking header for your foldable sections, try typing `divider` and hitting enter.

#### Color Picker

![Color Picker][im5]

#### New Skin

![New Skin Command][im6]

## Installation

### using git:
Create a directory "Rainmeter" in your Sublime Text 2 Package folder (`C:\Users\[Your Username]\AppData\Roaming\Sublime Text 2\Packages` on Windows). Then clone the package there using git: 

	git clone https://github.com/merlinthered/sublime-rainmeter.git

### download sublime-package:
Download the .sublime-package file from the [Downloads page][2] and place it in your "Installed Packages" directory (`C:\Users\[Your Username]\AppData\Roaming\Sublime Text 2\Installed Packages`)

I'm looking into adding the package to [Package Control][3], so installing and keeping up-to-date will be easier

## After Installing

If your Rainmeter is not installed in `C:\Program Files\Rainmeter`, copy the file `Rainmeter.sublime-build` into your User directory (`C:\Users\[Your Username]\AppData\Roaming\Sublime Text 2\Packages\User`) and edit it, replacing the path to Rainmeter with your own install location.

## Issues

The syntax definition tries to highlight all common language constructs properly. It might fail in some cases, where something is highlighted even though it's not supposed to be. One prominent example is that every number that has exactly 6 or 8 digits being highlighted like a hexadecimal color definition. I chose this explicitly because I think identifying the different parts in a color definition is more important than some incorrectly colored numbers. In most other cases, wrong highlighting is due to the inherent ambiguity in Rainmeter syntax. If you encounter one of those cases, don't hesitate to contact me, especially if you think you know how to fix it.

## Reference

### Used Commands
* indent_rainmeter
* color_pick
* new_skin

### Used Command Palette Commands
* Rainmeter: Indent for Code Folding
* Rainmeter: New Skin
* Rainmeter: Pick Color

### Used Key Bindings
* ctrl+alt+i (indent for code folding)
* ctrl+shift+c (pick color)

### Used Menu Entries
* Tools > Rainmeter > Indent for Code Folding
* Tools > Rainmeter > New Skin...

## Acknowledgements
[Color Picker plugin by weslly][4], which I tweaked to work with Rainmeter

[1]: http://www.sublimetext.com/ "Sublime Text 2"
[2]: https://github.com/merlinthered/sublime-rainmeter/downloads "Downloads page"
[3]: http://wbond.net/sublime_packages/package_control "Package Control"
[4]: https://github.com/weslly/ColorPicker "Color Picker"

[im1]:
[im2]: http://i.imgur.com/XszdQ.png "Color Schemes"
[im3]: 
[im4]:
[im5]:
[im6]:
