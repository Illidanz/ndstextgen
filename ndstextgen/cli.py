import os
import click
from PIL import Image
from hacktools import common, nitro
__version__ = "1.0.1"


@common.cli.command(context_settings=dict(show_default=True))
@click.argument("font")
@click.argument("text")
@click.option("--out",   default="text.png", help="Output file.")
@click.option("--vert",  default=2,          help="Vertical spacing between lines.")
@click.option("--fw",    default=0,          help="Use a fixed width instead of the VWF values in the font.")
@click.option("--color", default="black",    help="Color to apply to the font.")
@click.option("--size",  default=512,        help="Maximum width/height for the generated image.")
def gen(font, text, out, vert, fw, color, size):
    """FONT is the font file, .NFTR extension can be omitted.

    TEXT is the text to write. "\\n" can be used for a line break."""
    if not os.path.isfile(font):
        if not font.lower().endswith(".nftr"):
            font = font + ".NFTR"
        if not os.path.isfile(font):
            common.logError("Font", font, "not found")
            return
    # Read the font data
    nftr = nitro.readNFTR(font)
    # Create the empty image
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    # Generate the text
    currentx = 0
    currenty = 0
    text = text.replace("\\n", "\n")
    for i in range(len(text)):
        c = text[i]
        if c == "\n":
            currentx = 0
            currenty += nftr.height + vert
            continue
        glyph = nftr.glyphs[c]
        glyphdata = nftr.plgc[glyph.index]
        img.paste(glyphdata, (currentx + glyph.start, currenty))
        if fw > 0:
            currentx += fw
        else:
            currentx += glyph.length
    # Tint the image
    if color != "black":
        alpha = img.getchannel("A")
        img = Image.new("RGBA", (size, size), color)
        img.putalpha(alpha)
    # Crop and save the image
    bbox = img.getbbox()
    img = img.crop(bbox)
    img.save(out, "PNG")
    common.logMessage("Done!")


def main():
    click.echo("ndstextgen version " + __version__)
    gen()
