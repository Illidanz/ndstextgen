from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="ndstextgen",
    version="1.7.5",
    author="Illidan",
    description="Command line tool to render text from NDS .NFTR fonts.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Illidanz/ndstextgen",
    packages=["ndstextgen"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": ["ndstextgen=ndstextgen.cli:main"],
    },
    install_requires=[
        "hacktools>=0.38.0",
        "click>=8.1.0",
        "pillow>=11.1.0"
    ],
    python_requires=">=3.7",
)
