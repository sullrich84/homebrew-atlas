from setuptools import setup, find_packages

setup(
    name="atlas",
    version="0.0.0",
    packages=find_packages(),
    entry_points={"console_scripts": ["atlas = atlas.__main__:main"]},
)
