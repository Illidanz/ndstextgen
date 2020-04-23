# NDS Text Generator
Command line tool to render text from NDS .NFTR fonts.  
## Run from pip
`pip install ndstextgen`  
`ndstextgen --help`  
## Run from source
Install pipenv.  
`pipenv install`  
`pipenv run ndstextgen --help`  
## Usage
`ndstextgen <options> FONT "TEXT"`  
Example: `ndstextgen --color red font.NFTR "Print multiline\nred text."`  
`FONT`: (Required) Filename of the font, .NFTR extension can be omitted.  
`TEXT`: (Required) Text to write. "\\n" can be used for a line break.  
`--out <file>`: Output file. Default: text.png  
`--vert <int>`: Vertical spacing between lines. Default: 2  
`--fw <int>`: Use a fixed width instead of the VWF values in the font.  
`--color <text>`: Color to apply to the font. Default: black  
`--size <int>`: Maximum width/height for the generated image. Default: 512  
