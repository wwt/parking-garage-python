from setuptools import setup, find_packages

setup(
    name="garage",
    version="1.0",
    packages=find_packages("src"),
    package_dir={"": "src"},
    url="https://github.com/wwt/parking-garage-python",
    license="Apache 2.0",
    author="Connor Barragan",
    author_email="Connor.Barragan@wwt.com",
    description="Parking garage code exercise.",
)
