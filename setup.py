import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lsj2319-gescape", # Replace with your own username
    version="0.0.1",
    author="Lee Jordan",
    author_email="hi@leesjordan.net",
    description="Plant flowers and scrubs in a relaxing virtual garden",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lsj2319/Garden-Escape-Python-Project",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    install_requires=["tkinter", "PIL"],
    python_requires='>=3.6',
    entry_points={"console_scripts": [
        "lsj2319=gardenescape.__main__:main"]},
)