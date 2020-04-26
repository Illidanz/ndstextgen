def gen(font, text, out="text.png", vert=2, fw=0, color="black", bg="transparent", width=256, height=256, no_crop=False):
    from . import cli
    args = [font, text, "--out", out, "--vert", vert, "--fw", fw, "--color", color, "--bg", bg, "--width", width, "--height", height]
    if no_crop:
        args.append("--no-crop")
    cli.gen(args)
