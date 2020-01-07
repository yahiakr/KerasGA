import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="KerasGA",
    version="1.0.0",
    author="Yahia KERIM",
    author_email="yahiakerim@gmail.com",
    description="A simple and easy-to-use implementation of Genetic Algorithm for Keras NN models in Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yahiakr/KerasGA",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
)