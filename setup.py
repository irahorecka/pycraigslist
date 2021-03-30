import pycraigslist
from setuptools import setup, find_packages


_classifiers = [
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Topic :: Software Development :: Libraries",
    "Topic :: Utilities",
]

if __name__ == "__main__":
    setup(
        name="pycraigslist",
        version=pycraigslist.__version__,
        author="Ira Horecka",
        author_email="ira89@icloud.com",
        url="https://github.com/irahorecka/pycraigslist",
        py_modules=["pycraigslist"],
        description="A simple and expressive Craigslist API wrapper.",
        long_description=open("README.rst", encoding="utf-8").read(),
        license="MIT",
        classifiers=_classifiers,
        packages=find_packages(),
    )
