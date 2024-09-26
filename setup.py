from setuptools import setup, find_packages
with open("Readme.md") as f:
    if f is not None:
        readme = f.read()
setup(
    name='revit-extractor',
    version='0.1.1',
    description='A Library allow extract revit without open revit',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='chuongmep',
    author_email='chuongpqvn@gmail.com',
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=["aps-toolkit", "olefile"],
    package_dir={"": "."},
    include_package_data=True,

)