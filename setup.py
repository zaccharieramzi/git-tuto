import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="git-tuto",
    version="0.0.1",
    author="Zaccharie Ramzi",
    author_email="zaccharie.ramzi@gmail.com",
    description="Tutorial for git in open source projects, with a touch of CI.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zaccharieramzi/git-tuto",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
