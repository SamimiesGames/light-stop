from setuptools import find_packages, setup

NAME = "light-stop"
VERSION = "0.0.1"

AUTHOR = "SamimiesGames"
DESCRIPTION = ""


setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    license="MIT",
    description=DESCRIPTION,
    packages=find_packages(where="src"),
    package_dir={"": "src"}
)
