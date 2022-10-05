import setuptools, os

with open(os.path.join(os.path.dirname(__file__), "README.md"), 'r', encoding='utf-8') as readme:
    README = readme.read()

setuptools.setup(
    name="easy_flask_swagger",
    version="1.0.0",
    author="Yash Makan",
    author_email="yashmakan.work@gmail.com",
    description="Package used to create flask swagger documentation in few minutes with least possible effort.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/YashMakan/easy-flask-swagger",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
