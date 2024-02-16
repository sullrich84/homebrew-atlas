import os
from setuptools import setup, find_packages


def get_version():
    rel_path = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(rel_path, "atlas", "version.py")

    v = {}
    with open(path) as fp:
        exec(fp.read(), v)

    return v["__version__"]


setup(
    name="atlas",
    version=get_version(),
    packages=find_packages(),
    entry_points={"console_scripts": ["atlas = atlas.__main__:main"]},
)
