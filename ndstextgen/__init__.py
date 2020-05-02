def gen(font, text, out="text.png", vert=2, fw=0, spacing=0, color="black", bg="transparent", width=256, height=256, center=False, no_crop=False):
    from . import cli
    args = [font, text, "--out", out, "--vert", vert, "--fw", fw, "--spacing", spacing, "--color", color, "--bg", bg, "--width", width, "--height", height]
    if center:
        args.append("--center")
    if no_crop:
        args.append("--no-crop")
    return cli.gen(args, standalone_mode=False)
