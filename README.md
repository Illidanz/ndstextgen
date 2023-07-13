# NDS Text Generator
Command line tool to render text from NDS .NFTR fonts.  
## Run from pip
`pip install ndstextgen`  
`ndstextgen --help`  
## Run from source
Install pipenv.  
`pipenv sync`  
`pipenv run python ndstextgen --help`  
## Command line usage
`ndstextgen <options> FONT "TEXT"`  
Example: `ndstextgen --color red font.NFTR "Print multiline\nred text."`  
`FONT`: (Required) Filename of the font, .NFTR extension can be omitted.  
`TEXT`: (Required) Text to write. "\\n" can be used for a line break. Can be the name of a UTF-8 file to read the text from.  
`--out <file>`: Output file, set empty to just return the image. Default: text.png  
`--vert <int>`: Vertical spacing between lines. Default: 2  
`--fw <int>`: Use a fixed width instead of the VWF values in the font.  
`--spacing <int>`: Additional horizontal spacing between characters.  
`--color <text>`: Color to apply to the font. Default: black  
`--bg <text>`: Background color. Default: transparent  
`--width <int>`: Set width for the generated image. Default: 256  
`--height <int>`: Set height for the generated image. Default: 256  
`--center`: Center each line.  
`--wwrap`: Automatic wordwrap.  
`--no-crop`: Don't crop the image before saving it.  
`--encoding <str>`: Encoding the font uses. See [Python documentation](https://docs.python.org/3/library/codecs.html#standard-encodings).  
## Script usage
```python
import ndstextgen
image = ndstextgen.gen("font.NFTR", "Print multiline\nred text.", color="red")
```
