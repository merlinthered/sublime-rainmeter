# sublime-rainmeter

This package for [Sublime Text 2][1] makes developing Rainmeter skins even more fun.

## Features

### Syntax Highlighting

Syntax highlighting is turned on by default for files with the .ini and .inc extensions. It works best with the included color schemes, although other color schemes might work, too. 

There are four built-in color schemes you can choose from by copying `Rainmeter.sublime-settings` from the Rainmeter package directory to your User directory and changing the path to the .tmTheme file.

![Color Schemes][im1] 

If a certain file type doesn't open with Rainmeter highlighting even though you want it to, select View > Syntax > Open all with current extension as... > Rainmeter.

### Code Completion

![Code Completion][im2]

Code completion is activated by default. While typing, it will suggest completions from a list of options, values, built-in variables and more. When auto-completing a bang, the required and optional (in braces) parameters are also added, and you can cycle through them by pressing `tab` or `shift+tab`.

Additionally, code snippets for common usages of each meter and measure type, and all native plugins are included. The names of those snippets start with a "t" for template, so if you want to insert a basic template for a string meter, type `tstring` and hit enter, if you want to insert a metadata block, type `tmetadata`. There is also a snippet with a basic structure of a skin file called `tskin`.

![Snippets][im3]

You can see all available snippets by looking in the `Snippets` folder in the Rainmeter package directory. If you feel that one of those snippets needs to be changed in order to be more useful, don't hesitate to contact me.

### Tools

<a name='AutomaticIndentation'/>
#### Code Folding

![Code Folding][im4]

Sublime Text 2 supports folding indented code sections. The command `indent_rainmeter` that is included in this package automatically indents a rainmeter source file so code folding is possible in a sensible way. Hit `ctrl+alt+i` to activate it. All options in a section are indented and can be folded away. Additionally, inserting a comment line starting with a double semicolon: `;;` will indent everything after it so it can be folded until the next `;;` that you indented by the same amount. This is useful if you want to fold a specific section of code, like all measures or meters. If you want to add a nice looking header for your foldable sections, try typing `divider` and hitting enter.

#### Color Picker

![Color Picker][im5]

Ever wanted to quickly adjust the color of a meter but found yourself unable to imagine what a rgb color will look like in your head? No more! I have adapted the awesome [Color Picker Plugin][4] created by weslly to work with rainmeter-style hex-color definitions. Place your mouse cursor in a hexadecimal color definition, or select it and hit `ctrl+shift+c`. This will open a color picker dialog and let you choose a color. If your cursor is currently not in a color definition, the hex code will be inserted at the cursor position. You can't adjust the alpha value, but it will be preserved after you chose the new color.

#### New Skin

![Tools Menu][im6]

The Rainmeter section in the Tools menu contains a handy command for creating a new skin. It will open a new buffer, insert a basic skin skeleton and change the syntax highlighting mode to Rainmeter. The same skeleton is also available as a snippet called `tskin`.

#### Refresh Skin/Rainmeter

The package includes a custom "build system" for Rainmeter, which lets you refresh the current skin with a single button press. Press `f7` or `ctrl+b` to refresh the current skin, or load it, if it's not currently active. Pressing `ctrl+shift+b` will refresh Rainmeter and all skins instead. Those commands are also available from the tools menu via `Build` and `Run`. If this is not working for you, see [After Installing](#postinstall).

## Installation

### using git

Create a directory "Rainmeter" in your Sublime Text 2 Package folder (`C:\Users\[Your Username]\AppData\Roaming\Sublime Text 2\Packages` on Windows). Then clone the package there using git: 

	git clone https://github.com/merlinthered/sublime-rainmeter.git

### by downloading sublime-package

Download the .sublime-package file from the [Downloads page][2] and place it in your "Installed Packages" directory (`C:\Users\[Your Username]\AppData\Roaming\Sublime Text 2\Installed Packages`)

I'm looking into adding the package to [Package Control][3], so installing and keeping up-to-date will be easier

<a name='postinstall'/>
## After Installing

If your Rainmeter is not installed in `C:\Program Files\Rainmeter`, copy the file `Rainmeter.sublime-build` into your User directory (`C:\Users\[Your Username]\AppData\Roaming\Sublime Text 2\Packages\User`) and edit it, replacing the path to Rainmeter with your own install location.

## Issues

The syntax definition tries to highlight all common language constructs properly. It might fail in some cases, where something is highlighted even though it's not supposed to be. One prominent example is that every number that has exactly 6 or 8 digits being highlighted like a hexadecimal color definition. I chose this explicitly because I think identifying the different parts in a color definition is more important than some incorrectly colored numbers. In most other cases, wrong highlighting is due to the inherent ambiguity in Rainmeter syntax. If you encounter one of those cases, don't hesitate to contact me, especially if you think you know how to fix it.

## Reference

### Used Commands
* indent_rainmeter
* new_skin
* color_pick

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
* [Color Picker plugin by weslly][4], which I tweaked to work with Rainmeter
* [RainLexer by poiru][5], which is another awesome tool for developing Rainmeter skins, for the inspiration and one of the color schemes.
* [Monokai Color Scheme by Wimer Hazenberg][6], for providing such an amazing composition of colors.
* [The Rainmeter Community][7], for being awesome and testing this package.

[1]: http://www.sublimetext.com/ "Sublime Text 2"
[2]: https://github.com/merlinthered/sublime-rainmeter/downloads "Downloads page"
[3]: http://wbond.net/sublime_packages/package_control "Package Control"
[4]: https://github.com/weslly/ColorPicker "Color Picker"
[5]: https://github.com/poiru/rainlexer "RainLexer"
[6]: http://www.monokai.nl/blog/2006/07/15/textmate-color-theme/ "Monokai"
[7]: http://www.rainmeter.net/ "Rainmeter"

[im1]: http://i.imgur.com/XszdQ.png "Color Schemes"
[im2]: http://i.imgur.com/3rDom.png "Code Completion"
[im3]: http://i.imgur.com/gPoip.png "Snippets"
[im4]: http://i.imgur.com/gX4gE.png "Code Folding"
[im5]: http://i.imgur.com/IsfIw.png "Color Picker"
[im6]: http://i.imgur.com/wufyq.png "Tools Menu"