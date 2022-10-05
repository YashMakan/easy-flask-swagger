import os
import setuptools

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

setuptools.setup(
    name="easy_flask_swagger",
    version="0.0.1",
    author="Yash Makan",
    author_email="yashmakan.work@gmail.com",
    description="Package used to create flask swagger documentation in few minutes with least possible effort.",
    long_description="Package used to create flask swagger documentation in few minutes with least possible effort.",
    long_description_content_type="text/markdown",
    url="https://github.com/YashMakan/easy_flask_swagger",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
