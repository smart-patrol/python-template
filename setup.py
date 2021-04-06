"""
    Setup file for demo-dsproject.
    Use setup.cfg to configure your project.

    This file was generated with PyScaffold 4.0.
    PyScaffold helps you to put up the scaffold of your new Python project.
    Learn more under: https://pyscaffold.org/
"""
from setuptools import setup, find_packages

base_packages = []

test_packages = ["pytest>=5.4.3", "black>=19.10b0", "flake8>=3.8.3"]

util_packages = ["pre-commit>=2.6.0"]

dev_packages = test_packages + util_packages


if __name__ == "__main__":
    try:
        setup(
            name="packagename",
            version="0.0.1",
            packages=find_packages(),
            extras_require={"dev": dev_packages, "test": test_packages},
        )
    except:  # noqa
        print(
            "\n\nAn error occurred while building the project, "
            "please ensure you have the most updated version of setuptools, "
            "setuptools_scm and wheel with:\n"
            "   pip install -U setuptools setuptools_scm wheel\n\n"
        )
        raise
