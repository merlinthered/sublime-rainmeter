# sublime-rainmeter

This is a package for [Sublime Text 2][1], adding support for Rainmeter Skin development.

## Features

### Syntax Highlighting

![Syntax Highlighting][im1]

### Code Completion
![Code Completion][im2]

* Names of options and valid values
* Parameters for bangs automatically added
* Snippets for common meter, measure and plugin unsages
* Snippets for Rainmeter and Metadata section
* Snippet for skin skeleton
* Snippet for code folding header comment (see [Automatic Indentation for Code Folding](#AutomaticIndentation))

### Color Schemes
![Color Schemes][im3]

### Tools

#### Automatic Indentation for Code Folding
<a name='AutomaticIndentation'/>
![Automatic Indentation][im4]

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

## Acknowledgements
[Color Picker plugin by weslly][4], which I tweaked to work with Rainmeter

[1]: http://www.sublimetext.com/ "Sublime Text 2"
[2]: https://github.com/merlinthered/sublime-rainmeter/downloads "Downloads page"
[3]: http://wbond.net/sublime_packages/package_control "Package Control"
[4]: https://github.com/weslly/ColorPicker "Color Picker"

[im1]:
[im2]:
[im3]:
[im4]:
[im5]:
[im6]:
