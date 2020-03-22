import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="python-test-utils",
    version="0.1",
    author="Or Israeli",
    author_email="tur103103@gmail.com",
    description="A test utils package for testing python apps",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tur103/python_test_utils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
