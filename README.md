# PHP-Codebeautifier
This is a plugin for Sublime Text 3 that gives the option to run the phpcbf
## Prerequisite
You need the [PHP Codesniffer](https://github.com/squizlabs/PHP_CodeSniffer) more precise the code beautifier from them.
## Install
Clone this repo into your Packages folder of Sublime Text. If ```phpcbf``` is in your path you don't need to do much setup. Otherwise create a user config for this plugin and set the path to your executable.
```Javascript
{
  "path": "/path/to/your/phpcbf"
}
```

Please note that the executable has to be in the string.

## Usage
The usage is pretty straight forward just press ```CTRL+ALT+F``` or use the button in the Tools menu to execute it. For longer files give it a bit to run.

## Configuration
Nearly all configuration options from phpcbf are bound to options in the settings file. Please refer to the [documentiation](https://github.com/squizlabs/PHP_CodeSniffer/wiki/Fixing-Errors-Automatically) for phpcbf to know what they do.

The three most important ones are

1. path  - Sets the path to the phpcbf executable
2. level - Sets the code standard to follow. Default: psr-2
3. patch - Sets whenether patch command should be used. 
