from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("LICENSE.txt", "r") as fh:
    license = fh.read()

def setup_package():
    setup(
        name='sales-analysis',
        version='0.1',
        author='Joseph Moorhouse',
        license=license,
        description='A sales analysis package for an imaginary e-shop',
        long_description=long_description,
        packages=find_packages(include=["sales_analysis", "sales_analysis.*"]),
        install_requires=[
            "flask >= 1.1.1",
            "pytest",
            "pandas >= 1.0.0" 
        ],
    )

if __name__ == "__main__": 
    setup_package()