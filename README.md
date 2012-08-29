# Features

## Syntax Highlighting

Syntax highlighting is turned on by default for files with the .ini and .inc extensions. It works best with the included color schemes, although other color schemes might work, too. See [Selecting Your Color Scheme](#colorschemesettings) for instructions on how to change the color scheme.

![Color Schemes][im1] 

If a certain file type doesn't open with Rainmeter highlighting even though you want it to, select View > Syntax > Open all with current extension as... > Rainmeter.

## Code Completion

![Code Completion][im2]

Code completion is activated by default. While typing, it will suggest completions from a list of options, values, built-in variables and more. When auto-completing a bang, the required and optional (in braces) parameters are also added, and you can cycle through them by pressing `tab` or `shift+tab`.

Additionally, code snippets for common usages of each meter and measure type, and all native plugins are included. The names of those snippets start with a "t" for "template", so if you want to insert a basic template for a string meter, type `tstring` and hit enter, if you want to insert a metadata block, type `tmetadata`. There is also a snippet with a basic structure of a skin file called `tskin`.

![Snippets][im3]

You can see all available snippets by looking in the `Snippets` folder in the Rainmeter package directory. If you feel that one of those snippets needs to be changed in order to be more useful, don't hesitate to contact me.

## Tools

<a name='AutomaticIndentation'></a>
### Code Folding

![Code Folding][im4]

Sublime Text 2 supports folding indented code sections. The command `indent_rainmeter` that is included in this package automatically indents a rainmeter source file so code folding is possible in a sensible way. Hit `ctrl+alt+i` to activate it. All options in a section are indented and can be folded away. Additionally, inserting a comment line starting with a double semicolon: `;;` will indent everything after it so it can be folded until the next `;;` that you indented by the same amount. This is useful if you want to fold a specific section of code, like all measures or meters. If you want to add a nice looking header for your foldable sections, try typing `divider` and hitting enter.

### Color Picker

![Color Picker][im5]

Ever wanted to quickly adjust the color of a meter but found yourself unable to imagine what a rgb color will look like in your head? No more! I have adapted the awesome [Color Picker Plugin][4] created by weslly to work with rainmeter-style hex-color definitions. Place your mouse cursor in a hexadecimal color definition, or select it and hit `ctrl+shift+c`. This will open a color picker dialog and let you choose a color. If your cursor is currently not in a color definition, the hex code will be inserted at the cursor position. You can't adjust the alpha value, but it will be preserved after you chose the new color.

### New Skin

![Tools Menu][im6]

The Rainmeter section in the Tools menu contains a handy command for creating a new skin. It will open a new buffer, insert a basic skin skeleton and change the syntax highlighting mode to Rainmeter. The same skeleton is also available as a snippet called `tskin`.

### Refresh Skin/Rainmeter

The package includes a custom "build system" for Rainmeter, which lets you refresh the current skin with a single button press. Press `f7` or `ctrl+b` to refresh the current skin, or load it, if it's not currently active. Pressing `ctrl+shift+b` will refresh Rainmeter and all skins instead. Those commands are also available from the tools menu via `Build` and `Run`. If this is not working for you, see [After Installing](#postinstall).

# Installation

## with Package Control (recommended)

The package is pending to be added to the [Package Control][3] default channel, so installing will be very easy and updating will be automatic. For now, you have to add the repository to your Package Control manually.

To do this, open the command palette in Sublime Text 2 (`ctrl+shift+p`). Then, enter the URL of the project repository:

	https://github.com/merlinthered/sublime-rainmeter

Next, open your Package Control user settings (Preferences > Package Settings > Package Control > Settings - User) and add the following line at the very top, after the opening curly brace:

	"package_name_map": {"sublime-rainmeter": "Rainmeter"},

You should now be able to install the package via the "Package Control: Install Package" command.

Once the package is added to the default channel, these steps won't be necessary any more and you will be able to install the package out of the box.

## using git

Browse to your Sublime Text 2 Package folder (*C:\\Users\\\[Your Username\]\\AppData\\Roaming\\Sublime Text 2\\Packages* on Windows). Then clone the package there using git: 

	git clone https://github.com/merlinthered/sublime-rainmeter.git Rainmeter

Don't forget to update regularly by running

	git pull

in the Rainmeter package directory.

## by downloading sublime-package

Download the .sublime-package file from the [Downloads page][2] and place it in your "Installed Packages" directory (*C:\\Users\\\[Your Username]\AppData\\Roaming\\Sublime Text 2\\Installed Packages*). This download will not be updated as often

<a name='postinstall'></a>
# After Installing

## Setting up the Build System

If your Rainmeter is not installed in *C:\\Program Files\\Rainmeter*, copy the file *Rainmeter.sublime-build* into your User directory (*C:\\Users\\\[Your Username\]\\AppData\\Roaming\\Sublime Text 2\\Packages\\User*), rename it to *Rainmeter (User).sublime-build* and edit it, replacing the path to Rainmeter with your own install location. Make sure that "Automatic" or "Rainmeter (User)" is selected as the build system to use.

<a name="colorschemesettings"></a>
## Selecting Your Color Scheme

There are several built-in color schemes you can choose from. If you don't want to use the default color scheme "Monokai (Rainmeter)", you can select a custom one by editing your user settings: Preferences > Package Settings > Rainmeter > Settings - User. Add the following to specify your color scheme:

	"color_scheme": "Packages/Rainmeter/YourFavouriteScheme.tmTheme"

If the file was empty, you'll also have to add a "{" at the start of the file, and a "}" at the end of the file.

The following color schemes are currently included in the package:

* Lachgummi Joghurt.tmTheme
* Monokai (Rainmeter).tmTheme
* Nexus (Rainmeter).tmTheme
* RainLexer.tmTheme
* Rainmeter (Light).tmTheme

Using other color schemes that are not optimized for Rainmeter is possible, but will probably yield sub-optimal results.

# Additional Information

## Issues

The syntax definition tries to capture all common language constructs properly. It might fail in some cases, where something is highlighted even though it's not supposed to be. One prominent example is that every number that has exactly 6 or 8 digits being highlighted like a hexadecimal color definition. I chose this explicitly because I think identifying the different parts in a color definition is more important than some incorrectly colored numbers. In most other cases, wrong highlighting is due to the inherent ambiguity in Rainmeter syntax. If you encounter one of those cases, don't hesitate to contact me, especially if you think you know how to fix it.

## Hints for Color Scheme Designers

You can see all the different classes the syntax defines by looking into *Rainmeter.JSON-tmLanguage*. Perhaps even easier is copying the rainmeter-specific part from one of the included color schemes (it's pretty much at the top, and it's commented). All the classes with a short description what they mean are included there.

## Reference

### Used Commands
* indent_rainmeter
* new_skin
* rainmeter_color_pick

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
* Preferences > Package Settings > Rainmeter > Settings - Default
* Preferences > Package Settings > Rainmeter > Settings - User

# Acknowledgements
* [Color Picker plugin by weslly][4], which I tweaked to work with Rainmeter
* [RainLexer by poiru][5], which is another awesome tool for developing Rainmeter skins, for the inspiration and one of the color schemes.
* [Monokai Color Scheme by Wimer Hazenberg][6], for providing such an amazing composition of colors.
* [Kaelri](https://github.com/Kaelri) for contributing the "Nexus" color scheme.
* [The Rainmeter Community][7], for being awesome and testing this package.

[1]: http://www.sublimetext.com/ "Sublime Text 2"
[2]: https://github.com/merlinthered/sublime-rainmeter/downloads "Downloads page"
[3]: http://wbond.net/sublime_packages/package_control "Package Control"
[4]: https://github.com/weslly/ColorPicker "Color Picker"
[5]: https://github.com/poiru/rainlexer "RainLexer"
[6]: http://www.monokai.nl/blog/2006/07/15/textmate-color-theme/ "Monokai"
[7]: http://www.rainmeter.net/ "Rainmeter"

[im1]: http://i.imgur.com/esG5C.png "Color Schemes"
[im2]: http://i.imgur.com/ijcEU.png "Code Completion"
[im3]: http://i.imgur.com/O7FjT.png "Snippets"
[im4]: http://i.imgur.com/OEXo8.png "Code Folding"
[im5]: http://i.imgur.com/kdZXJ.png "Color Picker"
[im6]: http://i.imgur.com/DziPa.png "Tools Menu"