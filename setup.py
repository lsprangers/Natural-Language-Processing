import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cup_a_code_FrostSprangers",  # Replace with your own username
    version="0.0.1",
    author="Frost, Sprangers",
    author_email="sprangersluke@gmail.com",
    description="A small example package named eloquently",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lsprangers/Natural-Language-Processing",
    project_urls={
        "Bug Tracker": "https://github.com/lsprangers/Natural-Language-Processing/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.0",
)
